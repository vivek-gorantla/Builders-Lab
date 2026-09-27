# Problem 08: File Storage & Pre-Signed URL Manager

## 1. Scenario
Cloud storage architectures (AWS S3, Google Cloud Storage) issue temporary signed upload and download URLs so client apps upload files directly to object storage without choking backend servers.

## 2. Goal
Implement `FileStorageService` managing file metadata in SQL/Postgres database and generating HMAC pre-signed URLs.

## 3. Required Class
- `FileStorageService`

## 4. Required Methods
- `generate_presigned_upload_url(user_id: str, filename: str, content_type: str, size_bytes: int) -> dict`
- `confirm_upload(file_id: str, checksum_sha256: str) -> dict`
- `generate_presigned_download_url(file_id: str, requester_id: str) -> str`
- `list_user_files(user_id: str) -> list[dict]`

## 5. Behavior
- File extension validation: Disallows executable files (`.exe`, `.bat`, `.sh`). Allowed: `.pdf`, `.png`, `.jpg`, `.txt`, `.csv`, `.zip`.
- `generate_presigned_upload_url`: Creates record in DB `files` with status `"PENDING"`. Generates signed upload URL string containing `file_id`, expiration timestamp, and HMAC signature.
- `confirm_upload`: Verifies `file_id` exists, stores SHA256 checksum, updates status to `"ACTIVE"`.
- `generate_presigned_download_url`: Enforces ownership check (`requester_id == file.owner_id`). Returns signed download URL string.

## 6. Validation Rules
- Disallowed file extension raises `ValueError`.
- Unauthorized download request raises `PermissionError`.

## 7. Edge Cases
- Generating download URL for unconfirmed / pending file raises `ValueError`.

## 8. Examples
```python
storage = FileStorageService()
url_info = storage.generate_presigned_upload_url("u1", "doc.pdf", "application/pdf", 100)
```

## 9. Constraints
- Pure Python standard library (`hmac`, `hashlib`, `sqlite3`).

## 10. Left for Developer Decision
- Pre-signed URL token layout (`https://storage.local/upload?file_id=X&expires=Y&sig=Z`).
