FROM quay-enterprise-quay-quay-enterprise.apps.ocppaz0.ar.bsch/santandertec/santander-tecnologia-docker-base-images-santander-ubi:latest

ENV FLYWAY_VERSION=8.3.0

USER root

RUN dnf update -y --exclude=shadow* && \
    INSTALL_PKGS="openssl wget java-1.8.0-openjdk" && \
    dnf remove -y $INSTALL_PKGS && \
    dnf install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    dnf -y clean all && \
    rm -rf /var/cache/dnf/*

RUN useradd -s "/bin/bash" -d "/flyway" flyway

WORKDIR /flyway

USER flyway

RUN wget https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}.tar.gz && \
    tar -xzf flyway-commandline-${FLYWAY_VERSION}.tar.gz && \
    mv flyway-${FLYWAY_VERSION}/* . && \
    rm flyway-commandline-${FLYWAY_VERSION}.tar.gz
