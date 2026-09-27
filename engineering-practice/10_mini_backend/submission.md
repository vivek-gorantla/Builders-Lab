# Submission Guide - Project 10: Mini Backend

Before submitting:
- [ ] User registration validates inputs and email formats.
- [ ] Task creation requires valid existing owner ID and title.
- [ ] Ownership checks raise `PermissionError` when non-owner attempts modification.
- [ ] Task state transitions adhere to valid statuses.
- [ ] `list_tasks` returns structured pagination dict (`items`, `total`, `page`, `page_size`, `total_pages`).
- [ ] All pytest unit tests pass.

## Evaluation Criteria
- **Functional Correctness**: 50 points
- **Service Layer Architecture & Authorization**: 20 points
- **Validation & Error Handling**: 10 points
- **Code Quality**: 10 points
- **Performance**: 10 points

**Total**: 100 points
