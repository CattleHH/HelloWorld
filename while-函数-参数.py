# benqian=100000
# years=0
# while benqian<200000:
#     benqian=benqian*(1+0.067)
#     years+=1
#     print("第{0}年拿了{1}块钱".format(years,benqian))


# benqian=100000
# years=0
# while benqian<200000:
#     benqian=benqian*(1+0.067)
#     years+=1
#     print("第{0}年拿了{1}块钱".format(years,benqian))
# else:
#     print("翻倍了")

# def hello(person):
# #     print("函数自己的语句，参数值是{0}".format(person))
# #     return "return的值，参数是{0}".format(person)
# #
# # p='明月'
# # # hello(p)
# # str=hello(p)
# # print(str)


# def printLine(row):
#     for col in range(1,row+1):
#         sum=row*col
#         # print("{0}*{1}={2}".format(col,row,sum),end='  ')
#         print(row*col,end=' ')
#     print("")
#
# for row in range(1,10):
#     printLine(row)


# def reg(name,age,gender='male'):
#     if gender=='male':
#         print("{0} is {1}岁，他是个好学生".format(name,age))
#     else:
#         print("{0} is {1}岁，她是个好学生".format(name, age))
# reg('jingjing',19)
# reg('jingjing',18,'female')


# def stu( *args):
#      print("大家好：")
#      print(type(args))
#      for item in args:
#          print(item)
# stu("zhangsan",18,"dizhi","xxx")
# stu("zhoudashen")


# def stu(**kargs):
#     print("dajiahao")
#     print(type(kargs))
#     for k,v in kargs.items():
#         print(k,"--",v)
#     print("*"*20)
# stu(name="wangxiaojing",age=18,addr="beijing",work="teacher")
# stu(name="zhoudashen")
# stu()

# def stu(name,age,*args,hobby="没有",**kargs):
#     print("大家好：")
#     print("我叫{0}，我今年{1}岁了".format(name,age))
#     if hobby=="没有":
#         print("我没有爱好")
#     else:
#         print("我的爱好是{0}".format(hobby))
#     print("*"*20)
#     for i in args:
#         print(i)
#     print("&"*20)
#     for k,v in kargs.items():
#         print(k,'--',v)
# name="liuying"
# age=19
# # stu(name,age)
# # stu(name,age,hobby="游泳")
# stu(name,age,"王晓静","刘石头",hobby="游泳",hobby2="烹饪",hobby3="做作业")


help(print )













