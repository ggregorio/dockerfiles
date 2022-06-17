FROM ibmcom/websphere-traditional:8.5.5.17-ubi8

ENV http_proxy "http://proxy.ar.bsch:8080"
ENV https_proxy "http://proxy.ar.bsch:8080"
ENV no_proxy ".ar.bsch"
ENV HTTP_PROXY "http://proxy.ar.bsch:8080"
ENV HTTPS_PROXY "http://proxy.ar.bsch:8080"
ENV NO_PROXY ".ar.bsch,gitlab,docker,archive.apache.org"

USER root

RUN INSTALL_PKGS="wget curl tar" && \
    dnf install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \
    dnf clean all -y && \
    rm -rf /var/cache/dnf/*

RUN curl http://nexus.iaas.ar.bsch/repository/DevOps-repository/java/jdk-6u45-linux-x64.bin --output jdk-6u45-linux-x64.bin && \
    curl -q http://nexus.iaas.ar.bsch/repository/linux-yum-repository/libnsl-2.28-101.el8.x86_64.rpm --output libnsl-2.28-101.el8.x86_64.rpm && \
    sh ./jdk-6u45-linux-x64.bin && \
    dnf install -y libnsl-2.28-101.el8.x86_64.rpm

# Scripts Python para WAS
ADD /was/check_app_running.py /was/scripts/check_app_running.py
ADD /was/reset-ibm-was.py /was/scripts/reset-ibm-was.py
ADD /was/sync-was.py  /was/scripts/sync-was.py
ADD /was/update-was.py /was/scripts/update-was.py
ADD /was/check_app_running_nocluster.py /was/scripts/check_app_running_nocluster.py
ADD /was/check_app_running_threads.py /was/scripts/check_app_running_threads.py

# Install Ant
ENV ANT_VERSION 1.9.16
RUN wget -q https://downloads.apache.org/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz && \
    tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \
    mv apache-ant-${ANT_VERSION} /opt/ant && \
    rm apache-ant-${ANT_VERSION}-bin.tar.gz && \
    curl http://nexus.iaas.ar.bsch/repository/obcm-repository/obcm/ant-contrib/1.0b3/ant-contrib-1.0b3.jar -o ant-contrib-1.0b3.jar && \
    mv ant-contrib-1.0b3.jar /opt/ant/lib

# Install JQ
RUN curl http://nexus.iaas.ar.bsch/repository/linux-yum-repository/jq-linux64 --output jq && \
    chmod +x ./jq && \
    cp -rf jq /usr/bin/

ENV JAVA_HOME /jdk1.6.0_45
ENV PATH ${JAVA_HOME}/bin:$PATH

# Setting ANT_HOME
ENV ANT_HOME /opt/ant
ENV PATH ${ANT_HOME}/bin:$PATH  

# Install Maven
ENV MVN_VERSION 3.2.5
RUN wget -q https://archive.apache.org/dist/maven/maven-3/3.2.5/binaries/apache-maven-${MVN_VERSION}-bin.zip && \
    unzip apache-maven-${MVN_VERSION}-bin.zip && \
    mv apache-maven-${MVN_VERSION} /opt/ && \
    rm apache-maven-${MVN_VERSION}-bin.zip

ENV MAVEN_HOME /opt/apache-maven-${MVN_VERSION}
ENV M2_HOME /opt/apache-maven-${MVN_VERSION}
ENV PATH ${M2_HOME}/bin:$PATH
ADD was/settings.xml /settings.xml

# Install nexus cert
RUN cd / && curl http://nexus.iaas.ar.bsch/repository/DevOps-repository/crt/nexus-cert.crt --output nexus-cert.crt
RUN /opt/IBM/WebSphere/AppServer/java/bin/keytool -import -trustcacerts -keystore /opt/IBM/WebSphere/AppServer/java/jre/lib/security/cacerts -storepass changeit -noprompt -alias nexust-cert -file /nexus-cert.crt
RUN /jdk1.6.0_45/jre/bin/keytool -import -trustcacerts -keystore /jdk1.6.0_45/jre/lib/security/cacerts -storepass changeit -noprompt -alias nexust-cert -file /nexus-cert.crt
