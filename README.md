# Agenda Echo

> The agenda made a promise. The minutes left a record. Agenda Echo prints the difference.

## The editorial question

A meeting can quietly drop an item without ever saying that it was dropped. Agenda Echo gives every promised topic a line in a public redline. Validators read the agenda and the published minutes, then classify each item as `DECIDED`, `DISCUSSED`, `DEFERRED`, or `OMITTED`. The contract turns that item-level coverage into `COMPLETE`, `FOLLOWUP`, or `INCOMPLETE`.

## Three acts, not one giant form

The public edition behaves like a small newspaper desk:

1. **File the meeting** — name the session and appoint a reviewer.
2. **Pin the promises** — preserve the agenda URL and every promised topic.
3. **Read against the record** — compare the minutes only after the session exists.

The final redline is separate from the filing steps. It keeps the two source digests, citations, parties, item outcomes, and finalized state.

## Filed edition

| Record | Location |
|---|---|
| Public paper | https://agenda-echo.pages.dev/ |
| Source desk | https://github.com/SAMiiNW/agenda-echo |
| StudioNet contract | `0xDe66Ea52ea78e554Af30D69f55DE95582C87D031` |
| Deployment | `FINALIZED / MAJORITY_AGREE / SUCCESS` |
| Browser proof | `FOLLOWUP` with decided, discussed, and deferred items |

The exact public-browser transactions are filed in `evidence/browser-run.json`. The deployed contract source is compared byte-for-byte in `evidence/deployment-verification.json`.

## Press-room checks

```text
python -m pytest -q
genvm-lint check contracts/contract.py
python scripts/verify_deployment.py
```

Demo wallets and the sample meeting records are operator-controlled fixtures. They prove the workflow, not independent institutional authority.
