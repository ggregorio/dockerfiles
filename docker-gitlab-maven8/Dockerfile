FROM registry.redhat.io/openjdk/openjdk-8-rhel8

ENV http_proxy "http://proxy.ar.bsch:8080"
ENV https_proxy "http://proxy.ar.bsch:8080"
ENV no_proxy ".ar.bsch"
ENV HTTP_PROXY "http://proxy.ar.bsch:8080"
ENV HTTPS_PROXY "http://proxy.ar.bsch:8080"
ENV NO_PROXY ".ar.bsch"

#RUN apt-get install -y openssh-client
ADD settings2.xml /usr/share/maven/ref/settings.xml


USER root

#COPY nexus_certificate.pem /usr/share/pki/ca-trust-source/anchors/
#COPY nexus_ocp.pem  /usr/share/pki/ca-trust-source/anchors/
#RUN update-ca-trust

COPY santander-rootca.crt  /etc/pki/ca-trust/source/anchors/
COPY santander-rootca1.crt  /etc/pki/ca-trust/source/anchors/
RUN update-ca-trust extract

USER 1001



