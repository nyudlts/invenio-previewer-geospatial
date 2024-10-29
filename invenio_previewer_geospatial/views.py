# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 NYU Digital Library Technology Services.
#
# Invenio-Previewer-Geospatial is free software; you can redistribute it
# and/or modify it under the terms of the MIT License; see LICENSE file for
# more details.

"""Provides previewers for geospatial file formats."""

from flask import Blueprint, render_template
from invenio_i18n import gettext as _

blueprint = Blueprint(
    "invenio_previewer_geospatial",
    __name__,
    template_folder="templates",
    static_folder="static",
)
