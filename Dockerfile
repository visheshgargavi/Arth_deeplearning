FROM visheshgargavi/tensorflow-keras-flask:v1

RUN yum install git -y

RUN git clone https://github.com/visheshgargavi/Arth_deeplearning.git

RUN mv /Arth_deeplearning/jenkins_deep_learning/*  .

ENTRYPOINT ["python3" , "app.py"]

EXPOSE 81/tcp
