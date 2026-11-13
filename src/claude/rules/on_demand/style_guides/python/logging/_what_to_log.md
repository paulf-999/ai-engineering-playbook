<!-- created: 2026-08-28 -->
# ✅ What to Log

**Purpose:** Establish guidelines for useful logging — what information should be logged for debugging.

---

## ✅ What to log

**Log entry/exit for important functions:**

```python
def process_migration(plan_path: str, apply: bool) -> dict:
    logger.info(f"Starting migration process: plan={plan_path}, apply={apply}")
    try:
        result = migrate(plan_path, apply)
        logger.info(f"Migration complete: {result['created']} created, {result['skipped']} skipped")
        return result
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise
```

**Why:** Entry/exit logs create a breadcrumb trail for understanding program flow.

**Log state changes and decisions:**

```python
if connection.is_disabled:
    logger.warning(f"Connection '{connection.name}' is disabled (will not be migrated)")
    continue
```

**Why:** State changes show why the program took different paths.

**Log amounts and counts:**

```python
logger.info(f"Processing {len(connections)} connections from {num_sources} sources")
```

**Why:** Quantities help verify that the expected amount of work is being performed.

**Log configuration and setup:**

```python
logger.debug(f"Using config: base_url={client.base_url}, timeout={client.timeout}")
```

**Why:** Configuration context is essential for reproducing bugs.

**Log loop progress for long operations:**

```python
for i, conn in enumerate(connections, 1):
    if i % 100 == 0:
        logger.info(f"Processed {i}/{len(connections)} connections")
    process_connection(conn)
```

**Why:** Progress markers show that long operations are making forward progress (not hung).
