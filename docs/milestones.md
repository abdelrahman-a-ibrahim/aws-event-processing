# Implementation backlog

Status: all milestones unstarted. Check a task only when its evidence exists.

## M1 — Design and contracts

Define an event envelope, DynamoDB access patterns, late-event rules and SQS Standard versus FIFO tradeoffs.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

## M2 — Build the first path

Build an offline worker core with durable local state for experiments. Model duplicate, conflicting and out-of-order events before adding cloud adapters.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

## M3 — Integrate deliberately

Provision an isolated SQS queue, DLQ and DynamoDB tables. Use conditional updates/transactions where appropriate; explain atomicity boundaries.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

## M4 — Handle failure

Implement visibility handling, bounded retries, redrive controls and partial-batch outcomes if using Lambda. Model concurrent workers and deduplication expiry.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

## M5 — Demonstrate and operate

Measure event-to-state latency, duplicate handling, stale state and recovery. Record a cost estimate, measured usage and a full teardown inventory.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

