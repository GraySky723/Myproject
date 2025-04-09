# app.py - 主程序
from utils import greet

def main():
    name = input("请输入你的名字: ")
    print(greet(name))

if __name__ == "__main__":
    main()
