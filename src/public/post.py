import sys
sys.path.append('../')
from ruff.convert import to_html
from public.block.nav import nav
from yattag import Doc

doc, tag, text = Doc().tagtext()

with tag('html'):
    with tag('body'):
        doc.asis(nav())
        with tag('article'):
            with tag('header'):
                with tag('h2'):
                    text('First post')
            with tag('section'):
                with tag('p'):
                    text('''
                    Lorem ipsum dolor sit amet, ius ad fierent suscipit percipit, 
                    euismod legimus appellantur ad duo. Vim agam quidam denique at. 
                    Mea oratio ancillae an. Animal tractatos complectitur ex duo.
                    ''')

if __name__ == '__main__':
    with open(to_html(__file__), 'w') as file:
        file.write(doc.getvalue())
