from flask import url_for
from invenio_db import db
from invenio_files_rest.models import ObjectVersion
from six import BytesIO


def create_file(record, filename, stream):
    """Create a file and add in record."""
    obj = ObjectVersion.create(record.bucket, filename, stream=stream)
    record.update(
        dict(
            _files=[
                dict(
                    bucket=str(record.bucket.id),
                    key=filename,
                    size=obj.file.size,
                    checksum=str(obj.file.checksum),
                    version_id=str(obj.version_id),
                ),
            ]
        )
    )
    record.commit()
    db.session.commit()


def preview_url(pid_val, filename):
    """Preview URL."""
    return url_for(
        "invenio_records_ui.recid_previewer", pid_value=pid_val, filename=filename
    )


def test_gpx_extension(testapp, webassets, record):
    """Test view with GPX files."""
    create_file(record, "test.gpx", BytesIO(b'<?xml version="1.0"?>'))

    with testapp.test_client() as client:
        res = client.get(preview_url(record["control_number"], "test.gpx"))
        assert "data-file-uri" in res.get_data(as_text=True)
