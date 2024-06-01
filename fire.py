
class root:
    def __init__(self, child=None):
        self.levl = 0;
        self.newline = 1;
        self.child = child
        if isinstance(child, root) :
            child.set_level(self.levl + 1)
            child.set_newline();
        pass
    
    def set_newline(self):
        if self.child:
            self.newline = 1;
            if self.child.child :
                self.child.set_newline();
        else:
            self.newline = 0
    def set_level(self,lv):
        self.levl = lv
        if  self.child:
            self.child.set_level(lv +1)
        pass 
    
parent = root()

parent.set_level(10)
print(parent.newline)