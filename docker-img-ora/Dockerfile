FROM registry.redhat.io/ubi8/ubi

ENV http_proxy "http://proxy.ar.bsch:8080"
ENV https_proxy "http://proxy.ar.bsch:8080"
ENV no_proxy ".ar.bsch"
ENV HTTP_PROXY "http://proxy.ar.bsch:8080"
ENV HTTPS_PROXY "http://proxy.ar.bsch:8080"
ENV NO_PROXY ".ar.bsch"
ENV NLS_LANG=SPANISH_SPAIN.AL32UTF8

RUN yum -y install wget \
  && wget --no-check-certificate https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm \
  && wget --no-check-certificate https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-sqlplus-19.6.0.0.0-1.x86_64.rpm \
  && wget --no-check-certificate https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-tools-19.6.0.0.0-1.x86_64.rpm \
  && yum install -y oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm \
  && yum install -y oracle-instantclient19.6-sqlplus-19.6.0.0.0-1.x86_64.rpm \
  && yum install -y oracle-instantclient19.6-tools-19.6.0.0.0-1.x86_64.rpm \
  && ln -s /usr/lib64/libnsl.so.2.0.0 /usr/lib64/libnsl.so.1

USER root

#Development
RUN mkdir -p /usr/lib/oracle/19.6/client64/lib/network/admin/development
COPY ./DESA /usr/lib/oracle/19.6/client64/lib/network/admin/development
#Production
RUN mkdir -p /usr/lib/oracle/19.6/client64/lib/network/admin/production
COPY ./PROD /usr/lib/oracle/19.6/client64/lib/network/admin/production
#ENV TNS_ADMIN="development/"
RUN mkdir -p /usr/lib/oracle/19.6/client64/lib/network/admin
COPY ./DESA /usr/lib/oracle/19.6/client64/lib/network/admin


RUN export TNS_ADMIN=/usr/lib/oracle/19.6/client64/lib/network/admin
RUN export TNS_ADMIN_DEV=/usr/lib/oracle/19.6/client64/lib/network/admin/development 
RUN export TNS_ADMIN_PROD=/usr/lib/oracle/19.6/client64/lib/network/admin/production

#Agregar LDAP
COPY ./DESA/ldap.ora $/usr/lib/oracle/19.6/client64/lib/network/admin/development/ldap.ora
COPY ./PROD/ldap.ora $/usr/lib/oracle/19.6/client64/lib/network/admin/production/ldap.ora

#Pruebas:
COPY caller.sql /sql/caller.sql
COPY /sql/* /sql/
COPY login.sh /login.sh

USER 1001
RUN export NLS_LANG=SPANISH_SPAIN.AL32UTF8
RUN env
#RUN echo "sqlplus \$usuario/\$password@\$instancia @caller.sql" >> /login.sh

WORKDIR /sql

ENTRYPOINT ["bash","/login.sh"]
