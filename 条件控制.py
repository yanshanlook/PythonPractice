age=int(input("请输入你家狗狗的年龄："))
print("")
if age<=0:
    print("Are you kidding me?")
elif age==1:
    print("相当于14岁的人")
elif age==2:
    print("相当于22岁的人")
elif age>2:
    human=22+(age-2)*5
    print("相当于人类的年龄：",human)

input("点击enter退出")
