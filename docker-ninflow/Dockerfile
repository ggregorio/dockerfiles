FROM quay-enterprise-quay-quay-enterprise.apps.ocppaz0.ar.bsch/santandertec/santander-tecnologia-docker-base-images-net-core-build:v5.0 AS base

USER root

ENV https_proxy "http://proxy.ar.bsch:8080"
ENV no_proxy ".ar.bsch,180.250.40.181"

# Download EPEL for RHEL 7 and missing libexif (removed from RHEL6)
RUN yum -y install "https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm"
RUN yum -y install "http://mirror.centos.org/centos/7/os/x86_64/Packages/libexif-0.6.22-1.el7.x86_64.rpm"
RUN yum -y install "http://mirror.centos.org/centos/7/os/x86_64/Packages/libpng-1.5.13-8.el7.x86_64.rpm"
RUN yum -y install "http://mirror.centos.org/centos/7/os/x86_64/Packages/giflib-4.1.6-9.el7.i686.rpm"
RUN yum -y install "https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/l/libgdiplus-2.10-10.el7.x86_64.rpm" --skip-broken


#USER 1001

#COPY build .

#ENTRYPOINT ["dotnet", "Nimflow.Hub.WebApi.dll"]
