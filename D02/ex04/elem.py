class Text(str):
    def __init__(self, txt=""):
        self.txt = txt;
        self.proc();
    def __str__(self):
        return self.txt;
    def proc(self):
        element = "\n<br />\n";
        self.txt = element.join(self.txt.split('\n'));
    def isEmpty(self):
        return self.txt == '';

level = 0;
class Elem(object):
    def __init__(self, tag="div", attr={}, content=None, tag_type="double"):
        self.lvl = 0;
        self.tag = tag;
        self.newline = 0;
        self.tag_type = tag_type;
        self.setup(content);
        if isinstance(self.content[0], Elem):
            self.set_level(self.lvl + 1);
        # if isinstance(self.content[0], (Elem, Text)):
        #     self.isInline(self.content[0])
        
            
    def isInline(self, content):
        if content:
            self.newline = 1;
            if isinstance(content, Elem) and content.content:
                self.content.isInline()

        

    def setup(self, content):
        if not isinstance(content, (None.__class__, list, Elem, Text)):
            raise Exception("Err");
        if isinstance(content, list):
            for c in content:
                if not (isinstance(c, (Elem, Text))) : raise Exception("Err");
            self.content = content;
        else:
            self.content = [content];
    
    def set_level(self, lvl):
        for elem in self.content:
            elem.lvl = lvl;
            if elem.content and isinstance(elem.content[0], Elem):
                elem.set_level(elem.lvl + 1)
        pass;
    
    def open_tag(self):
        str = "%s<%s>%s" % ((self.lvl) * "  ", self.tag, self.newline * '\n');
        return str

    def generate_content(self):
        str = ""
        for elem in self.content:
            if elem:
                if isinstance(elem , Text):
                    str += "%s%s\n" % ((self.lvl + 1 ) * "  ", elem);
                else:
                    str += elem.__str__();
        return str;
        
    def __str__(self):
        str = "";
        str += self.open_tag()
        str += self.generate_content()
        str += "%s</%s>%s" % (self.newline * self.lvl * "  ", self.tag, int(0 if self.lvl == 0 else 1) * '\n')
        return str;

print(str(Elem(content=[Text('foo'), Text('bar'), Elem()])) )
