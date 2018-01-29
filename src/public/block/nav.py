import sys
sys.path.append('../../')
from yattag import Doc

doc, tag, text = Doc().tagtext()

def nav():
    with tag('nav'):
        with tag('ul'):
            with tag('li'):
                text('first')
            with tag('li'):
                text('second')          
            with tag('li'):
                text('third')
    return doc.getvalue()

if __name__ == '__main__':
    print(nav())