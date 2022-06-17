FROM quay-enterprise-quay-quay-enterprise.apps.ocppaz0.ar.bsch/santandertec/santander-tecnologia-docker-base-images-python-base:v3.8

USER root

RUN sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
RUN sudo dnf upgrade


RUN yum -y install zbar-devel
RUN yum -y install yum install java-1.8.0-openjdk-devel
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-devel/

RUN java -version

RUN mkdir -p /home/app/images

RUN chgrp -R 0 /home/app && \
    chmod -R g=u /home/app

WORKDIR /home/app

RUN pip install --upgrade pip
RUN pip3 --default-timeout=2000 install -r requirements.txt

RUN chmod +x /home/app/entrypoint.sh
RUN chmod 755 /home/app/entrypoint.sh

USER default

ENTRYPOINT ["/bin/bash"]
