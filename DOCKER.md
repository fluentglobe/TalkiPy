# Building using Docker

Install [Docker Desktop for macOS/Windows](https://www.docker.com/products/docker-desktop)

On a new machine create a Docker container from root directory.

    > docker build --tag k210 .

You open a build shell in the Docker container by

    > docker run -i -v /Volumes/Projects/TalkiPy:/TalkiPy -t k210:latest /bin/bash

The default toolchain path in `config.conf` is `/opt/kendryte_toolchain`. That is populated when the container is built.

The `modules_conf.mk` defines features to include in the firmware.

From the build shell do the following to create a new Firmware in `TalkiPy/ports/k210-freertos/output`

```
cd /TalkiPy
make -C mpy-cross
cd ports/k210-freertos
./config.sh
./build.sh
```


## Build and Update Talki Toy

```
brew install cmake coreutils gawk findutils gnu-sed
cd .
make -C mpy-cross
cd ports/k210-freertos

```
