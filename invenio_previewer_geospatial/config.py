# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 NYU Digital Library Technology Services.
#
# Invenio-Previewer-Geospatial is free software; you can redistribute it
# and/or modify it under the terms of the MIT License; see LICENSE file for
# more details.

"""Provides previewers for geospatial file formats."""

PREVIEWER_GEOSPATIAL_BASE_TEMPLATE = "invenio_previewer_geospatial/base.html"
"""Default base template for the demo page."""

PREVIEWER_PREFERENCE = [
    "gpx",
]
"""Decides which previewers are available and their priority."""
