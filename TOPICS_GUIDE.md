# 📖 Builders-Lab: Complete Engineering Topics & Training Guide

Welcome to the **Builders-Lab Topics & Training Guide**! This document provides the theoretical foundations, implementation patterns, and mini code tutorials for every major software engineering and backend system design concept tested across the 20 projects in this laboratory.

---

## 📋 Table of Contents

1. [OOP & Invariant Validation](#1-oop--invariant-validation)
2. [In-Memory Caching & LRU Eviction](#2-in-memory-caching--lru-eviction)
3. [Concurrency, Threading & Producer-Consumer Queues](#3-concurrency-threading--producer-consumer-queues)
4. [File Traversal & Memory-Efficient Streaming](#4-file-traversal--memory-efficient-streaming)
5. [Design Patterns: Strategy & Observer (Pub/Sub)](#5-design-patterns-strategy--observer-pubsub)
6. [Priority Queues & Scheduled Execution](#6-priority-queues--scheduled-execution)
7. [Sliding-Window Rate Limiting](#7-sliding-window-rate-limiting)
8. [Service Layer Architecture & Pagination](#8-service-layer-architecture--pagination)
9. [LLM Conversation Memory & Sliding Context Windows](#9-llm-conversation-memory--sliding-context-windows)
10. [Semantic Vector Search & RAG Engine](#10-semantic-vector-search--rag-engine)
11. [Webhooks, HMAC Signatures & Dead Letter Queues](#11-webhooks-hmac-signatures--dead-letter-queues)
12. [URL Shortening & Base62 Encoding](#12-url-shortening--base62-encoding)
13. [Fintech Double-Entry Ledgers & Balance Audits](#13-fintech-double-entry-ledgers--balance-audits)
14. [Inventory Locking & Order State Machines](#14-inventory-locking--order-state-machines)
15. [Salted Passwords, JWT Tokens & Token Blacklisting](#15-salted-passwords-jwt-tokens--token-blacklisting)
16. [S3 Pre-Signed URLs & File SHA256 Checksums](#16-s3-pre-signed-urls--file-sha256-checksums)
17. [Real-Time Gaming Leaderboards & Rank Calculations](#17-real-time-gaming-leaderboards--rank-calculations)
18. [DB-Backed Job Queue Architecture](#18-db-backed-job-queue-architecture)

---

## 1. OOP & Invariant Validation

### Concept Explanation
In enterprise backend development, domain entities (like Products, Users, Orders) must enforce **business invariants** (e.g. prices cannot be negative, stock cannot drop below zero). Encapsulation ensures that external code cannot put an object into an invalid state.

### Code Tutorial & Pattern
```python
class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        if not product_id:
            raise ValueError("Product ID cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")
            
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def deduct_stock(self, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity to deduct must be positive.")
        if quantity > self.stock:
            raise ValueError(f"Insufficient stock. Available: {self.stock}, Requested: {quantity}")
        self.stock -= quantity
```

### Tested In Projects
- `engineering-practice/01_inventory_manager`
- `engineering-practice/10_mini_backend`

---

## 2. In-Memory Caching & LRU Eviction

### Concept Explanation
Caches speed up data access by keeping hot items in memory. When memory capacity is reached, an **LRU (Least Recently Used)** strategy evicts the item that has not been accessed for the longest time. `collections.OrderedDict` provides $O(1)$ key lookup and order maintenance via `move_to_end()`.

### Code Tutorial & Pattern
```python
from collections import OrderedDict
import time
from typing import Any, Optional

class SimpleLRUCache:
    def __init__(self, capacity: int = 3):
        self.capacity = capacity
        self.cache: OrderedDict[str, tuple[Any, Optional[float]]] = OrderedDict()

    def set(self, key: str, value: Any, ttl_seconds: Optional[float] = None):
        expires_at = time.time() + ttl_seconds if ttl_seconds else None
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = (value, expires_at)
        
        if len(self.cache) > self.capacity:
            # Evict least recently used (first item)
            self.cache.popitem(last=False)

    def get(self, key: str) -> Optional[Any]:
        if key not in self.cache:
            return None
        val, expires_at = self.cache[key]
        if expires_at and time.time() > expires_at:
            del self.cache[key] # Expired
            return None
        self.cache.move_to_end(key) # Mark recently used
        return val
```

### Tested In Projects
- `engineering-practice/02_expiring_cache`
- `backend-practice/10_api_cache_middleware`

---

## 3. Concurrency, Threading & Producer-Consumer Queues

### Concept Explanation
When processing background tasks, worker threads pull work from a thread-safe FIFO queue (`queue.Queue`). Mutex locks (`threading.Lock`) prevent race conditions when multiple threads read/write shared state.

### Code Tutorial & Pattern
```python
import queue
import threading
import time

class WorkerQueue:
    def __init__(self, num_workers: int = 2):
        self.task_queue = queue.Queue()
        self.workers = []
        self.running = True
        
        for _ in range(num_workers):
            t = threading.Thread(target=self._worker_loop, daemon=True)
            t.start()
            self.workers.append(t)

    def submit_task(self, func, *args):
        self.task_queue.put((func, args))

    def _worker_loop(self):
        while self.running:
            try:
                func, args = self.task_queue.get(timeout=0.1)
                try:
                    func(*args)
                except Exception as e:
                    print(f"Worker task error: {e}")
                finally:
                    self.task_queue.task_done()
            except queue.Empty:
                continue
```

### Tested In Projects
- `engineering-practice/03_job_queue`
- `engineering-practice/08_rate_limiter`
- `backend-practice/06_db_connection_pool`

---

## 4. File Traversal & Memory-Efficient Streaming

### Concept Explanation
When reading multi-gigabyte log files, loading the whole file into RAM using `.read()` will cause Out-Of-Memory (OOM) crashes. Python file objects are **iterators**: iterating line-by-line streams content with $O(1)$ memory.

### Code Tutorial & Pattern
```python
from pathlib import Path

def process_large_log_file(file_path: Path):
    info_count = 0
    error_count = 0
    
    # Line-by-line memory efficient streaming
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "INFO" in line:
                info_count += 1
            elif "ERROR" in line:
                error_count += 1
                
    return {"INFO": info_count, "ERROR": error_count}
```

### Tested In Projects
- `engineering-practice/04_file_indexer`
- `engineering-practice/05_log_processing_service`

---

## 5. Design Patterns: Strategy & Observer (Pub/Sub)

### Concept Explanation
- **Strategy Pattern**: Encapsulates interchangeable algorithms behind an abstract interface (`abc.ABC`).
- **Observer / Pub/Sub Pattern**: Decouples message publishers from subscribers. Subscribers receive events without publishers knowing subscriber implementation details. **Error isolation** ensures one failing subscriber does not crash others.

### Code Tutorial & Pattern
```python
from abc import ABC, abstractmethod
from typing import Callable, Dict, List

# Strategy Pattern
class NotificationProvider(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass

# Pub/Sub Observer Pattern
class SimpleMessageBroker:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, topic: str, callback: Callable):
        self.subscribers.setdefault(topic, []).append(callback)

    def publish(self, topic: str, message: str):
        for callback in self.subscribers.get(topic, []):
            try:
                callback(message) # Exception isolation
            except Exception as e:
                print(f"Subscriber error suppressed: {e}")
```

### Tested In Projects
- `engineering-practice/06_notification_engine`
- `engineering-practice/09_message_broker`

---

## 6. Priority Queues & Scheduled Execution

### Concept Explanation
A **Min-Heap** (`heapq`) maintains elements sorted by priority key. In a task scheduler, tasks are pushed into a heap ordered by execution timestamp (`run_at`). The scheduler pops tasks when `time.time() >= run_at`.

### Code Tutorial & Pattern
```python
import heapq
import time

class PriorityScheduler:
    def __init__(self):
        self.heap = [] # List of tuples: (run_at, task_id, func)

    def schedule(self, task_id: str, run_at: float, func):
        heapq.heappush(self.heap, (run_at, task_id, func))

    def execute_due_tasks(self):
        now = time.time()
        while self.heap and self.heap[0][0] <= now:
            run_at, task_id, func = heapq.heappop(self.heap)
            func()
```

### Tested In Projects
- `engineering-practice/07_task_scheduler`

---

## 7. Sliding-Window Rate Limiting

### Concept Explanation
The **Sliding-Window Log** algorithm tracks request timestamps per client in a double-ended queue (`collections.deque`). Requests older than `(now - window_seconds)` are popped before checking if `len(deque) < limit`.

### Code Tutorial & Pattern
```python
from collections import deque
import threading
import time

class SlidingWindowRateLimiter:
    def __init__(self, limit: int = 5, window_seconds: float = 10.0):
        self.limit = limit
        self.window_seconds = window_seconds
        self.requests = {} # client_id -> deque of timestamps
        self.lock = threading.Lock()

    def allow(self, client_id: str) -> bool:
        with self.lock:
            now = time.time()
            if client_id not in self.requests:
                self.requests[client_id] = deque()
            
            dq = self.requests[client_id]
            # Prune expired timestamps
            while dq and dq[0] <= now - self.window_seconds:
                dq.popleft()
                
            if len(dq) < self.limit:
                dq.append(now)
                return True
            return False
```

### Tested In Projects
- `engineering-practice/08_rate_limiter`

---

## 8. Service Layer Architecture & Pagination

### Concept Explanation
The **Service Layer** pattern separates database domain logic from API presentation controllers. Pagination breaks large result sets into smaller pages using `offset = (page - 1) * page_size` and `total_pages = math.ceil(total / page_size)`.

### Code Tutorial & Pattern
```python
import math

def paginate_items(items: list, page: int = 1, page_size: int = 10) -> dict:
    total = len(items)
    total_pages = math.ceil(total / page_size) if total > 0 else 1
    
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated_items = items[start_idx:end_idx]
    
    return {
        "items": paginated_items,
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
    }
```

### Tested In Projects
- `engineering-practice/10_mini_backend`
- `backend-practice/04_idempotent_issue_service`

---

## 9. LLM Conversation Memory & Sliding Context Windows

### Concept Explanation
Large Language Model APIs do not store state between requests. Backend servers store conversation history arrays `[{"role": "system", ...}, {"role": "user", ...}, {"role": "assistant", ...}]`. To prevent exceeding LLM context limits, sliding context windows prune old user/assistant messages while keeping the system prompt intact.

### Code Tutorial & Pattern
```python
class LLMContextMemory:
    def __init__(self, max_history_messages: int = 4):
        self.max_history = max_history_messages
        self.system_prompt = {"role": "system", "content": "You are a helpful assistant."}
        self.messages = [self.system_prompt]

    def add_user_message(self, content: str):
        self.messages.append({"role": "user", "content": content})
        self._prune_context()

    def add_assistant_message(self, content: str):
        self.messages.append({"role": "assistant", "content": content})
        self._prune_context()

    def _prune_context(self):
        non_system = [m for m in self.messages if m["role"] != "system"]
        if len(non_system) > self.max_history:
            pruned = non_system[-self.max_history:]
            self.messages = [self.system_prompt] + pruned
```

### Tested In Projects
- `backend-practice/01_llm_chat_backend`

---

## 10. Semantic Vector Search & RAG Engine

### Concept Explanation
**Retrieval-Augmented Generation (RAG)** indexes text chunks as mathematical vectors. When a user asks a query, the query is vectorized and compared against document vectors using **Cosine Similarity**:
$$\text{Cosine Similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}$$
Top relevant document chunks are dynamically injected into the LLM system prompt.

### Code Tutorial & Pattern
```python
import math

def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)
```

### Tested In Projects
- `backend-practice/02_vector_rag_service`

---

## 11. Webhooks, HMAC Signatures & Dead Letter Queues

### Concept Explanation
Webhooks send HTTP POST payloads to customer servers. To prevent payload tampering, webhooks sign payloads using **HMAC SHA256**. Delivery engines retry transient HTTP errors and route permanently failing requests to a **Dead Letter Queue (DLQ)**.

### Code Tutorial & Pattern
```python
import hashlib
import hmac

def sign_webhook_payload(secret: str, payload_json_str: str) -> str:
    signature = hmac.new(
        secret.encode('utf-8'),
        payload_json_str.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    return f"sha256={signature}"
```

### Tested In Projects
- `backend-practice/03_webhook_dispatch_engine`

---

## 12. URL Shortening & Base62 Encoding

### Concept Explanation
URL Shorteners convert database primary key IDs into short strings using **Base62 encoding** (`0-9`, `a-z`, `A-Z`).

### Code Tutorial & Pattern
```python
BASE62_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode_base62(num: int) -> str:
    if num == 0:
        return BASE62_ALPHABET[0]
    arr = []
    base = len(BASE62_ALPHABET)
    while num > 0:
        rem = num % base
        arr.append(BASE62_ALPHABET[rem])
        num //= base
    return "".join(reversed(arr))
```

### Tested In Projects
- `backend-practice/04_url_shortener_analytics`

---

## 13. Fintech Double-Entry Ledgers & Balance Audits

### Concept Explanation
In financial systems, money cannot appear out of nowhere. Every transaction consists of equal debit and credit entries. The fundamental accounting invariant is:
$$\sum \text{Debits} = \sum \text{Credits}$$

### Code Tutorial & Pattern
```python
class DoubleEntryLedger:
    def __init__(self):
        self.entries = [] # List of {"account_id": str, "type": "DEBIT"/"CREDIT", "amount": float}

    def record_transfer(self, source_acc: str, target_acc: str, amount: float):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        # Debit source, Credit target
        self.entries.append({"account_id": source_acc, "type": "DEBIT", "amount": amount})
        self.entries.append({"account_id": target_acc, "type": "CREDIT", "amount": amount})

    def verify_integrity((self) -> bool:
        total_debits = sum(e["amount"] for e in self.entries if e["type"] == "DEBIT")
        total_credits = sum(e["amount"] for e in self.entries if e["type"] == "CREDIT")
        return abs(total_debits - total_credits) < 1e-6
```

### Tested In Projects
- `backend-practice/05_payment_ledger_service`

---

## 14. Inventory Locking & Order State Machines

### Concept Explanation
E-commerce checkouts lock product stock during order placement using database transactions to prevent **overselling**. If payment succeeds, status updates to `PAID`. If cancelled, locked stock is released back.

### Code Tutorial & Pattern
```python
class OrderStateMachine:
    VALID_TRANSITIONS = {
        "PENDING": ["PAID", "CANCELLED"],
        "PAID": ["REFUNDED"],
        "CANCELLED": [],
        "REFUNDED": [],
    }

    @classmethod
    def transition(cls, current_status: str, new_status: str) -> str:
        if new_status not in cls.VALID_TRANSITIONS.get(current_status, []):
            raise ValueError(f"Invalid transition from {current_status} to {new_status}")
        return new_status
```

### Tested In Projects
- `backend-practice/06_ecommerce_order_inventory`

---

## 15. Salted Passwords, JWT Tokens & Token Blacklisting

### Concept Explanation
- **Salted Password Hashing**: Passwords are hashed with unique random salts using `hashlib.pbkdf2_hmac` to prevent rainbow table attacks.
- **JWT Revocation**: Stateless JWT access tokens can be revoked before expiration by storing their signature in a database **token blacklist**.

### Code Tutorial & Pattern
```python
import hashlib
import os

def hash_password(password: str) -> tuple[str, str]:
    salt = os.urandom(16).hex()
    pwd_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        iterations=100000
    ).hex()
    return pwd_hash, salt
```

### Tested In Projects
- `backend-practice/07_auth_jwt_session_db`

---

## 16. S3 Pre-Signed URLs & File SHA256 Checksums

### Concept Explanation
Pre-signed URLs contain temporary authentication tokens and expiration timestamps signed by the server's secret key. Clients upload directly to storage, and the server verifies file integrity via **SHA256 checksums**.

### Code Tutorial & Pattern
```python
import hashlib
import hmac
import time

def generate_presigned_url(file_id: str, secret_key: str, expires_in_seconds: int = 300) -> str:
    expires_at = int(time.time()) + expires_in_seconds
    to_sign = f"{file_id}:{expires_at}"
    sig = hmac.new(secret_key.encode('utf-8'), to_sign.encode('utf-8'), hashlib.sha256).hexdigest()
    return f"https://storage.local/files/{file_id}?expires={expires_at}&signature={sig}"
```

### Tested In Projects
- `backend-practice/08_file_storage_presigned`

---

## 17. Real-Time Gaming Leaderboards & Rank Calculations

### Concept Explanation
Leaderboard ranks are calculated dynamically:
$$\text{Rank}(P) = 1 + \text{Count of players with Total Score} > \text{Score}(P)$$

### Code Tutorial & Pattern
```python
def compute_player_rank(scores_dict: dict[str, int], target_player_id: str) -> int:
    target_score = scores_dict[target_player_id]
    higher_players = sum(1 for score in scores_dict.values() if score > target_score)
    return 1 + higher_players
```

### Tested In Projects
- `backend-practice/09_realtime_leaderboard`

---

## 18. DB-Backed Job Queue Architecture

### Concept Explanation
In Celery/Sidekiq-style DB queues, background workers poll a relational `jobs` table for `PENDING` jobs, lock rows via database transactions, execute handlers, and automatically update status to `COMPLETED` or `FAILED` with retry counters.

### Code Tutorial & Pattern
```python
import sqlite3

def poll_and_lock_next_job(conn: sqlite3.Connection, worker_id: str):
    cursor = conn.cursor()
    # Select oldest pending job
    cursor.execute("SELECT job_id, task_type, payload FROM jobs WHERE status = 'PENDING' ORDER BY created_at ASC LIMIT 1")
    row = cursor.fetchone()
    if not row:
        return None
        
    job_id, task_type, payload = row
    cursor.execute("UPDATE jobs SET status = 'RUNNING', worker_id = ? WHERE job_id = ?", (worker_id, job_id))
    conn.commit()
    return {"job_id": job_id, "task_type": task_type, "payload": payload}
```

### Tested In Projects
- `backend-practice/10_distributed_job_scheduler_db`

---

## 🚀 How to Use This Guide for Training

1. Pick a project you want to build (e.g. `backend-practice/01_llm_chat_backend`).
2. Read the corresponding topic section in this guide to master the concept & implementation pattern.
3. Open `problem.md` and starter `solution.py` in the project folder.
4. Implement the solution based on the pattern you learned.
5. Run `python -m pytest` to verify your implementation!
