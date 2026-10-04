from pathlib import Path
HTML=(Path(__file__).parents[1]/'docs'/'index.html').read_text()
def test_complete_browser_workflow():
 for item in ('id="connect"','id="open"','id="review"','id="load"','id="demo"','FINALIZED','get_session'):assert item in HTML
def test_editorial_redline_identity():
 assert 'class="steps"' in HTML and 'What made the minutes?' in HTML
 assert '<details class="step"' in HTML and 'FINAL REDLINE' in HTML
