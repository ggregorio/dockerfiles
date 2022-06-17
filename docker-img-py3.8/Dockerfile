FROM quay-enterprise-quay-quay-enterprise.apps.ocppaz0.ar.bsch/santandertec/santander-tecnologia-docker-base-images-santander-ubi:latest
ENV REQUESTS_CA_BUNDLE=/etc/pki/ca-trust/source/anchors/santander-rootca-0.crt\
    PATH=/app/bin:$PATH\
    PYTHONUNBUFFERED=1
COPY pip.conf /etc/pip.conf
USER root
WORKDIR /app

# Install Git
RUN yum install git -y

# Install Python
RUN dnf install zip -y
RUN dnf install python3.8 -y && pip3 install virtualenv && python3 -m venv /app && chown -R usuario-generico:usuario-generico /app
RUN yum install python38-devel -y

RUN yum update -y

# Install JQ
RUN curl http://nexus.iaas.ar.bsch/repository/linux-yum-repository/jq-linux64 --output jq && \
    chmod +x ./jq && \
    cp -rf jq /usr/bin/

USER usuario-generico
RUN pip install --upgrade pip
