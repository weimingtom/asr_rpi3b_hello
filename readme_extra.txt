https://blog.csdn.net/u012206617/article/details/105094522/
/var/cache/apt/archive

镜像
2018-04-18-raspbian-stretch
https://blog.csdn.net/xs18952904/article/details/102327954

https://raspberrypi.stackexchange.com/questions/6974/how-can-i-determine-which-os-image-i-am-running
$ cat /etc/rpi-issue
Raspberry Pi reference 2016-05-10

$ cd /usr/src
$ grep -R 'snd_soc_codec_' *
/usr/src/linux-headers-4.14.79+/include/sound/soc.h

$ dpkg -l raspberrypi-kernel
1.20181112-1
$ dpkg -l raspberrypi-kernel-headers
1.20181112-1

下载headers的deb包
http://archive.raspberrypi.org/debian/pool/main/r/raspberrypi-firmware/
http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/pool/main/r/raspberrypi-firmware/
https://mirrors.tuna.tsinghua.edu.cn/raspberrypi/pool/main/r/raspberrypi-firmware/

$ apt-cache showpkg raspberrypi-kernel-headers

https://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/pool/main/d/dkms/
https://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/pool/main/i/i2c-tools/
https://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/pool/main/a/alsa-plugins/
https://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/pool/main/s/speex/

libspeex
