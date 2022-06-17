FROM quay-enterprise-quay-quay-enterprise.apps.ocppaz0.ar.bsch/santandertec/santander-tecnologia-docker-base-images-java-openjdk-base:v1.8.0

ARG MAVEN_VERSION=3.8.3
ARG USER_HOME_DIR="/home/openjdk"
ARG BASE_URL=https://downloads.apache.org/maven/maven-3/${MAVEN_VERSION}/binaries/

USER root

RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && dnf update -y --exclude=shadow* \
  && dnf install wget -y \
  && wget --no-check-certificate -P /tmp/ ${BASE_URL}/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
  && tar -xzf /tmp/apache-maven-${MAVEN_VERSION}-bin.tar.gz -C /usr/share/maven --strip-components=1 \
  && rm -f /tmp/apache-maven-${MAVEN_VERSION}-bin.tar.gz\
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

RUN dnf install -y glibc-all-langpacks langpacks-en

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"


RUN curl http://nexus.iaas.ar.bsch/repository/linux-yum-repository/jq-linux64 --output jq
RUN chmod +x ./jq
RUN cp -rf jq /usr/bin/

COPY mvn-entrypoint.sh /usr/local/bin/mvn-entrypoint.sh
COPY settings.xml /usr/share/maven/ref/

ENTRYPOINT ["/usr/local/bin/mvn-entrypoint.sh"]
CMD ["mvn"]

USER 1002





