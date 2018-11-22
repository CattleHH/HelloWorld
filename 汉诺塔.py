def hano(n,a,b,c):
    if n==1:
        print(a,"-->",c)
        return None
    # if n==2:
    #     print(a,"-->",b)
    #     print(a,"-->",c)
    #     print(b,"-->",c)
    #     return None
    hano(n-1,a,c,b)
    print(a,"-->",c)
    hano(n-1,b,a,c)

a="A"
b="B"
c="C"

# n=1
# hano(n,a,b,c)

# n=2
# hano(n,a,b,c)

n=3
hano(n,a,b,c)

