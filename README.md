# Agenda Echo

Agenda Echo produces an auditable, item-level redline between a published meeting agenda and the later minutes. Validators classify each promised item as `DECIDED`, `DISCUSSED`, `DEFERRED`, or `OMITTED`, while the contract preserves immutable provenance, exact quotes, source receipts, actors and event order.

## Provenance and audit model

- Evidence must be a raw GitHub URL pinned to a full 40-character commit SHA. Moving branches and generic URLs are rejected.
- The agenda publisher, minutes publisher, repository, commit and file path remain visible in the stored record.
- Validators freeze both complete source bodies with strict equality and recompute each SHA-256 receipt.
- Every finding cites source indexes, a verbatim agenda quote and, unless omitted, a verbatim minutes quote plus an explanation.
- Semantic consensus checks the full source meaning, not merely quote presence or formatting.
- The session contains an append-only audit trail: owner `OPENED`, independent reviewer `REVIEWED`, with sequence numbers, actor wallets and source metadata.
- A finalized session cannot be reviewed again.

The included publishers, evidence files and wallets are operator-controlled demonstration fixtures. They prove the enforced audit boundary, not independent institutional authority.

## Verified Studio Next deployment

| Item | Value |
|---|---|
| Public app | https://agenda-echo.pages.dev/ |
| Network | GenLayer Studio Next, chain `61997` |
| Contract | `0x5D4eCD8920D81DB46Ede83e68775AbB632e8E26E` |
| Deployment tx | `0x360ffc70b017530504dc7bb886df64b9c5605ce393f9b86645a8fc039c470027` |
| Live open tx | `0x7911592ccf5e14d4d91665ff2fa0cb6608e70bbed8d6f1870817ff8411feb5e1` |
| Live review tx | `0x1dfb829b10233ba4f65e80465f0b0277cfdfbe7cf56cfce5256179623b82e2fd` |
| Stored result | `FOLLOWUP`, three quote-bound findings, two ordered audit events |

See `evidence/live-run.json` and `evidence/deployment-verification.json` for the complete stored proof.

## Checks

```text
python -m pytest -q
genvm-lint check contracts/contract.py
python scripts/verify_deployment.py
```
