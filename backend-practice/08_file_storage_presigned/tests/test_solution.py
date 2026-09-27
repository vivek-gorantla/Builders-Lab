import sys
import os
import sqlite3
import pytest

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']

from solution import FileStorageService

@pytest.fixture
def db_conn():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()

def test_presigned_upload_and_confirm(db_conn):
    storage = FileStorageService(db_conn)
    presigned = storage.generate_presigned_upload_url("user_1", "report.pdf", "application/pdf", 1024)
    assert "upload_url" in presigned
    assert "file_id" in presigned

    file_id = presigned["file_id"]
    confirmed = storage.confirm_upload(file_id, checksum_sha256="dummy_sha256_hash")
    assert confirmed["status"] == "ACTIVE"

def test_presigned_download_url_permissions(db_conn):
    storage = FileStorageService(db_conn)
    presigned = storage.generate_presigned_upload_url("user_1", "photo.png", "image/png", 2048)
    file_id = presigned["file_id"]
    storage.confirm_upload(file_id, "hash")

    # Owner can get download url
    dl_url = storage.generate_presigned_download_url(file_id, requester_id="user_1")
    assert "signature" in dl_url or "token" in dl_url

    # Unauthorized requester raises PermissionError
    with pytest.raises(PermissionError):
        storage.generate_presigned_download_url(file_id, requester_id="user_unauthorized")

def test_disallowed_file_extension_rejected(db_conn):
    storage = FileStorageService(db_conn)
    with pytest.raises(ValueError):
        storage.generate_presigned_upload_url("user_1", "malicious_script.exe", "application/x-msdownload", 500)
