# app.py - 主程序
from utils import greet
from calculate import add, subtract,multiply,divide

def main():
    name = input("请输入你的名字: ")
    print(greet(name))

    # 新增计算功能
    num1 = int(input("请输入第一个数字: "))
    num2 = int(input("请输入第二个数字: "))
    print(f"相加后: {add(num1, num2)}")
    print(f"相减后: {subtract(num1, num2)}")
    print(f"相乘后: {multiply(num1,num2)}")
    print(f"相除后: {divide(num1,num2)}")
if __name__ == "__main__":
    main()
