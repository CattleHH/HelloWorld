for i in range(1,10):
    for m in range(1,i+1):
        sum=m*i
        # print("i={0}".format(i), end='  ')
        if m<i:
            print("{0}*{1}={2}".format(m,i,sum),end='  ')
            # print("i={0}".format(i),end='  ')
            # print("m={0}".format(m))
        else:
            print("{0}*{1}={2}".format(m, i, sum))