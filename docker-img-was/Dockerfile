FROM ibmcom/websphere-traditional:9.0.5.1
#FROM ibmcom/websphere-traditional:9.0.5.2-ubi7


ENV http_proxy "http://proxy.ar.bsch:8080"
ENV https_proxy "http://proxy.ar.bsch:8080"
ENV no_proxy ".ar.bsch"
ENV HTTP_PROXY "http://proxy.ar.bsch:8080"
ENV HTTPS_PROXY "http://proxy.ar.bsch:8080"
ENV NO_PROXY ".ar.bsch,gitlab,docker,archive.apache.org"

###Change user to install ant
USER root

RUN apt-get update -y
RUN apt-get install -y curl
RUN apt-get install -y wget
RUN apt-get install -y tar
RUN apt-get install -y dnsutils

#RUN yum update -y
#RUN yum install -y curl
#RUN yum install -y wget
#RUN yum install -y tar


### Install Scripts de Python para WAS

ADD /was/check_app_running.py /was/scripts/check_app_running.py
ADD /was/reset-ibm-was.py /was/scripts/reset-ibm-was.py
ADD /was/sync-was.py  /was/scripts/sync-was.py
ADD /was/update-was.py /was/scripts/update-was.py
ADD /was/check_app_running_nocluster.py /was/scripts/check_app_running_nocluster.py

RUN chmod 775 -R /was

#### Install cert
COPY nexus_certificate.pem usr/share/ca-certificates/extra
COPY nexus_ocp.pem  usr/share/ca-certificates/extra

RUN dpkg-reconfigure ca-certificates
RUN update-ca-certificates

#COPY /was/etc/trust.p12 /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/etc/
#COPY /was/etc/key.p12 /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/etc/
#COPY /was/etc/serverCert.arm /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/etc/
#COPY /was/etc/clientCert.arm /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/etc/
#COPY /was/etc/IBMLSDActiveServerList.asl /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/etc/
#COPY /was/etc/DummyServerTrustFile.jks /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/etc/
#COPY /was/etc/DummyServerKeyFile.jks /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/etc/
#COPY /was/etc/DummyClientTrustFile.jks /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/etc/
#COPY /was/etc/DummyClientKeyFile.jks /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/etc/

### Install Ant
#ENV ANT_VERSION 1.10.7
#RUN wget -q https://downloads.apache.org/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz
#RUN tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz 
#RUN mv apache-ant-${ANT_VERSION} /opt/ant 
#RUN rm apache-ant-${ANT_VERSION}-bin.tar.gz

### Setting JAVA_HOME
#ENV JAVA_HOME /opt/IBM/WebSphere/AppServer/java/8.0/jre
#ENV PATH ${JAVA_HOME}/bin:$PATH
# Setting ANT_HOME
#ENV ANT_HOME /opt/ant
#ENV PATH ${ANT_HOME}/bin:$PATH  
