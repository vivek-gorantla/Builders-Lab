# 🚀 Builders-Lab: Hands-on Python Software & Backend Engineering Practice

Welcome to **Builders-Lab**! This repository is a structured, local engineering practice laboratory containing **20 real-world Python software engineering projects** divided into two practice suites:

1. **[Engineering Practice Suite](./engineering-practice)**: System design, data structures, concurrency, caching, queues, file processing, and service design.
2. **[Backend, DB & API Practice Suite](./backend-practice)**: Modern backend architecture, LLM/ChatGPT services, Vector RAG search, Webhooks, double-entry financial ledgers, JWT Auth, S3-style storage, and DB-backed queues.

Each project contains a realistic problem scenario, complete specification, starter solution skeleton (`solution.py`), unit test suite (`tests/test_solution.py`), and evaluation guide.

---

## 🛠️ Repository Structure Overview

```text
d:\Vivek\coding_practise\
│
├── engineering-practice/      # Core Software Engineering & System Design Suite (10 Projects)
│   ├── 01_inventory_manager/
│   ├── 02_expiring_cache/
│   ├── 03_job_queue/
│   ├── 04_file_indexer/
│   ├── 05_log_processing_service/
│   ├── 06_notification_engine/
│   ├── 07_task_scheduler/
│   ├── 08_rate_limiter/
│   ├── 09_message_broker/
│   └── 10_mini_backend/
│
└── backend-practice/          # Modern Backend, DB & API Architecture Suite (10 Projects)
    ├── 01_llm_chat_backend/
    ├── 02_vector_rag_service/
    ├── 03_webhook_dispatch_engine/
    ├── 04_url_shortener_analytics/
    ├── 05_payment_ledger_service/
    ├── 06_ecommerce_order_inventory/
    ├── 07_auth_jwt_session_db/
    ├── 08_file_storage_presigned/
    ├── 09_realtime_leaderboard/
    └── 10_distributed_job_scheduler_db/
```

---

## 📚 1. Engineering Practice Suite (`engineering-practice/`)

Focuses on core Python language features, Object-Oriented Design, data structures, concurrency, file streaming, and thread safety.

| # | Project | Key Concepts | Problem & Starter |
|---|---|---|---|
| **01** | **Inventory Manager** | OOP, state validation, dict indexing, stock reporting | [`01_inventory_manager`](./engineering-practice/01_inventory_manager) |
| **02** | **Expiring Cache** | TTL timestamps, LRU eviction, capacity limits | [`02_expiring_cache`](./engineering-practice/02_expiring_cache) |
| **03** | **Job Queue** | Threading, `queue.Queue`, Producer/Consumer, cancellation | [`03_job_queue`](./engineering-practice/03_job_queue) |
| **04** | **File Indexer** | `pathlib`, directory traversal, file metadata search | [`04_file_indexer`](./engineering-practice/04_file_indexer) |
| **05** | **Log Processing Service** | Line streaming, string parsing, metrics aggregation | [`05_log_processing_service`](./engineering-practice/05_log_processing_service) |
| **06** | **Notification Engine** | Strategy pattern, interfaces, retries, audit logs | [`06_notification_engine`](./engineering-practice/06_notification_engine) |
| **07** | **Task Scheduler** | Priority queues (`heapq`), timed wait loops, shutdown | [`07_task_scheduler`](./engineering-practice/07_task_scheduler) |
| **08** | **Rate Limiter** | Sliding-window algorithm, per-client limits, `threading.Lock` | [`08_rate_limiter`](./engineering-practice/08_rate_limiter) |
| **09** | **Message Broker** | Pub/Sub observer pattern, callback error isolation | [`09_message_broker`](./engineering-practice/09_message_broker) |
| **10** | **Mini Backend** | Service layer architecture, access control, pagination | [`10_mini_backend`](./engineering-practice/10_mini_backend) |

---

## ⚡ 2. Modern Backend, DB & API Suite (`backend-practice/`)

Focuses on modern cloud backend engineering, AI/LLM integration, database transactions, security, and production API design. Supports SQLite and PostgreSQL.

| # | Project | Key Concepts | Problem & Starter |
|---|---|---|---|
| **01** | **ChatGPT / LLM Chat API** | Conversation memory history, system prompts, token tracking, sliding context window | [`01_llm_chat_backend`](./backend-practice/01_llm_chat_backend) |
| **02** | **Semantic Vector RAG Search** | Text embeddings, Cosine similarity index, RAG prompt builder | [`02_vector_rag_service`](./backend-practice/02_vector_rag_service) |
| **03** | **Webhook Delivery Engine** | Event fan-out, HMAC SHA256 signatures, retries, Dead Letter Queue (DLQ) | [`03_webhook_dispatch_engine`](./backend-practice/03_webhook_dispatch_engine) |
| **04** | **URL Shortener & Analytics** | Base62 encoding, custom slugs, TTL expiration, DB click analytics | [`04_url_shortener_analytics`](./backend-practice/04_url_shortener_analytics) |
| **05** | **Fintech Payment Ledger** | Double-entry accounting ($\sum \text{debits} = \sum \text{credits}$), atomic transfers, zero-balance audit | [`05_payment_ledger_service`](./backend-practice/05_payment_ledger_service) |
| **06** | **Order & Inventory Locking** | Atomic stock reservations, overselling prevention, order state machine | [`06_ecommerce_order_inventory`](./backend-practice/06_ecommerce_order_inventory) |
| **07** | **OAuth2 / JWT Auth Service** | PBKDF2 password hashing, JWT access/refresh tokens, DB token blacklist | [`07_auth_jwt_session_db`](./backend-practice/07_auth_jwt_session_db) |
| **08** | **File Storage & Pre-Signed URLs** | AWS S3-style pre-signed URLs, HMAC signatures, checksum validation | [`08_file_storage_presigned`](./backend-practice/08_file_storage_presigned) |
| **09** | **Gaming Leaderboard & Stats** | Real-time rank calculation, country filters, win streak tracking | [`09_realtime_leaderboard`](./backend-practice/09_realtime_leaderboard) |
| **10** | **DB Background Job Scheduler** | Celery/Sidekiq DB queue architecture, worker polling concurrency, automatic retries | [`10_distributed_job_scheduler_db`](./backend-practice/10_distributed_job_scheduler_db) |

---

## 🏁 Quick Start & Workflow

### 1. Prerequisites
- Python 3.10+
- `pytest`

### 2. Practice Workflow
1. Navigate into any project folder:
   ```bash
   cd engineering-practice/01_inventory_manager
   # or
   cd backend-practice/01_llm_chat_backend
   ```
2. Read `README.md` and `problem.md` to understand the scenario, required API contract, and constraints.
3. Open `solution.py` and implement the stubbed methods.
4. Run unit tests to verify your implementation:
   ```bash
   python -m pytest
   ```
5. Check `submission.md` to evaluate your solution against the 100-point rubric.

### 3. Run Entire Test Suite

**Run all Engineering Practice tests:**
```bash
cd engineering-practice
python -m pytest
```

**Run all Backend Practice tests:**
```bash
cd backend-practice
python -m pytest
```

---

## ⚙️ Tech Stack & Dependencies

- **Language**: Python 3.10+
- **Database**: Standard Library `sqlite3` (compatible with PostgreSQL via `psycopg2` / `DATABASE_URL`)
- **Testing**: `pytest`
- **Standard Library Modules**: `threading`, `queue`, `heapq`, `hashlib`, `hmac`, `uuid`, `pathlib`, `abc`, `json`, `time`
