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
    def __init__(self, tag="div", attr={}, content=None, type="double"):
        print(self.__class__, id(self))
        self.lvl = 0;
        self.setup(content);

    def setup(self, content):
        if not isinstance(content, (None.__class__, list, Elem, Text)):
            raise Exception("Err");
        if isinstance(content, list):
            for c in content:
                if not (isinstance(c, (Elem, Text))) : raise Exception("Err");
            self.content = content;
        else:
            self.content = [content];
    
    def __str__(self):
        self.set_levels(0);
        return "";
    
    def set_levels(self, lvl):
        print("call")
        global level;
        for cc in self.content:
            if isinstance(cc, Elem):
                level += 1
                cc.lvl = level
            if cc and isinstance(cc.content[0], Elem):
                cc.content[0].set_levels(cc.lvl);
            
        pass;

obj = Elem(content=Elem(content=Elem(content=Elem(content=Elem(content=Elem())))));
str = obj.__str__();
print(obj.lvl)
print(level)

