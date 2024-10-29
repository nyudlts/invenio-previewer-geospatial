# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 NYU Digital Library Technology Services.
#
# Invenio-Previewer-Geospatial is free software; you can redistribute it
# and/or modify it under the terms of the MIT License; see LICENSE file for
# more details.

"""Module tests."""

from flask import Flask

from invenio_previewer_geospatial import InvenioPreviewerGeospatial


def test_version():
    """Test version import."""
    from invenio_previewer_geospatial import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioPreviewerGeospatial(app)
    assert "invenio-previewer-geospatial" in app.extensions

    app = Flask("testapp")
    ext = InvenioPreviewerGeospatial()
    assert "invenio-previewer-geospatial" not in app.extensions
    ext.init_app(app)
    assert "invenio-previewer-geospatial" in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert "Welcome to Invenio-Previewer-Geospatial" in str(res.data)
