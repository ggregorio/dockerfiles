FROM registry.redhat.io/rhel8/python-38

ENV HTTP_PROXY "http://proxy.ar.bsch:8080"
ENV HTTPS_PROXY "http://proxy.ar.bsch:8080"
ENV NO_PROXY "localhost,.ar.bsch"

USER root
RUN yum -y update && yum -y install openssl && yum -y install ca-certificates

USER 1001

RUN pip install --upgrade pip

