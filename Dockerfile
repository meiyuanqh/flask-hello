from python:2.7-slim
MAINTAINER meiyuanqh <meiyuanqh@163.com>

ADD app.py app.py
ADD run.sh /run.sh
RUN chmod +x /run.sh
RUN apt-get update -y && apt-get install -y wget && wget https://bootstrap.pypa.io/ez_setup.py -O - | python && easy_install flask
EXPOSE 80
WORKDIR .
CMD ["/run.sh"]
