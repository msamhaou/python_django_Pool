d = [
('Hendrix' , '1942'),
('Allman' , '1946'),
('King' , '1925'),
('Clapton' , '1945'),
('Johnson' , '1911'),
('Berry' , '1926'),
('Vaughan' , '1954'),
('Cooder' , '1947'),
('Page' , '1944'),
('Richards' , '1943'),
('Hammett' , '1962'),
('Cobain' , '1967'),
('Garcia' , '1942'),
('Beck' , '1944'),
('Santana' , '1947'),
('Ramone' , '1948'),
('White' , '1975'),
('Frusciante', '1970'),
('Thompson' , '1949'),
('Burton' , '1939')
]

def my_sort() :
    my_dict = {elem[1] : elem[0] for elem in d};
    my_lst = list(my_dict.keys())
    my_lst.sort()
    sorted_dict = {i : my_dict[i] for i in my_lst};
    return sorted_dict;
    

if __name__ == '__main__' :
    getDic = my_sort();
    {print(elem, ":",getDic[elem]) for elem in getDic}
