import sys
sys.path.append('../../')
from yattag import Doc

doc, tag, text = Doc().tagtext()

def nav():
    with tag('nav'):
        with tag('ul'):
            with tag('li'):
                with tag('a', href='/index.html'):
                    text('Home')
            with tag('li'):
                with tag('a', href='/post.html'):
                    text('First post') 
    return doc.getvalue()

if __name__ == '__main__':
    print(nav())