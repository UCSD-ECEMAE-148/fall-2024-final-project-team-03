FROM dustynv/ros:foxy-ros-core-l4t-r32.7.1

LABEL maintainer="UCSD ECE-MAE-148 F2024 Team 3"

# working directory
ENV HOME /root
WORKDIR $HOME

# nvidia-container-runtime
#ENV NVIDIA_VISIBLE_DEVICES \
#    ${NVIDIA_VISIBLE_DEVICES:-all}
#ENV NVIDIA_DRIVER_CAPABILITIES \
#    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics


# general utilities
RUN sudo apt-get update && apt-get install -y \
    wget \
    curl \
    git \
    gdb \
    nano \
    python-dev \
    python3-pip \
    unzip \
    apt-utils \
    tmux

# pip
RUN pip3 install --upgrade pip

#### ROS2 SETUP

# Locale options
RUN sudo apt-get install -y locales
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# install development tools and ROS tools
RUN sudo apt-get install -y \
  build-essential \
  cmake \
  python3-catkin-pkg-modules \
  python3-colcon-common-extensions \
  python3-rosdep \
  python3-vcstool

# install python packages
# specify a version of flake8 as the latest (3.8 is not compatible with ament)
RUN pip3 install -U --ignore-installed \
  argcomplete \
  flake8==3.7 \
  flake8-blind-except \
  flake8-builtins \
  flake8-class-newline \
  flake8-comprehensions \
  flake8-deprecated \
  flake8-docstrings \
  flake8-import-order \
  flake8-quotes \
  pytest-repeat \
  pytest-rerunfailures \
  pytest \
  pytest-cov \
  pytest-runner \
  setuptools 

# install Fast-RTPS dependencies
RUN sudo apt-get install --no-install-recommends -y \
  libasio-dev \
  libtinyxml2-dev

# install CycloneDDS dependencies
RUN sudo apt-get install --no-install-recommends -y \
  libcunit1-dev

#### TENSORFLOW

WORKDIR $HOME

# install tensorflow
#RUN export LD_LIBRARY_PATH=${LD_LIBRARY_PATH:+${LD_LIBRARY_PATH}:}/usr/local/cuda/extras/CUPTI/lib64
#RUN pip install tensorflow

# tensorflow object detection dependencies from:
# https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#install-prerequisites
# https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md
RUN sudo apt-get install -y bash

RUN sudo apt-get install -y \
  protobuf-compiler \
  python-lxml \
  python-tk

RUN pip install --ignore-installed \
  Cython \
  contextlib2 \
  jupyter \
  matplotlib \
  Pillow

# get tensorflow models repository
# specify 2.3.x branch for compatibility with available TF version on jetson nano
# TODO: check v2.20 WIP object detection https://github.com/tensorflow/models/tree/v2.2.0/official/vision/detection
RUN git clone -b r2.3.0 https://github.com/tensorflow/models.git /usr/local/lib/python3.6/dist-packages/tensorflow/models

