from pathlib import Path
HTML=(Path(__file__).parents[1]/'docs'/'index.html').read_text(encoding='utf-8')
def test_complete_browser_workflow():
 for item in ('id="connect"','id="open"','id="review"','id="load"','until:\'finalized\'','get_session','agendaPublisher','minutesPublisher'):assert item in HTML
def test_editorial_redline_identity():
 assert 'class="steps"' in HTML and 'What made the minutes?' in HTML
 assert '<details class="step"' in HTML and 'PROVENANCE + AUDIT RECEIPT' in HTML
