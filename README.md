# AWS Event Processing

An SQS and DynamoDB event-processing service designed for duplicate-safe state updates and recoverable delivery.

**Status: In development** · Personal project by Abdelrahman Ahmed

## Overview

A near-real-time processing service for session activity and attendance events. The design accounts for duplicate deliveries, concurrent workers, late updates and recovery from failed batches using Amazon SQS and DynamoDB.

## Current state

The repository currently contains the system design, delivery requirements, a synthetic input fixture and initial Python interfaces. Runtime behavior, service integrations and deployment are planned. Interface methods raise `NotImplementedError`; there is no running application or published runtime benchmark yet.

## Planned capabilities

- Asynchronous SQS processing with DynamoDB-backed state projections.
- Duplicate-safe state updates and concurrency controls.
- Explicit late-event handling and ordering rules.
- Visibility timeout management, dead-letter routing and controlled redrive.
- Latency metrics, reconciliation and resource lifecycle documentation.

Detailed scope is tracked in the [delivery roadmap](docs/roadmap.md) and [requirements](docs/requirements.md).

## Architecture

```text
Event producer -> SQS -> Worker -> DynamoDB
                   |       |
                   DLQ     +-> metrics / reconciliation
```

This is the proposed component design. See [architecture](docs/architecture.md) for boundaries and [architecture decisions](docs/adr/0001-system-boundaries.md) for the choices still to resolve.

## Technology direction

SQS · DynamoDB · Python · Idempotency · Eventual consistency.

These technologies describe the intended implementation. Dependencies and compatible versions will be pinned when introduced. Optional services are not required by the current source checks.

## Working with the source

```sh
git clone https://github.com/abdelrahman-a-ibrahim/aws-event-processing.git
cd aws-event-processing
python3 tools/check_project.py
```

Python 3.9+ is sufficient for the current standard-library source check. It parses Python and JSON and checks required project files. It does **not** run an application, validate deployment behavior or establish feature completion.

The initial application boundary is in [`src/aws_event_processing/interfaces.py`](src/aws_event_processing/interfaces.py). [`examples/scenario.json`](examples/scenario.json) provides a synthetic development input. Installation and runtime commands will be added with the first executable release.

## Quality and reliability

- A duplicate cannot increment attendance twice, including after worker restart.
- Late events follow the documented ordering rule.
- Deduplication and state mutation cannot diverge silently at a crash boundary.
- Every sampled event is either applied, explicitly rejected or traceable in quarantine.

These are acceptance targets. Failure scenarios are specified in [reliability verification](docs/reliability.md); [results](docs/verification/README.md) will be recorded as implementation progresses. Correctness and performance claims must reference an actual environment, workload and commit.

## Development roadmap

- [ ] Contracts and system boundaries
- [ ] Core implementation and behavior tests
- [ ] External adapters and scoped access
- [ ] Failure recovery and operational visibility
- [ ] Reproducible deployment and release validation

See [delivery stages and future scope](docs/roadmap.md). For deployment prerequisites and resource lifecycle, see [operations](docs/operations.md).

## Repository structure

```text
src/aws_event_processing/       Initial application interfaces
examples/                  Synthetic development inputs
tests/                     Behavior verification plan
docs/architecture.md       Component design and boundaries
docs/requirements.md       Functional and quality requirements
docs/roadmap.md            Delivery stages and future scope
docs/reliability.md        Failure and recovery scenarios
docs/operations.md         Runtime and deployment plan
docs/verification/         Results as implementation progresses
tools/check_project.py     Source integrity check
```

## Development

Use focused feature branches, add behavior tests with implementation changes and update the relevant architecture decision when guarantees change. Read [CONTRIBUTING.md](CONTRIBUTING.md).

This is an independent personal project. Examples use synthetic data. See [NOTICE.md](NOTICE.md) for licensing status.

## References

- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transactions.html
