# smart_home (cctv)



### 기능처리도 
<img width="852" alt="KakaoTalk_20210901_152518711" src="https://user-images.githubusercontent.com/80305565/131622524-5923bb9e-4e5f-4e2b-9f00-cc9249a453cd.png">

## ovenCV
---------------
### 0. openCV가 설치되어있는지 확인한다.
```
pkg-config --modversion opencv
```
### 1. openCV 패키지들을 설치합니다.
순서대로 설치해줍니다.

```
sudo apt-get install build-essential cmake
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev
sudo apt-get install libv4l-dev v4l-utils
sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
sudo apt-get install libgtk2.0-dev
sudo apt-get install mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev
sudo apt-get install libatlas-base-dev gfortran libeigen3-dev
sudo apt-get install python2.7-dev python3-dev python-numpy python3-numpy
```

### 2. openCV 소스코드를 다운받습니다.

```
mkdir opencv
cd opencv
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.1.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.1.zip
unzip opencv_contrib.zip
```

### 3. 컴파일을 준비합니다.
```
cd opencv-4.5.1
mkdir build
cd build


cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=OFF -D WITH_IPP=OFF -D WITH_1394=OFF -D BUILD_WITH_DEBUG_INFO=OFF -D BUILD_DOCS=OFF -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=OFF -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D ENABLE_NEON=ON -D ENABLE_VFPV3=ON -D WITH_QT=OFF -D WITH_GTK=ON -D WITH_OPENGL=ON -D OPENCV_ENABLE_NONFREE=ON -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.5.1/modules -D WITH_V4L=ON -D WITH_FFMPEG=ON -D WITH_XINE=ON -D ENABLE_PRECOMPILED_HEADERS=OFF -D BUILD_NEW_PYTHON_SUPPORT=ON -D OPENCV_GENERATE_PKGCONFIG=ON ../
```
### 4. 메모리를 늘려줍니다
```
sudo nano /etc/dphys-swapfile
CONF_SWAPSIZE=2048
sudo /etc/init.d/dphys-swapfile restart
```
### 5. 컴파일을 해줍니다.
```
time make -j4
```
'building cxx object modules/python3/cmakefiles/opencv_python3.dir/__/src2/cv2.cpp.o'
이라는 오류가 발생하면 ctrl + c를 해서 강제 종료한 뒤
```
make
```
를 입력해줍니다.
### 5. 컴파일 완료된 파일을 설치해줍니다.
```
sudo make install
```
openCV라이브러리를 찾을 수 있도록 아래 명령어를 실행시켜주세요.
```
sudo ldconfig
```
dphys-swapfile 설정파일을 원래대로 수정해줍니다.
```
sudo nano /etc/dphys-swapfile
sudo /etc/init.d/dphys-swapfile restart
```
설치가 정상적으로 확인해봅니다.
```
pi@raspberrypi:~/opencv/opencv-4.5.1/build $ python3
Python 3.7.3 (default, Jul 25 2020, 13:03:44)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> cv2.__version__
'4.5.1'
>>> quit()
```
