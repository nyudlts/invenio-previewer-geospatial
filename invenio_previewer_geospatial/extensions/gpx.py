"""GPX Previewer."""

from flask import render_template
from invenio_previewer.proxies import current_previewer

previewable_extensions = ["gpx"]


def can_preview(file):
    """Check if file can be previewed."""
    return file.is_local() and file.has_extensions(".gpx")


def preview(file):
    """Render the GPX template."""
    return render_template(
        "invenio_previewer_geospatial/gpx.html",
        file=file,
        js_bundles=current_previewer.js_bundles + ["gpx_js.js"],
        css_bundles=current_previewer.css_bundles + ["gpx_css.css"],
    )
