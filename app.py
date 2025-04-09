# app.py - 主程序
from utils import greet
from calculate import add, subtract

def main():
    name = input("请输入你的名字: ")
    print(greet(name))

    # 新增计算功能
    num1 = int(input("请输入第一个数字: "))
    num2 = int(input("请输入第二个数字: "))

    print(f"加法结果: {add(num1, num2)}")
    print(f"减法结果: {subtract(num1, num2)}")

if __name__ == "__main__":
    main()
