import json, re, time
from dataclasses import replace
from pathlib import Path
from genlayer_py import create_account, create_client
from genlayer_py.chains import studio_devnet

ROOT = Path(__file__).parents[1]; env = (ROOT.parents[3] / "accounts.env").read_text(); deployment = json.loads((ROOT / "deployment.json").read_text())
contract, commit = deployment["contractAddress"], deployment["sourceCommit"]
chain = replace(studio_devnet, name="GenLayer Studio Next", rpc_urls={"default": {"http": ["https://studio-next.genlayer.com/api"]}})
def account(number): return create_account(account_private_key=re.search(rf'^ACCOUNT_{number}_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)', env, re.M).group(1).strip())
def client(number): return create_client(chain=chain, account=account(number))
def write(number, label, function, args, intelligent=False):
    c = client(number); fees = c.estimate_transaction_fees({"leader_timeunits_allocation":500 if intelligent else 180,"validator_timeunits_allocation":650 if intelligent else 360})
    tx = c.write_contract(address=contract, function_name=function, args=args, fees=fees); print(label + "_tx=" + str(tx), flush=True)
    c.wait_for_transaction_receipt(transaction_hash=tx, wait_until="finalized", retries=300, interval=3000, full_transaction=True); return str(tx)
base = f"https://raw.githubusercontent.com/SAMiiNW/agenda-echo/{commit}/docs/evidence/"
agenda, minutes = base + "agenda.md", base + "minutes.md"; session_id = "HARBOR-AUDIT-" + str(int(time.time()))
items = ["Approve extended winter desk hours.", "Review the accessible entrance signage replacement.", "Decide whether to add a Saturday help shift."]
transactions = {"open":write(1,"OPEN","open_session",[session_id,account(2).address,"Harbor access committee","Harbor Public Records demo publisher",agenda,items]),"review":write(2,"REVIEW","review_minutes",[session_id,"Harbor Clerk Minutes demo publisher",minutes],True)}
state = client(1).read_contract(address=contract,function_name="get_session",args=[session_id])
if state["state"] != "FOLLOWUP" or len(state["findings"]) != 3 or [x["action"] for x in state["audit_events"]] != ["OPENED","REVIEWED"]: raise RuntimeError("unexpected stored state: " + json.dumps(state))
proof = {"sessionId":session_id,"transactions":transactions,"state":state,"fixtureDisclosure":"Publishers, evidence files and wallets are operator-controlled fixtures. Pinned commits, receipts, roles and audit order are enforced by the contract."}
(ROOT / "evidence" / "live-run.json").write_text(json.dumps(proof,indent=2) + "\n"); print(json.dumps(proof,indent=2),flush=True)
