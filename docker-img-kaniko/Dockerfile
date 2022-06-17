FROM gitlab.ar.bsch:4567/santander-tecnologia/docker-base-images/other/kaniko:v2

# Variables de proxy
ENV http_proxy "http://proxy.ar.bsch:8080"
ENV https_proxy "http://proxy.ar.bsch:8080"
ENV no_proxy ".ar.bsch"
ENV HTTP_PROXY "http://proxy.ar.bsch:8080"
ENV HTTPS_PROXY "http://proxy.ar.bsch:8080"
ENV NO_PROXY ".ar.bsch"

WORKDIR /bin

ADD curl-amd64 curl

# RUN chmod u+x /bin/curl

# RUN export PATH=$PATH:/bin/curl
