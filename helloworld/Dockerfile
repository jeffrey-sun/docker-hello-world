FROM docker.oa.com:8080/public/centos-7.2
RUN mkdir -p /data/DisasterRecovery
ADD * /data/DisasterRecovery/ 
RUN yum -y update \
    && yum -y install gcc-c++ gcc \
    && cd /data/DisasterRecovery \
    && g++ -c main.cpp \
    && g++ -o test main.o \
    && chmod +x ./start.sh
CMD ["sh","/data/DisasterRecovery/start.sh"]

