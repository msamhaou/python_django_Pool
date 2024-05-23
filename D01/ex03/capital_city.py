import sys;

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

def linkDict(state, capital):
    try:
        print(capital[state]);
    except:
            print("Unknown state");
    pass;

if __name__ == '__main__' :
    if (len(sys.argv) != 2) :
        sys.exit(1);
    args = sys.argv;
    linkDict(args[1], capital_cities);
