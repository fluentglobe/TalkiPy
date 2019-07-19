FROM buildpack-deps:buster

ARG VERSION=master

ARG DEBIAN_FRONTEND=noninteractive

ENV PATH /usr/local/bin:$PATH
ENV KENDRYTE_VERSION 8.2.0-20190409

RUN apt-get update \
  && apt-get install -y make unrar-free autoconf automake libtool gcc g++ gperf \
    flex bison texinfo gawk ncurses-dev libexpat-dev python3-dev python3 python3-pip \
    sed git unzip bash help2man wget bzip2 build-essential libtool cmake

RUN apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && useradd micropython

RUN mkdir /opt/kendryte-toolchain
RUN chmod 775 /opt/kendryte-toolchain

RUN wget -O /tmp/kendryte-toolchain-ubuntu-amd64-$KENDRYTE_VERSION.tar.xz http://dl.cdn.sipeed.com/kendryte-toolchain-ubuntu-amd64-$KENDRYTE_VERSION.tar.xz
RUN tar -Jxvf /tmp/kendryte-toolchain-ubuntu-amd64-$KENDRYTE_VERSION.tar.xz -C /opt \
 && rm /tmp/kendryte-toolchain-ubuntu-amd64-$KENDRYTE_VERSION.tar.xz

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --requirement ./requirements.txt

USER micropython

ENV PATH=/opt/kendryte-toolchain/bin:$PATH

# RUN make -C mpy-cross

# RUN cd ports/k210-freertos && ./build.sh
