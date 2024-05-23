ft = 42
ft_str = ft.__str__()
qd = "quarante-deux"
lst = [42]
dic = { 42 : 42}
tup = (ft,)
set = {};

print(ft, "est de type <class",type(ft));
print(ft_str, "est de type <class",type(ft_str));
print(qd, "est de type <class",type(qd));
print(ft.__float__(), "est de type <class",type(ft.__float__()));
print((ft == ft), "est de type <class",type(ft == ft));
print((lst), "est de type <class",type(lst));
print(dic, "est de type <class",type(dic));
print(tup, "est de type <class",type(tup));
print(set, "est de type <class",type(set));
