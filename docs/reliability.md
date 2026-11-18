# Reliability and failure verification

Status: verification scenarios planned; no results recorded yet.

## Required scenarios
- Run two workers on duplicate deliveries of the same event.
- Crash after the database update but before deleting the SQS message.
- Let an old event arrive after a newer update.
- Replay a DLQ batch containing both valid and invalid events.

## Verification protocol
For each implemented scenario, document:
1. Commit, runtime versions, environment and topology.
2. Input workload and the expected invariant.
3. Baseline observations, fault injection and timestamps.
4. Observed errors, duplicate effects or state inconsistencies.
5. Recovery steps and measured time to restore behavior.
6. Resource cleanup and remaining limitations.

A simulator establishes application behavior within its assumptions. Real service ordering, consistency, failover and durability claims require verification against the selected dependencies. Distinguish those results in reports.

## Release evidence
- A duplicate cannot increment attendance twice, including after worker restart.
- Late events follow the documented ordering rule.
- Deduplication and state mutation cannot diverge silently at a crash boundary.
- Every sampled event is either applied, explicitly rejected or traceable in quarantine.

Store concise reports in [verification results](verification/README.md). Targets and illustrative fixture values must not be reported as measurements.
