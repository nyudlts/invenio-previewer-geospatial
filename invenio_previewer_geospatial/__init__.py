# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 NYU Digital Library Technology Services.
#
# Invenio-Previewer-Geospatial is free software; you can redistribute it
# and/or modify it under the terms of the MIT License; see LICENSE file for
# more details.

"""Provides previewers for geospatial file formats."""

from .ext import InvenioPreviewerGeospatial
from .proxies import current_previewer

__version__ = "0.1.0"

__all__ = ("__version__", "current_previewer", "InvenioPreviewerGeospatial")
