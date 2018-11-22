# d={"one":1,"two":2,"three":3}
# print(d["one"])
# for k in d.keys():
#     print(k,d[k])
# for v in d.values():
#     print(v)


# d={"one":1,"two":2,"three":3}
# dd={k:v for k,v in d.items() if v%2==0}
# print(dd)
# i=d.items()
# print(type(i))
# print(i)

d={"one":1,"two":2,"three":3}
dd={k:v for k,v in d.items() if v%2==0}
print(dd)
i=d.values()
print(type(i))
print(i)
l=["一","二","三"]
f=d.fromkeys(l,"hhhh")
print(f)
