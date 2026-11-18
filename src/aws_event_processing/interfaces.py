"""Initial application boundary for AWS Event Processing.

The runtime is in development. Refine models and errors alongside the first
implementation; dict/list annotations mark contracts still to be formalized.
"""

class LiveEventProcessor:
    def process(self, event: dict) -> dict:
        """Apply a duplicate-safe state transition and return an acknowledgement decision."""
        raise NotImplementedError("Runtime implementation is in development.")

    def reconcile(self, session_id: str) -> dict:
        """Compare accepted source events with the materialized session view."""
        raise NotImplementedError("Runtime implementation is in development.")
