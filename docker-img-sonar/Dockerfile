FROM sonarsource/sonar-scanner-cli:latest

ENV http_proxy "http://proxy.ar.bsch:8080"
ENV https_proxy "http://proxy.ar.bsch:8080"
ENV no_proxy ".ar.bsch"
ENV HTTP_PROXY "http://proxy.ar.bsch:8080"
ENV HTTPS_PROXY "http://proxy.ar.bsch:8080"
ENV NO_PROXY ".ar.bsch,gitlab,docker,archive.apache.org"


COPY ./cert/sonarOCP.cer /opt/java/openjdk/lib/security/sonarOCP.cer
COPY ./cert/sonarOCPIntermedio.cer /opt/java/openjdk/lib/security/sonarOCPIntermedio.cer

RUN keytool -import -keystore /opt/java/openjdk/lib/security/cacerts -storepass changeit -noprompt -alias sonarOCP -file /opt/java/openjdk/lib/security/sonarOCP.cer
RUN keytool -import -keystore /opt/java/openjdk/lib/security/cacerts -storepass changeit -noprompt -alias sonarOCPIntermedio -file /opt/java/openjdk/lib/security/sonarOCPIntermedio.cer

WORKDIR /opt

ENTRYPOINT ["/bin/echo", "Hello Sonar"]


