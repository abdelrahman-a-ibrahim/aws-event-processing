# Architecture

Status: proposed. Components shown below are implementation targets.

## Product context
A near-real-time processing service for session activity and attendance events. The design accounts for duplicate deliveries, concurrent workers, late updates and recovery from failed batches using Amazon SQS and DynamoDB.

## Component view
```text
Event producer -> SQS -> Worker -> DynamoDB
                   |       |
                   DLQ     +-> metrics / reconciliation
```

## Design decisions
- Standard versus FIFO and the business ordering requirement
- Atomic deduplication plus state mutation
- Idempotency-key lifetime and redrive limits

Record decisions and alternatives in [ADR 0001](adr/0001-system-boundaries.md). Define authoritative state, acknowledgement boundaries, identities, retry behavior and recovery ownership before implementing adapters.

## Interface boundary
`src/aws_event_processing/interfaces.py` defines the initial application boundary. Return models and error contracts remain to be specified. These interfaces do not implement the component graph.

## Integration boundaries
Local adapters and synthetic fixtures precede external integrations. Every live adapter needs an explicit identity, permission scope, timeout strategy and observability contract. Separate user-supplied content from execution authority.

## Deployment design
Document topology, dependency versions, configuration and state persistence alongside the first executable delivery. Record what local environments cannot establish about availability, ordering or durability.

## Compatibility
Version interfaces and fixtures when their semantics change. Sibling projects are optional integrations, not implicit filesystem dependencies.
