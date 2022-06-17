FROM registry.access.redhat.com/ubi8/ubi:latest

LABEL maintainer="Federico Omoto <eomoto@santandertecnologia.com.ar>"
LABEL description="Kotlin v1.5.31 Docker base image"

#ENV http_proxy=http://proxy.ar.bsch:8080
#ENV https_proxy=http://proxy.ar.bsch:8080

# Update the OS
RUN dnf -y update && dnf clean all

# Install useful commands
RUN dnf -y install iputils net-tools bind-utils procps-ng vim less hostname wget bzip2 unzip && dnf clean all

# JDK version
ARG JDK_VERSION=17

# Gradle version
ARG GRADLE_VERSION=7.2

# Install JDK 17
RUN dnf -y install https://download.oracle.com/java/$JDK_VERSION/latest/jdk-${JDK_VERSION}_linux-x64_bin.rpm

# Install gradle
RUN curl -s -O --location -k https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip &> /dev/null
RUN unzip gradle-$GRADLE_VERSION-bin.zip -d /usr/local &> /dev/null
RUN ln -s /usr/local/gradle-$GRADLE_VERSION/bin/gradle /usr/local/bin
RUN rm -f gradle-$GRADLE_VERSION-bin.zip

# Set the app workdir
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
RUN chmod -R g+w /usr/src/app
ENV HOME=/usr/src/app
ENV GRADLE_USER_HOME=$HOME/.gradle

# Install gradle plugins and dependencies
COPY build.gradle.kts .
COPY gradle.properties .
COPY settings.gradle.kts .
RUN gradle assemble --warning-mode all
RUN rm -rf build build.gradle.kts settings.gradle.kts

# Ease extending this base image
ENV http_proxy=http://proxy.ar.bsch:8080
ENV https_proxy=http://proxy.ar.bsch:8080
ENV no_proxy=.ar.bsch
