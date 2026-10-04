# Agenda Echo

Agenda Echo turns the gap between a promised meeting agenda and its published minutes into an item-level public receipt. Validators fetch both records, classify every topic as `DECIDED`, `DISCUSSED`, `DEFERRED`, or `OMITTED`, and agree on citations plus content digests. Contract code derives `COMPLETE`, `FOLLOWUP`, or `INCOMPLETE`.

The browser experience is a meeting tape rather than an argument grid: agenda items become a vertical timeline whose labels change only after StudioNet finalization. It supports a connected wallet, manual session creation, separate reviewer action, receipt lookup, and a full two-wallet demo.

## Verified release

- Application: https://agenda-echo.pages.dev/
- Repository: https://github.com/SAMiiNW/agenda-echo
- StudioNet contract: `0xDe66Ea52ea78e554Af30D69f55DE95582C87D031`
- Deployment: `FINALIZED / MAJORITY_AGREE / SUCCESS`
- Public browser run: `FOLLOWUP` with `DECIDED`, `DISCUSSED`, and `DEFERRED` outcomes

The public run used the exact canonical URL and recorded both finalized transaction hashes in `evidence/browser-run.json`.

## Checks

```text
python -m pytest -q
genvm-lint check contracts/contract.py
```

Evidence and demo wallets are operator-controlled fixtures. They demonstrate the workflow, not independent institutional authority.
