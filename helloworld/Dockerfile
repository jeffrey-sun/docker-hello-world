FROM docker.oa.com:8080/public/centos-7.2

COPY info.php /data/demo/

RUN yum -y update \
    && yum -y install php

CMD ["php", "-S 0.0.0.0:8001", "-t /data/demo/"]