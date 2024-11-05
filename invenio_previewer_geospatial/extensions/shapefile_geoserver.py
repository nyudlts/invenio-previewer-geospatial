"""Shapefile previews via GeoServer."""

from flask import current_app, render_template
from invenio_previewer.proxies import current_previewer
from invenio_previewer.utils import dotted_exts

previewable_extensions = ["shp"]


def can_preview(file):
    """Check if file can be previewed."""
    return file.is_local() and file.has_extensions(*dotted_exts(previewable_extensions))


def preview(file):
    """Render the Geoserver template."""
    return render_template(
        "invenio_previewer_geospatial/geoserver.html",
        record=file.record,
        wms_url_field=(
            current_app.config.get(
                "PREVIEWER_GEOSPATIAL_CUSTOM_FIELDS_GEOSERVER_WMS_URL"
            )
        ),
        layer_name_field=(
            current_app.config.get(
                "PREVIEWER_GEOSPATIAL_CUSTOM_FIELDS_GEOSERVER_LAYER_NAME"
            )
        ),
        bounds_field=(
            current_app.config.get(
                "PREVIEWER_GEOSPATIAL_CUSTOM_FIELDS_GEOSERVER_BOUNDS"
            )
        ),
        js_bundles=current_previewer.js_bundles + ["geoserver_js.js"],
        css_bundles=current_previewer.css_bundles + ["geoserver_css.css"],
    )