#protobuf compilation
WORKDIR /usr/local/lib/python3.6/dist-packages/tensorflow/models/research
RUN protoc object_detection/protos/*.proto --python_out=.

# Tensorflow-Slim (required for image segmentation)
RUN pip install tf_slim

# optional install COCO API for COCO metrics
#RUN git clone https://github.com/cocodataset/cocoapi.git $HOME/cocoapi
#WORKDIR $HOME/cocoapi/PythonAPI
#RUN rm Makefile
#COPY scripts/coco/Makefile $HOME/cocoapi/PythonAPI/Makefile
#RUN make
#RUN cp -r pycocotools /usr/local/lib/python3.6/dist-packages/tensorflow/models/research
#RUN pip install pycocotools

##### ROS2 VISION OPEN CV

## the vision open cv package is currently not used due to bugs in its ROS 2 version
#RUN apt-get update && apt-get install -y libcanberra-gtk-module libboost-all-dev
#RUN mkdir -p $HOME/ros2_vision_opencv_ws/src
#WORKDIR $HOME/ros2_vision_opencv_ws/src
#RUN git clone -b ros2 https://github.com/ros-perception/vision_opencv.git

##### INSTALL ROS 2 TENSORFLOW

RUN pip3 install distro

WORKDIR $HOME

RUN rosdep update
RUN sudo apt-get update

RUN mkdir -p $HOME/tf_ws/src
ADD https://api.github.com/repos/alsora/ros2-tensorflow/git/refs/heads/master version.json
RUN git clone https://github.com/MinjunSong068/ros2-tensorflow $HOME/tf_ws/src/ros2-tensorflow
WORKDIR $HOME/tf_ws
# RUN rosdep install --from-paths src --ignore-src -r

#RUN sudo apt-get install -y ros-foxy-image-transport ros-foxy-vision-msgs \
#   ros-foxy-derived-object-msgs ros-foxy-rmw-cyclonedds-cpp ros-foxy-sensor-msgs-py \
#   ros-foxy-ament-cmake-python

RUN pip3 install --ignore-installed sphinx-autodoc-typehints sphinx-rtd-theme sphinx cmake

#RUN apt-get install -y python3-sphinx python3-sphinx-autodoc-typehints python3-sphinx-rtd-theme

# RUN source /opt/ros/foxy/install/setup.bash

#RUN sudo apt-get update \
 # && sudo apt-get upgrade -y

RUN . /opt/ros/foxy/install/setup.bash \
  && rosdep update

RUN mkdir -p rclpy_ws/src \
  && cd rclpy_ws/src \
  && . /opt/ros/foxy/install/setup.bash \
  && git clone -b foxy https://github.com/ros2/rclpy.git \
  && cd .. \
  && colcon build --symlink-install

RUN sudo apt-get update \
  && sudo apt-get install -y python3-pip pkg-config \
  && sudo apt-get install -y libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran \
  && sudo ln -s /usr/include/locale.h /usr/include/xlocale.h \
  && sudo pip3 install --verbose 'protobuf<4' 'Cython<3' 


##Install tensorflow

RUN pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v45 tensorflow==2.3.1
RUN export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1

##Adafruit servo motor dependencies
RUN pip3 install adafruit-blinka==3.3.4 \
  adafruit-pureIO==1.0.4 \
  Jetson.GPIO==2.0.4 \
  adafruit-circuitpython-pca9685==3.2.5 \
  adafruit-circuitpython-register==1.7.1 \
  adafruit-circuitpython-servokit==1.1.0 \
  adafruit-circuitpython-busdevice==4.3.0 \
  adafruit-platformDetect==1.4.5 \
  pyserial==3.4 \
  pyusb==1.0.2 \
  spidev==3.4 \
  sysv-ipc==1.0.1

RUN sudo apt update \
	&& sudo apt upgrade -y

RUN . /opt/ros/foxy/install/setup.bash \
  && rosdep install --from-paths src --ignore-src --rosdistro foxy -y \
  && colcon build

RUN sudo apt-get install -y xaw3dg xorg-dev qtbase5-dev qtdeclarative5-dev

##image tools was installed by default with AMD64 but didn't seem to appear on ARM so build it manually
RUN . ./install/setup.bash \
  && cd src \
  && git clone -b foxy https://github.com/ros2/demos.git \
  && cd .. \
  && colcon build --packages-select image_tools

##opencv dependencies for openCV node
RUN . ./install/setup.bash \
  && cd src \
  && git clone -b foxy https://github.com/ros-perception/vision_opencv \
  && cd .. \
  && colcon build --symlink-install --packages-select cv_bridge image_geometry opencv_tests vision_opencv

#### SET ENVIRONMENT

WORKDIR $HOME

RUN echo "source /opt/ros/foxy/install/setup.sh" >> ~/.bashrc \
  && echo "source $HOME/tf_ws/install/local_setup.sh" >> ~/.bashrc \
  && echo "export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.8/dist-packages/tensorflow/models/research" >> ~/.bashrc \
  && echo "export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.6/dist-packages/tensorflow/models/research" >> ~/.bashrc \
  && echo "export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1" >> ~/.bashrc  
  ##needed cause of this -> https://forums.developer.nvidia.com/t/error-importerror-usr-lib-aarch64-linux-gnu-libgomp-so-1-cannot-allocate-memory-in-static-tls-block-i-looked-through-available-threads-already/166494/4
