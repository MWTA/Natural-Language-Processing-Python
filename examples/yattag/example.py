'''
    http://www.yattag.org/
'''
from yattag import Doc

arq = open('examples/yattag/report.html', 'w')

doc, tag, text = Doc().tagtext()

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('body'):
        text('Hello world!')

print(doc.getvalue())

arq.write(doc.getvalue())
arq.close()
