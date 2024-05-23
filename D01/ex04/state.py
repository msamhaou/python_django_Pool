import sys;

def get_key_form_value(value, dict) :
    i=0
    for key, val in dict.items():
        if val == value : return key
        i += 1
    pass

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
    value = get_key_form_value(sys.argv[1], capital_cities);
    if not value :
        print('Unknown capital city');
        exit(0);
    print(get_key_form_value(value, states));

        