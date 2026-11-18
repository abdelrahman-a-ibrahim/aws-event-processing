# ADR 0001: System boundaries and implementation approach

Status: proposed.

## Context
A near-real-time processing service for session activity and attendance events. The design accounts for duplicate deliveries, concurrent workers, late updates and recovery from failed batches using Amazon SQS and DynamoDB.

## Questions
- Standard versus FIFO and the business ordering requirement
- Atomic deduplication plus state mutation
- Idempotency-key lifetime and redrive limits

## Alternatives
- A local implementation with synthetic external adapters.
- An integrated deployment with real dependencies in an isolated environment.
- A smaller implementation that preserves the core invariant.

## Decision
Pending. Record the selected option, rejected alternatives and rationale before implementing external adapters.

## Consequences
Assess correctness, operational complexity, cost, security boundaries, recovery and maintenance. Define the concrete constraint that would justify revisiting the decision.
