FROM quay-enterprise-quay-quay-enterprise.apps.ocppaz0.ar.bsch/santandertec/santander-tecnologia-docker-base-images-python-base:v3.8


RUN echo urllib3>=1.26.2 > requirements.txt
RUN echo requests>=2.25.1 >> requirements.txt
RUN echo python-gitlab>=2.5.0 >> requirements.txt
RUN echo termcolor>=1.1.0 >> requirements.txt
RUN echo xlrd>=2.0.1 >> requirements.txt
RUN pip install --upgrade pip
#RUN pip install --trusted-host nexus.iaas.ar.bsch --use-deprecated=html5lib  -r requirements.txt
RUN pip install --trusted-host nexus.iaas.ar.bsch  -r requirements.txt





