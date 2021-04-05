FROM centos:latest
RUN yum install git -y
RUN yum install python36 -y
RUN pip3 install flask
RUN pip3 install keras
RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow==2.4.1
RUN git clone https://github.com/visheshgargavi/Arth_deeplearning.git

RUN mv /Arth_deeplearning/jenkins_deep_learning/*  .

ENTRYPOINT ["flask" , "run","--host=0.0.0.0","--port=81"]

EXPOSE 81/tcp

RUN yum clean all
