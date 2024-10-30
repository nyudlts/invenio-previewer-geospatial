from flask import current_app
from werkzeug.local import LocalProxy

current_previewer = LocalProxy(
    lambda: current_app.extensions["invenio-previewer-geospatial"]
)
"""Proxy object to the current previewer extension."""
