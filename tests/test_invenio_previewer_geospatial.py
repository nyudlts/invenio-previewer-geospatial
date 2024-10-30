# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 NYU Digital Library Technology Services.
#
# Invenio-Previewer-Geospatial is free software; you can redistribute it
# and/or modify it under the terms of the MIT License; see LICENSE file for
# more details.

"""Module tests."""
import importlib

from flask import Flask
from mock import patch
from pkg_resources import EntryPoint

from invenio_previewer_geospatial import InvenioPreviewerGeospatial


class MockEntryPoint(EntryPoint):
    """Mocking of entrypoint."""

    def load(self):
        """Mock load entry point."""
        return importlib.import_module(self.module_name)


def _mock_entry_points(group=None):
    """Mocking funtion of entrypoints."""
    data = {
        "invenio_previewer.previewers": [
            MockEntryPoint(
                "gpx",
                "invenio_previewer_geospatial.extensions.gpx",
            ),
        ],
    }
    names = data.keys() if group is None else [group]
    for key in names:
        for entry_point in data[key]:
            yield entry_point


def test_version():
    """Test version import."""
    from invenio_previewer_geospatial import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    InvenioPreviewerGeospatial(app)
    assert "invenio-previewer-geospatial" in app.extensions


@patch("pkg_resources.iter_entry_points", _mock_entry_points)
def test_entrypoint_previewer():
    """Test the entry points."""
    app = Flask("testapp")
    ext = InvenioPreviewerGeospatial(app)
    ext.load_entry_point_group("invenio_previewer.previewers")
    assert len(ext.previewers) == 1
