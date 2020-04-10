-----(if online)  

(Open raspbian desktop WIFI, with password)  

$ sudo leafpad /etc/apt/sources.list.d/raspi.list
deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ stretch main ui
# Uncomment line below then 'apt-get update' to enable 'apt-get source'
#deb-src http://archive.raspberrypi.org/debian/ stretch main ui

$ sudo leafpad /etc/apt/sources.list
#deb http://raspbian.raspberrypi.org/raspbian/ stretch main contrib non-free rpi
deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi
#deb http://mirrordirector.raspberrypi.org/raspbian/ stretch main contrib non-free rpi
#deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi
#deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi
# Uncomment line below then 'apt-get update' to enable 'apt-get source'
#deb-src http://raspbian.raspberrypi.org/raspbian/ stretch main contrib non-free rpi

$ sudo apt update
$ sudo dpkg -i raspberrypi-kernel-headers_1.20180417-1_armhf.deb 
$ apt-get -y install dkms i2c-tools libasound2-plugins

-----(or if offline)

$ sudo dpkg -i raspberrypi-kernel-headers_1.20180417-1_armhf.deb 
$ sudo dpkg -i dkms_2.3-2_all.deb
$ sudo dpkg -i i2c-tools_3.1.2-3_armhf.deb
$ sudo dpkg -i libspeexdsp1_1.2_rc1.2-1_armhf.deb
$ sudo dpkg -i libasound2-plugins_1.1.1-1_armhf.deb

----------------

$ cd seeed-voicecard
$ chmod +x ./install.sh
$ chmod +x ./seeed-voicecard
$ chmod +x ./uninstall.sh
$ sudo ./uninstall.sh
$ sudo ./install.sh
$ reboot
$ aplay -l
card 1: seeed2micvoicec
$ arecord -l
card 1: seeed2micvoicec
-----------------
$ cd ~
$ cd baidu_STT
$ python Smart_Fan.py

-----------------
-----------------
(Ref:)   
	http://wiki.seeedstudio.com/cn/ReSpeaker_2_Mics_Pi_HAT/
	https://console.bce.baidu.com
	https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/src/baidu_STT.zip
-----------------
(not necessary:) 
$ sudo apt update
$ sudo apt install audacity
$ audacity
ALSA, bcm2835 alsa: - (hw£º0£¬0), ac108, 2 or 4
$ alsamixer
f6 -> seeed-2mic
-----------------
(not necessary:) 
$ sudo apt install mpg123
$ pip install baidu-aip monotonic pyaudio
---------------------
