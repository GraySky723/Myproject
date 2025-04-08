# 使用官方的 Python 镜像作为基础
FROM python:3.10

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到容器内的 `/app` 目录
COPY . .

# 安装 Python 依赖（如果有 requirements.txt）
RUN pip install --no-cache-dir -r requirements.txt

# 运行 Python 程序
CMD ["python", "app.py"]
