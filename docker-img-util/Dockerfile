FROM mcr.microsoft.com/powershell

ENV http_proxy "http://proxy.ar.bsch:8080"
ENV https_proxy "http://proxy.ar.bsch:8080"
ENV no_proxy ".ar.bsch"

# update 
RUN apt-get update

# install utilities
RUN apt-get install -y git \
  && apt-get install -y wget \
  && apt-get install -y curl\
  && apt-get install -y python3 \
  && apt-get install -y python3-pip \
  && apt-get install -y jq \
  && apt-get install -y mysql-client \
  && apt-get install -y postgresql-client
