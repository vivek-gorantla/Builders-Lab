# Engineering Practice Repository

Welcome to your local Python engineering practice repository! This collection contains 10 real-world, self-contained Python software engineering projects designed to help you practice object-oriented design, data structures, concurrency, file systems, caching, event-driven architectures, and clean code principles.

## 🎯 Recommended Project Progression

| # | Project | Difficulty | Key Concepts |
|---|---|---|---|
| 01 | [Inventory Manager](./01_inventory_manager) | Beginner+ | OOP, state validation, dictionaries, report generation |
| 02 | [Expiring Cache](./02_expiring_cache) | Beginner+ | Timestamps, TTL, LRU eviction, capacity limits |
| 03 | [Job Queue](./03_job_queue) | Intermediate | Threading, Producer/Consumer pattern, locks, status management |
| 04 | [File Indexer](./04_file_indexer) | Intermediate | Pathlib, recursive traversal, searching, metadata sorting |
| 05 | [Log Processing Service](./05_log_processing_service) | Intermediate | File streaming, string parsing, metrics aggregation |
| 06 | [Notification Engine](./06_notification_engine) | Intermediate | Strategy pattern, interfaces, dependency injection, retries |
| 07 | [Task Scheduler](./07_task_scheduler) | Intermediate+ | Priority queues (`heapq`), background scheduling, thread wait loops |
| 08 | [Rate Limiter](./08_rate_limiter) | Intermediate+ | Sliding-window algorithm, per-client limits, `threading.Lock` |
| 09 | [Message Broker](./09_message_broker) | Advanced | Pub/Sub observer pattern, callback error isolation, async dispatch |
| 10 | [Mini Backend](./10_mini_backend) | Advanced | Service layer architecture, access control, validation, pagination |

## 🚀 How to Practice

1. Navigate into any project folder directly in Antigravity or your terminal:
   ```bash
   cd 01_inventory_manager
   ```
2. Read `README.md` and `problem.md` to understand the scenario, requirements, and design boundaries.
3. Open `solution.py` and write your implementation to replace the stubbed methods.
4. Run tests to verify your solution:
   ```bash
   python -m pytest
   ```
5. Check `submission.md` to review evaluation criteria and ensure your implementation satisfies all requirements.

## 🧪 Running All Tests Across Projects

Run a single project's tests:
```bash
cd 01_inventory_manager
python -m pytest
```

Run all project tests from root:
```bash
cd engineering-practice
python -m pytest
```

Run individual project tests:
```bash
cd 01_inventory_manager
python -m pytest
```