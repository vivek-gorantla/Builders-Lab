# Cool Modern Backend, DB & API Engineering Projects

Welcome to your local Python **Cool Modern Backend, DB & API Engineering Practice** repository! This collection contains 10 real-world, high-impact backend engineering projects reflecting actual production systems built at modern tech companies (ChatGPT/LLM services, Vector Search RAG, Webhooks, URL Shorteners with Analytics, Double-Entry Payment Ledgers, E-Commerce Order/Stock locking, OAuth2/JWT DB auth, Pre-signed S3 Storage, Real-Time Gaming Leaderboards, and DB-backed Job Schedulers).

All projects support real database connections (SQLite by default, or hosted/Docker PostgreSQL via DB connection strings).

## 🎯 The 10 Modern Backend Projects

| # | Project | Description & Key Concepts | Starter File |
|---|---|---|---|
| 01 | [ChatGPT / LLM Chat Assistant API](./01_llm_chat_backend) | Conversation history, system prompts, token usage tracking, sliding context window | `01_llm_chat_backend/solution.py` |
| 02 | [Semantic Vector Search & RAG Engine](./02_vector_rag_service) | Document vectorization, cosine similarity index, RAG LLM prompt builder | `02_vector_rag_service/solution.py` |
| 03 | [Real-Time Webhook Delivery Engine](./03_webhook_dispatch_engine) | Event fan-out, HMAC SHA256 signatures, retry backoff, Dead Letter Queue (DLQ) | `03_webhook_dispatch_engine/solution.py` |
| 04 | [URL Shortener & Analytics Service](./04_url_shortener_analytics) | Base62 encoding, custom slugs, TTL expiration, DB click analytics | `04_url_shortener_analytics/solution.py` |
| 05 | [Fintech Double-Entry Payment Ledger](./05_payment_ledger_service) | Double-entry accounting ($\sum 	ext{debits} = \sum 	ext{credits}$), atomic transfers, zero-balance audit | `05_payment_ledger_service/solution.py` |
| 06 | [E-Commerce Order & Inventory Locking](./06_ecommerce_order_inventory) | Inventory stock reservations, overselling prevention, order state machine | `06_ecommerce_order_inventory/solution.py` |
| 07 | [OAuth2 / JWT Auth & Session Service](./07_auth_jwt_session_db) | PBKDF2 password hashing, JWT tokens, DB token revocation/blacklist | `07_auth_jwt_session_db/solution.py` |
| 08 | [File Storage & Pre-Signed URL Manager](./08_file_storage_presigned) | AWS S3-style pre-signed URLs, HMAC signatures, checksum validation | `08_file_storage_presigned/solution.py` |
| 09 | [Gaming Leaderboard & Stats Engine](./09_realtime_leaderboard) | Real-time global rank calculation, country filters, win streak tracking | `09_realtime_leaderboard/solution.py` |
| 10 | [DB-Backed Background Job Scheduler](./10_distributed_job_scheduler_db) | Celery/Sidekiq DB queue architecture, worker polling, automatic retries | `10_distributed_job_scheduler_db/solution.py` |

## 🚀 How to Practice

1. Navigate into any project folder:
   ```bash
   cd 01_llm_chat_backend
   ```
2. Read `README.md` and `problem.md` to understand requirements.
3. Open `solution.py` and implement the stubbed methods.
4. Run tests:
   ```bash
   python -m pytest
   ```

## 🧪 Running All Tests Across Projects

```bash
python -m pytest
```
