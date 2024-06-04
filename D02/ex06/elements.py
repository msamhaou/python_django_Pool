from elem import Elem, Text
import sys

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', attr=attr, content=content)

class Head(Elem):
    def __init__(slef, content=None, attr={}):
        super().__init__(tag='head',content=content, attr=attr)


class Body(Elem):
    def __init__(slef, content=None, attr={}):
        super().__init__(tag='body',content=content, attr=attr)
        
class Title(Elem):
    def __init__(slef, content=None, attr={}):
        super().__init__(tag='title',content=content, attr=attr)
        
class Meta(Elem):
    def __init__(slef, attr={}):
        super().__init__(tag='meta', attr=attr, tag_type='simple')

class Img(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='img', attr = attr, tag_type = 'simple')

class Table(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='table', attr = attr, content=content)

class Th(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='th', attr=attr, content=content)

class Tr(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='tr', attr=attr, content=content)
        
class Td(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='td', attr=attr, content=content)
        
class Ul(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='ul', attr=attr, content=content)
        
class Ol(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='ol', attr=attr, content=content)
        
class Li(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='li', attr=attr, content=content)

class H1(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='h1', attr=attr, content=content)

class H2(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='h2', attr=attr, content=content)
        
class P(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='p', attr=attr, content=content)

class Div(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='div', attr=attr, content=content)
        
class Span(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='span', attr=attr, content=content)
    
class Hr(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='hr', attr=attr, content=content)
        
class Br(Elem):
    def __init__(self, attr={}, content=None):
        super().__init__(tag='br', attr=attr, content=content)
        
if __name__ == '__main__':
    file = open('index.html', 'w');
    file.write( str(Html( [Head(content=Title(content=Text('Hello'))), Body(content=[H1(content=Text('"Oh no, not again!"')), Img(attr={'src':"https://www.w3schools.com/images/w3schools_green.jpg"})])] ) ) )
