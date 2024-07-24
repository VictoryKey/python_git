# 使用官方的 Python 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到容器的 /app 目录
COPY . /app

# 安装 Flask
RUN pip install --no-cache-dir flask

# 安装其他依赖（如果有）
# RUN pip install -r requirements.txt

# 暴露容器的端口（Flask 默认端口是 5000）
EXPOSE 5000

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# 运行 Flask 应用
CMD ["flask", "run", "--host=0.0.0.0"]
