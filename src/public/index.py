import sys
sys.path.append('../')
from ruff.convert import to_html
from public.block.nav import nav
from yattag import Doc

doc, tag, text = Doc().tagtext()

with tag('html'):
    with tag('body'):
        doc.asis(nav())
        with tag('h1'):
            text('Hello world!')

with open(to_html(__file__), 'w') as file:
    file.write(doc.getvalue())
