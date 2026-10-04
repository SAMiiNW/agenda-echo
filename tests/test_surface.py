from pathlib import Path
HTML=(Path(__file__).parents[1]/'docs'/'index.html').read_text()
def test_complete_browser_workflow():
 for item in ('CONNECT WALLET','OPEN SESSION','REVIEW MINUTES','LOAD RECEIPT','RUN FULL DEMO','FINALIZED','get_session'):assert item in HTML
def test_timeline_identity():
 assert 'class="timeline"' in HTML and 'Hear what the minutes missed.' in HTML
