..
    Copyright (C) 2024 NYU Digital Library Technology Services.

    Invenio-Previewer-Geospatial is free software; you can redistribute it
    and/or modify it under the terms of the MIT License; see LICENSE file for
    more details.

==============================
 Invenio-Previewer-Geospatial
==============================

.. image:: https://github.com/nyudlts/invenio-previewer-geospatial/workflows/CI/badge.svg
        :target: https://github.com/nyudlts/invenio-previewer-geospatial/actions?query=workflow%3ACI

.. image:: https://img.shields.io/github/license/nyudlts/invenio-previewer-geospatial.svg
        :target: https://github.com/nyudlts/invenio-previewer-geospatial/blob/master/LICENSE

Provides previewers for geospatial file formats

Installation
------------

To add this package to your Invenio RDM instance:

Add Package
~~~~~~~~~~~

.. code:: bash

   $ cd your-invenio-rdm
   $ pipenv install git+https://github.com/nyudlts/invenio-previewer-geospatial.git

Add Previews to Invenio Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``invenio.cfg`` edit (or add) ``PREVIEWER_PREVIEWERS_ORDER`` and
``PREVIEWER_PREFERENCE`` to include the previewers provided by this
package:

::

   PREVIEWER_PREVIEWERS_ORDER = [
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

Allow Images from Open Street Map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``invenio.cfg`` edit ``APP_DEFAULT_SECURE_HEADERS`` to allow images
from OpenStreetMap:

::

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
               'data:',
           ]
       },
       ...
   }

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
