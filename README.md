TalkiPy
=======================

</br>

<div class="title_pic">
    <img src="ports/k210-freertos/docs/assets/micropython.png">
</div>

</br>
</br>

**TalkiPy, Hello! My name is Talki**

TalkiPy is designed to experiment with Talki Activities during development, based on the [Micropython](http://www.micropython.org) syntax, running on a very powerful embedded AIOT chip [K210](https://kendryte.com).

## Simple code

Find I2C devices:

```python
from machine import I2C

i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29)
devices = i2c.scan()
print(devices)
```

Take picture:

```python
import sensor
import image
import lcd

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
while True:
    img=sensor.snapshot()
    lcd.display(img)
```

## Release

See [Releases page](https://github.com/fluentglobe/TalkiPy/releases)

## Documentation

Doc refer to [fluentglobe.com docs](https://fluentglobe.com/talki/py)


## Build From Source

    > docker build --tag t210 .
    > docker run -i -v /Volumes/Projects/TalkiPy:/TalkiPy -t k210:latest /bin/bash

See [build doc](ports/k210-freertos/README.md)

## License

See [LICENSE](LICENSE.md) file
