FROM buildpack-deps:stretch

ARG VERSION=master

ARG DEBIAN_FRONTEND=noninteractive

ENV PATH /usr/local/bin:$PATH
ENV KENDRYTE_VERSION 8.2.0-20190213

RUN apt-get update \
  && apt-get install -y make unrar-free autoconf automake libtool gcc g++ gperf \
    flex bison texinfo gawk ncurses-dev libexpat-dev python-dev python python-serial \
    sed git unzip bash help2man wget bzip2 build-essential libtool cmake

RUN apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && useradd micropython

RUN mkdir /opt/kendryte-toolchain
RUN chmod 775 /opt/kendryte-toolchain

RUN wget -O /tmp/kendryte-toolchain-ubuntu-amd64-$KENDRYTE_VERSION.tar.gz https://s3.cn-north-1.amazonaws.com.cn/dl.kendryte.com/documents/kendryte-toolchain-ubuntu-amd64-$KENDRYTE_VERSION.tar.gz
RUN tar -xzf /tmp/kendryte-toolchain-ubuntu-amd64-$KENDRYTE_VERSION.tar.gz -C /opt \
 && rm /tmp/kendryte-toolchain-ubuntu-amd64-$KENDRYTE_VERSION.tar.gz

USER micropython

ENV PATH=/opt/kendryte-toolchain/bin:$PATH

# RUN make -C mpy-cross

# RUN cd ports/k210-freertos && ./build.sh
