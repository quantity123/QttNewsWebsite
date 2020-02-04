# 从仓库拉取 带有 python 3.7 的 Linux 环境
FROM python:3.7
# 设置环境变量
ENV PYTHONUNBUFFERED 1
# 安装 mysql 数据库客户端
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev -y
# 创建 code 文件夹并设置成工作目录
RUN mkdir /QttNewsWebsite
# 将 code 文件夹设置为工作目录
WORKDIR /QttNewsWebsite
# 更新 pip
RUN pip install pip -U
ADD requirements.txt /QttNewsWebsite/
# 安装依赖库
RUN pip install -r requirements.txt
# 将当前目录所有目录和文件都复制到容器的 code 目录
ADD . /QttNewsWebsite/