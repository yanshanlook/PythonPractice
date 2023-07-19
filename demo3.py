try:
    a = int(input("请输入第一个整数： "))
    b = int(input("请输入第二个整数： "))
    result = a / b
except ZeroDivisionError:
    print("不能为0")
except BaseException as e:
    print("产生了错误："+e)
else:
    print("结果为",result)
finally:
    print("无论是否产生异常，都执行的代码")

print("程序结束")