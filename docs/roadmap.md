# Delivery roadmap

Status: planned. No delivery stage is complete.

### 1. Contracts and system boundaries

Define an event envelope, DynamoDB access patterns, late-event rules and SQS Standard versus FIFO tradeoffs.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 2. Core implementation

Build an offline worker core with durable local state for experiments. Model duplicate, conflicting and out-of-order events before adding cloud adapters.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 3. Integrations and access controls

Provision an isolated SQS queue, DLQ and DynamoDB tables. Use conditional updates/transactions where appropriate; explain atomicity boundaries.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 4. Recovery and operational behavior

Implement visibility handling, bounded retries, redrive controls and partial-batch outcomes if using Lambda. Model concurrent workers and deduplication expiry.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 5. Release validation

Measure event-to-state latency, duplicate handling, stale state and recovery. Record a cost estimate, measured usage and a full teardown inventory.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

## Future scope

- DynamoDB hot-partition load experiment
- Projection rebuild from an immutable archive
- Backlog-aware worker scaling
- Compare Lambda with a long-running worker

Select and pin implementation dependencies when introduced. Scope is refined through architecture decisions; completion requires working behavior and verification evidence.
