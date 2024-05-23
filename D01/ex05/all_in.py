import sys;

def linkDict(state, capital):
    try:
        print(capital[state]);
    except:
         print("Unknown state");
    pass;

def get_key_form_value(value, dict) :
    for key, val in dict.items():
        if val.lower() == value.lower() : return key
    pass;

def get_state(lowkey, dic) :
    for key, val in dic.items():
        if key.lower() == lowkey : return key;
    pass;
       

if __name__ == '__main__':
    if (len(sys.argv) != 2) :
        sys.exit(1)
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
    args = sys.argv[1].split(',');
    for arg in args :
        arg = arg.strip();
        if (not arg):
            continue;
        state_abv = get_key_form_value(arg, capital_cities);
        state = get_state(arg.lower(), states);
        if(state):
            print(state, "is the capital of", capital_cities[states[state]]);
        elif (state_abv):
            print(get_key_form_value(state_abv, states), "is the capital of", capital_cities[state_abv]);
        else:
            print(arg, "is neither a capital city nor a state")
        
    
    
    

        