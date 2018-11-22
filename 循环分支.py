# gender=input("请输入你的性别：")
# print("你输入的性别是：{0}".format(gender))
# if gender=="男":
#     print("请敲代码")
# else:
#     print("节日快乐")
# print("好了开始上课")


# for name in ['zhangsan','lisi','wangwu','jingjing']:
#     print(name)
#     if name=='jingjing':
#         print("我最爱的{0}出现了".format(name))
#     else:
#         print('同学我们不约')


# for i in range(1,11):
#     if i==7:
#         print('我找到了')
#         break
#     else:
#         print(i)


for i in range(1,11):
    if i%2==1:
        continue
    print("{0}是偶数".format(i))

    