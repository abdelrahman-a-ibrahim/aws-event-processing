# ADR 0001: System boundaries and implementation approach

Status: proposed / decision not yet made.

## Context
Process live attendance updates from fictional workshops. Events can arrive twice, late or out of order. Use SQS and DynamoDB to maintain a reliable view of session activity.

## Decision questions
- Standard versus FIFO and the business ordering requirement
- Atomic deduplication plus state mutation
- Idempotency-key lifetime and redrive limits

## Options
1. Small local implementation with synthetic adapters.
2. Integrated lab with real dependencies in a disposable environment.
3. A justified alternative to be supplied during design.

## Decision
Pending. Start by evaluating the smallest approach that can demonstrate the core invariant.

## Consequences to assess
Correctness, complexity, cost, recovery, trust boundaries, portability and maintenance burden.

## Evidence needed
A failure experiment, a working implementation slice and a comparison of the alternatives.

## Revisit when
Document a concrete load, team, correctness or operational constraint that invalidates the selected approach.
