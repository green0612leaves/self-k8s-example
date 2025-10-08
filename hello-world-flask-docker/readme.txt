docker pull zhangrui20200722/hello-world-flask:v1

#--------
# 打 tag 并指定标签名（如 v1）
#docker tag hello-world-flask zhangrui20200722/hello-world-flask:v1

docker build -t hello-world-flask:v2 .

docker tag hello-world-flask:v2 zhangrui20200722/hello-world-flask:v2

# 推送指定标签的镜像
docker push zhangrui20200722/hello-world-flask:v2


docker run -d -p 8000:5000 --name my-flask-app zhangrui20200722/hello-world-flask:v2

#---------

docker login -u zhangrui20200722
#  密码：  Zr@hh81yyyh0504

# zhangrui20200722/hello-world-flask   那么镜像将会被推送到一个新的仓库
