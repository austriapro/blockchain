# updated 2023/08/04 to MultiChain 2.3.3
# see https://hub.docker.com/repository/docker/cbaumann/multichain-2-base/general

FROM cbaumann/multichain-2-base
MAINTAINER cbaumann

ADD ./runchain.sh /root/runchain.sh
RUN chmod a+x /root/runchain.sh

CMD ["/bin/bash", "/root/runchain.sh"]
