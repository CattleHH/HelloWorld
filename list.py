# a = [1,2,3]
# e = ['a','d','g']
# f = a+e
# print(f)
# b = a*3
# print(b)
# c = 5
# d = c in a
# print(d)
# d = c not in a
# print(d)

# a = [1,2,3]
# for i in a:
#     print(i)
#
# c = ["i love wangxiaojing"]
# for i in c:
#     print(i)
#
# print(len(a))

a={1,2,3}
c={4,5,6}
#
# s={e*f for e in a for f in c}
# print(s)

for e in a:
    for f in c:
        print(e*f,end=" ")