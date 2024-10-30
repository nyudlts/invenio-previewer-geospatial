# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 NYU Digital Library Technology Services.
#
# Invenio-Previewer-Geospatial is free software; you can redistribute it
# and/or modify it under the terms of the MIT License; see LICENSE file for
# more details.

"""Provides previewers for geospatial file formats."""

import pkg_resources
from invenio_previewer.ext import load_or_import_from_config
from pkg_resources import DistributionNotFound, get_distribution
from werkzeug.utils import cached_property

from . import config
from .views import blueprint


class _InvenioPreviewerGeospatialState(object):
    """State object."""

    def __init__(self, app, entry_point_group=None):
        """Initialize state."""
        self.app = app
        self.entry_point_group = entry_point_group
        self.previewers = {}
        self._previewable_extensions = set()

    @cached_property
    def previewable_extensions(self):
        if self.entry_point_group is not None:
            self.load_entry_point_group(self.entry_point_group)
            self.entry_point_group = None
        return self._previewable_extensions

    @cached_property
    def record_file_factory(self):
        """Load default record file factory."""
        try:
            get_distribution("invenio-records-files")
            from invenio_records_files.utils import record_file_factory

            default = record_file_factory
        except DistributionNotFound:

            def default(pid, record, filename):
                return None

        return load_or_import_from_config(
            "PREVIEWER_RECORD_FILE_FACOTRY",
            app=self.app,
            default=default,
        )

    @property
    def css_bundles(self):
        return self.app.config["PREVIEWER_BASE_CSS_BUNDLES"]

    @property
    def js_bundles(self):
        return self.app.config["PREVIEWER_BASE_JS_BUNDLES"]

    def register_previewer(self, name, previewer):
        """Register a previewer in the system."""
        if name in self.previewers:
            assert (
                name not in self.previewers
            ), "Previewer with same name already registered"
        self.previewers[name] = previewer
        if hasattr(previewer, "previewable_extensions"):
            self._previewable_extensions |= set(previewer.previewable_extensions)

    def load_entry_point_group(self, entry_point_group):
        """Load previewers from an entry point group."""
        for ep in pkg_resources.iter_entry_points(group=entry_point_group):
            self.register_previewer(ep.name, ep.load())

    def iter_previewers(self, previewers=None):
        """Get previewers ordered by PREVIEWER_PREVIEWERS_ORDER."""
        if self.entry_point_group is not None:
            self.load_entry_point_group(self.entry_point_group)
            self.entry_point_group = None

        previewers = previewers or self.app.config.get("PREVIEWER_PREFERENCE", [])

        for item in previewers:
            if item in self.previewers:
                yield self.previewers[item]


class InvenioPreviewerGeospatial(object):
    """Invenio-Previewer-Geospatial extension."""

    def __init__(self, app, **kwargs):
        """Extension initialization."""
        if app:
            self._state = self.init_app(app, **kwargs)

    def init_app(self, app, entry_point_group="invenio_previewer.previewers"):
        """Flask application initialization."""
        self.init_config(app)
        app.register_blueprint(blueprint)
        state = _InvenioPreviewerGeospatialState(
            app, entry_point_group=entry_point_group
        )
        app.extensions["invenio-previewer-geospatial"] = state
        return state

    def init_config(self, app):
        """Initialize configuration."""
        app.config.setdefault("PREVIEWER_BASE_TEMPLATE", "invenio_previewer/base.html")

        for k in dir(config):
            if k.startswith("PREVIEWER_"):
                app.config.setdefault(k, getattr(config, k))

    def __getattr__(self, name):
        """Proxy to state object."""
        return getattr(self._state, name, None)
