# Functional and quality requirements

Status: proposed requirements, not delivered capabilities.

## Purpose
A near-real-time processing service for session activity and attendance events. The design accounts for duplicate deliveries, concurrent workers, late updates and recovery from failed batches using Amazon SQS and DynamoDB.

## Target capabilities
- Define an event envelope, DynamoDB access patterns, late-event rules and SQS Standard versus FIFO tradeoffs.
- Build an offline worker core with durable local state for experiments. Model duplicate, conflicting and out-of-order events before adding cloud adapters.
- Provision an isolated SQS queue, DLQ and DynamoDB tables. Use conditional updates/transactions where appropriate; explain atomicity boundaries.
- Implement visibility handling, bounded retries, redrive controls and partial-batch outcomes if using Lambda. Model concurrent workers and deduplication expiry.
- Measure event-to-state latency, duplicate handling, stale state and recovery. Record a cost estimate, measured usage and a full teardown inventory.

## Acceptance criteria
- A duplicate cannot increment attendance twice, including after worker restart.
- Late events follow the documented ordering rule.
- Deduplication and state mutation cannot diverge silently at a crash boundary.
- Every sampled event is either applied, explicitly rejected or traceable in quarantine.

## Cross-cutting requirements
- Reproducible configuration and documented version requirements.
- Explicit invalid-input, authorization and dependency-failure behavior.
- Clearly defined durable state, retries and concurrency boundaries.
- Observable operations with bounded, non-sensitive diagnostic output.
- A documented resource lifecycle, recovery procedure and cleanup path.

## Scope control
This repository owns its implementation and contracts. Optional integrations with other personal projects use versioned interfaces. Sample data is synthetic. External accounts and paid services are not required for the current source checks.
