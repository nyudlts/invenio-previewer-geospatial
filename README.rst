Invenio-Previewer-Geospatial
============================

|ci-badge| |license|

Provides previewers for geospatial file formats

Installation
------------

To add this package to your Invenio RDM instance:

Add Package and Build Assets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   $ cd your-invenio-rdm
   $ pipenv install git+https://github.com/nyudlts/invenio-previewer-geospatial.git
   $ invenio-cli assets build

Add Previews to Invenio Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``invenio.cfg`` edit (or add) ``PREVIEWER_PREVIEWERS_ORDER`` and
``PREVIEWER_PREFERENCE`` to include the previewers provided by this
package:

::

   PREVIEWER_PREVIEWERS_ORDER = [
       "invenio_previewer.extensions.geoserver",
       "invenio_previewer.extensions.gpx",
       "invenio_previewer.extensions.csv_papaparsejs",
       "invenio_previewer.extensions.json_prismjs",
       "invenio_previewer.extensions.simple_image",
       "invenio_previewer.extensions.xml_prismjs",
       "invenio_previewer.extensions.mistune",
       "invenio_previewer.extensions.pdfjs",
       "invenio_previewer.extensions.zip",
       "invenio_previewer.extensions.ipynb",
       "invenio_previewer.extensions.audio_videojs",
       "invenio_previewer.extensions.video_videojs",
       "invenio_previewer.extensions.txt_previewer",
       "invenio_previewer.extensions.default",
   ]

   PREVIEWER_PREFERENCE = [
       "geoserver",
       "gpx",
       "csv_papaparsejs",
       "json_prismjs",
       "simple_image",
       "xml_prismjs",
       "mistune",
       "pdfjs",
       "zip",
       "ipynb",
       "audio_videojs",
       "video_videojs",
       "txt",
   ]

Allow Images from Open Street Map & GeoServers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``invenio.cfg`` edit ``APP_DEFAULT_SECURE_HEADERS`` to allow images
from OpenStreetMap:

.. code:: python

   APP_DEFAULT_SECURE_HEADERS = {
       'content_security_policy': {
           'default-src': [
               "'self'",
               'data:',
               "'unsafe-inline'",
               "blob:",
           ],
           'img-src': [
               "'self'",
               "https://*.openstreetmap.org",
               "https://maps-public.geo.nyu.edu/geoserver/sdr/wms",
               'data:',
           ]
       },
       ...
   }

Add Custom GeoServer Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``invenio.cfg`` add the following namespace, custom fields and UI elements:

.. code:: python

    # Set these if you want to override the field names below
    PREVIEWER_GEOSPATIAL_CUSTOM_FIELDS_GEOSERVER_WMS_URL = "geoserver:wms_url"
    PREVIEWER_GEOSPATIAL_CUSTOM_FIELDS_GEOSERVER_WFS_URL = "geoserver:wfs_url"
    PREVIEWER_GEOSPATIAL_CUSTOM_FIELDS_GEOSERVER_LAYER_NAME = "geoserver:layer_name"

    RDM_NAMESPACES = {
        "geoserver": "https://geoserver.org/"
    }

    RDM_CUSTOM_FIELDS = [
        TextCF(name="geoserver:wms_url"),
        TextCF(name="geoserver:wfs_url"),
        TextCF(name="geoserver:layer_name"),
    ]

    RDM_CUSTOM_FIELDS_UI = [
        {
            "section": _("GeoServer"),
            "fields": [
                dict(
                    field="geoserver:wms_url",
                    ui_widget="Input",
                    props=dict(
                        label="WMS URL",
                        placeholder="https://maps-public.geo.nyu.edu/geoserver/sdr/wms",
                        icon="linkify",
                        description="GeoServer WMS Service Base URL",
                        required=False
                    )
                ),
                dict(
                    field="geoserver:wfs_url",
                    ui_widget="Input",
                    props=dict(
                        label="WMS URL",
                        placeholder="https://maps-public.geo.nyu.edu/geoserver/sdr/wfs",
                        icon="linkify",
                        description="GeoServer WFS Service Base URL",
                        required=False
                    )
                ),
                dict(
                    field="geoserver:layer_name",
                    ui_widget="Input",
                    props=dict(
                        label="Layer Name",
                        placeholder="sdr:nyu_2451_12345",
                        icon="pencil",
                        description="Name of the GeoServer Layer this data can be found in",
                        required=False
                    )
                )
            ]
        }
    ]


Development
-----------

To check out the project, install dependencies and run the test suite,
do the following:

.. code:: bash

   $ git clone git@github.com:nyudlts/invenio-previewer-geospatial.git
   $ cd invenio-previewer-geospatial
   $ python -m venv .venv
   $ source .venv/bin/activate
   $ pip install --upgrade pip
   $ pip install ".[all,tests]"
   $ ./run-tests.sh

.. |ci-badge| image:: https://github.com/nyudlts/invenio-previewer-geospatial/workflows/CI/badge.svg
   :target: https://github.com/nyudlts/invenio-previewer-geospatial/actions?query=workflow%3ACI
.. |license| image:: https://img.shields.io/github/license/nyudlts/invenio-previewer-geospatial.svg
   :target: https://github.com/nyudlts/invenio-previewer-geospatial/blob/master/LICENSE
