# Requirement matrix

| Requirement | Implementation | Proof |
|---|---|---|
| Compare an agenda with published minutes | `review_session` retrieves both records and classifies every agenda item | Contract tests and `evidence/live-run.json` |
| Preserve review provenance | URLs, SHA-256 digests, citations, outcomes, owner, and reviewer are stored | `contracts/contract.py` and finalized receipt |
| Keep lifecycle deterministic | Contract code derives `COMPLETE`, `FOLLOWUP`, or `INCOMPLETE` | Unit tests cover all three states |
| Provide a complete public workflow | Open, review, lookup, wallet connection, and full demo are available | `https://agenda-echo.pages.dev/` |
| Prove the deployed artifact | Source hash matches the finalized StudioNet deployment | `evidence/deployment-verification.json` |
| Prove browser execution | Canonical public site reached `DEMO FINALIZED` | `evidence/browser-run.json` |
