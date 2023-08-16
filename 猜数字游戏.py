number=7
guess=-1
print("数字猜谜游戏")
while guess!=number:
    guess=int(input("请输入你猜的数字： "))

    if guess ==number:
        print("恭喜你猜对了")
    elif guess<number:
        print("小了")
    elif guess>number:
        print("大了")
        