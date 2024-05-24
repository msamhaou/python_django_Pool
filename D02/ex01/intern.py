class Intern:
    def __init__(this, Name=None):
        if (Name != None):
            this.Name = Name
        else:
            this.Name = "My name? I’m nobody, an intern, I have no name.";
    
    def __str__(this):
        return this.Name;

    def make_coffee(this):
        return Coffee();

    def work(this):
            raise Exception("I’m just an intern, I can’t do that...");
    pass;

class Coffee:
    def __str__(this):
        return "This is the worst coffee you ever tasted.";
    pass;

if __name__ == "__main__":
    intern = Intern();
    print(intern);
    mark = Intern("Mark")
    print(mark);
    
    mark_coffee = mark.make_coffee();
    print(mark_coffee);
    try:
        intern.work()
    except Exception as e:
        print(e);
        