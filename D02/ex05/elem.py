#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.
    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """

    class ValidationError(Exception):
        pass
    
    
    
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.content = content if isinstance(content, list) else ([content] if content is not None else [])
        self.tag_type = tag_type
        self.lvl = 0
        for c in self.content:
            if not self.check_type(c):
                raise self.ValidationError
        if self.content:
            self.set_level(self.lvl)

    def set_level(self, lvl):
            self.lvl += 1
            for c in self.content:
                if (isinstance(c, Elem) and c.content):
                    c.set_level(c.lvl)
            pass
    
    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        result = ''
        result = "<%s%s>" % (self.tag, self.__make_attr())
        if self.tag_type == 'double':
            result += "%s</%s>" % (self.__make_content(), self.tag)
        elif self.tag_type == 'simple':
            result = "<%s%s />" % (self.tag, self.__make_attr())
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        if not self.content:
            return ''
        result = ''
        if not self.content[0].__str__() == '':
            result = '\n'
        for elem in self.content:
            if (isinstance(elem, Text) and elem.__str__() == ''):
                result += ''
            else:
                tab = 0
                if isinstance(elem, Elem) and elem.tag_type == 'simple':
                    tab = 1
                result += "%s%s\n%s" % ((self.lvl - tab) * '  ' ,str(elem), (self.lvl - 1) * '  ');
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content.extend([elem for elem in content if elem != Text('')])
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or an Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))
