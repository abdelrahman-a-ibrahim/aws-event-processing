# Verification plan

Runtime behavior tests will be added with the implementation. The current source integrity check does not provide runtime coverage.

## Required behavior coverage
- A duplicate cannot increment attendance twice, including after worker restart.
- Late events follow the documented ordering rule.
- Deduplication and state mutation cannot diverge silently at a crash boundary.
- Every sampled event is either applied, explicitly rejected or traceable in quarantine.

## Failure coverage
- Run two workers on duplicate deliveries of the same event.
- Crash after the database update but before deleting the SQS message.
- Let an old event arrive after a newer update.
- Replay a DLQ batch containing both valid and invalid events.

Add domain tests, adapter contract tests and integration tests as those components are implemented. Include relevant invalid input, unauthorized access, concurrency, retry and restart scenarios. Real dependency guarantees require real integration evidence; mocks alone cannot establish ordering, replication, consistency or durability.

See [reliability](../docs/reliability.md) for execution/reporting requirements.
