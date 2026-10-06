import ast
from pathlib import Path
S=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text();T=ast.parse(S)
def load(n):
 x=next(v for v in T.body if isinstance(v,ast.FunctionDef) and v.name==n);d={};exec(compile(ast.Module(body=[x],type_ignores=[]),'<c>','exec'),d);return d[n]
def test_session_states():
 f=load('session_state');assert f(['DECIDED','DISCUSSED'])=='COMPLETE';assert f(['DECIDED','DEFERRED'])=='FOLLOWUP';assert f(['DEFERRED','OMITTED'])=='INCOMPLETE'
def test_bound_consensus_and_sources():
 for phrase in ('full commit SHA','strict_eq','prompt_non_comparative','agenda_quote','minutes_quote','audit_events','Source receipt mismatch'):assert phrase in S
def test_surface():
 for n in ('open_session','review_minutes','get_session'):assert f'def {n}' in S
