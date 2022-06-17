FROM ibmcom/websphere-traditional:8.5.5.17-ubi8

ENV http_proxy "http://proxy.ar.bsch:8080"
ENV https_proxy "http://proxy.ar.bsch:8080"
ENV no_proxy ".ar.bsch"
ENV HTTP_PROXY "http://proxy.ar.bsch:8080"
ENV HTTPS_PROXY "http://proxy.ar.bsch:8080"
ENV NO_PROXY ".ar.bsch,gitlab,docker,archive.apache.org"

#Change user to install ant
USER root

#RUN mkdir /tmp

RUN yum update -y
RUN yum install -y curl
RUN yum install -y wget
RUN yum install -y tar

RUN curl --insecure http://nexus.iaas.ar.bsch/repository/DevOps-repository/java/jdk-6u45-linux-x64.bin --output jdk-6u45-linux-x64.bin

RUN ls -la

RUN sh ./jdk-6u45-linux-x64.bin

RUN curl --insecure -q http://nexus.iaas.ar.bsch/repository/linux-yum-repository/libnsl-2.28-101.el8.x86_64.rpm --output libnsl-2.28-101.el8.x86_64.rpm
##RUN wget --no-check-certificate https://rpmfind.net/linux/centos/8.2.2004/BaseOS/x86_64/os/Packages/libnsl-2.28-101.el8.x86_64.rpm

RUN yum install -y libnsl-2.28-101.el8.x86_64.rpm --nobest --skip-broken

### Install Scripts de Python para WAS

ADD /was/check_app_running.py /was/scripts/check_app_running.py
ADD /was/reset-ibm-was.py /was/scripts/reset-ibm-was.py
ADD /was/sync-was.py  /was/scripts/sync-was.py
ADD /was/update-was.py /was/scripts/update-was.py
ADD /was/check_app_running_nocluster.py /was/scripts/check_app_running_nocluster.py

# Install Ant
#ENV ANT_VERSION 1.10.9
#RUN wget -q https://downloads.apache.org/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz
#RUN tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz 
#RUN mv apache-ant-${ANT_VERSION} /opt/ant 
#RUN rm apache-ant-${ANT_VERSION}-bin.tar.gz

#RUN curl --insecure http://nexus.iaas.ar.bsch/repository/obcm-repository/obcm/ant-contrib/1.0b3/ant-contrib-1.0b3.jar -o ant-contrib-1.0b3.jar
#RUN mv ant-contrib-1.0b3.jar /opt/ant/lib

RUN pwd
RUN ls /jdk1.6.0_45/bin

# Install JQ
RUN curl --insecure http://nexus.iaas.ar.bsch/repository/linux-yum-repository/jq-linux64 --output jq
RUN chmod +x ./jq
RUN cp -rf jq /usr/bin/

#ENV JAVA_HOME /opt/IBM/WebSphere/AppServer/java/
ENV JAVA_HOME /jdk1.6.0_45
ENV PATH ${JAVA_HOME}/bin:$PATH
# Setting ANT_HOME
ENV ANT_HOME /opt/ant
ENV PATH ${ANT_HOME}/bin:$PATH  

### Install Scripts de Python para WAS
ADD /was/check_app_running.py /was/scripts/check_app_running.py
ADD /was/reset-ibm-was.py /was/scripts/reset-ibm-was.py
ADD /was/sync-was.py  /was/scripts/sync-was.py
ADD /was/update-was.py /was/scripts/update-was.py
ADD /was/check_app_running_nocluster.py /was/scripts/check_app_running_nocluster.py

# Install Maven
#ENV MVN_VERSION 3.2.5
#RUN wget -q https://archive.apache.org/dist/maven/maven-3/3.2.5/binaries/apache-maven-${MVN_VERSION}-bin.zip
#RUN unzip apache-maven-${MVN_VERSION}-bin.zip
#RUN mv apache-maven-${MVN_VERSION} /opt/
#RUN rm apache-maven-${MVN_VERSION}-bin.zip
#ENV MAVEN_HOME /opt/apache-maven-${MVN_VERSION}
#ENV M2_HOME /opt/apache-maven-${MVN_VERSION}
#ENV PATH ${M2_HOME}/bin:$PATH
ADD settings2.xml /settings.xml

## Install nexus cert
#ADD nexus-cert.crt /
#RUN /opt/IBM/WebSphere/AppServer/java/bin/keytool -import -trustcacerts -keystore /opt/IBM/WebSphere/AppServer/java/jre/lib/security/cacerts -storepass changeit -noprompt -alias nexust-cert -file /nexus-cert.crt
#RUN /jdk1.6.0_45/jre/bin/keytool -import -trustcacerts -keystore /jdk1.6.0_45/jre/lib/security/cacerts -storepass changeit -noprompt -alias nexust-cert -file /nexus-cert.crt
