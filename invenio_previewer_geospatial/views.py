# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 NYU Digital Library Technology Services.
#
# Invenio-Previewer-Geospatial is free software; you can redistribute it
# and/or modify it under the terms of the MIT License; see LICENSE file for
# more details.

"""Provides previewers for geospatial file formats."""

from flask import Blueprint, abort, current_app, request
from invenio_previewer.api import PreviewFile
from invenio_previewer.extensions import default

from .proxies import current_previewer

blueprint = Blueprint(
    "invenio_previewer_geospatial",
    __name__,
    template_folder="templates",
    static_folder="static",
)


def preview(pid, record, template=None, **kwargs):
    """Preview file for given record.

    Plug this method into your ``RECORDS_UI_ENDPOINTS`` configuration:

    .. code-block:: python

        RECORDS_UI_ENDPOINTS = dict(
            recid=dict(
                # ...
                route='/records/<pid_value/preview/<path:filename>',
                view_imp='invenio_previewer.views.preview',
                record_class='invenio_records_files.api:Record',
            )
        )
    """
    # Get file from record
    fileobj = current_previewer.record_file_factory(
        pid,
        record,
        request.view_args.get("filename", request.args.get("filename", type=str)),
    )
    if not fileobj:
        abort(404)

    # Try to see if specific previewer is set
    file_previewer = fileobj.get("previewer")

    # Find a suitable previewer
    fileobj = PreviewFile(pid, record, fileobj)
    for plugin in current_previewer.iter_previewers(
        previewers=[file_previewer] if file_previewer else None
    ):
        if plugin.can_preview(fileobj):
            try:
                return plugin.preview(fileobj)
            except Exception:
                current_app.logger.warning(
                    (
                        "Preview failed for {key}, in {pid_type}:{pid_value}".format(
                            key=fileobj.file.key,
                            pid_type=fileobj.pid.pid_type,
                            pid_value=fileobj.pid.pid_value,
                        )
                    ),
                    exc_info=True,
                )
    return default.preview(fileobj)


@blueprint.app_template_test("previewable")
def is_previewable(extension):
    """Test if a file can be previewed checking its extension."""
    return extension in current_previewer.previewable_extensions
