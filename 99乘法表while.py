b=1
c=1
while  c<=9:
    j=b*c
    print("{0}*{1}={2}".format(b,c,j),end='   ')
    c+=1
    if c==9:
        j=b*c
        print("{0}*{1}={2}".format(b, c, j))
        b+=1
        c=b


