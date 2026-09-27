# Submission Guide - Project 02: Expiring Cache

Before submitting, check:
- [ ] `ExpiringCache` initialized properly with optional capacity.
- [ ] Expired entries return `None` on `get()`.
- [ ] LRU eviction correctly removes the least recently accessed item when capacity is hit.
- [ ] `size()` returns active unexpired key count.
- [ ] `delete()` handles existing and missing keys cleanly.
- [ ] Tests pass.

## Evaluation Criteria
- **Functional Correctness**: 50 points
- **Edge Case & TTL Expiration**: 20 points
- **Error Handling**: 10 points
- **Code Quality**: 10 points
- **Performance**: 10 points

**Total**: 100 points
