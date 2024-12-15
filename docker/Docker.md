## Docker instructions for ROS2-Tensorflow object detection system

## Clone the repo 
```commandline
git clone -b main https://github.com/MinjunSong068/ros2-tensorflow
```

## Docker build (inside the Docker folder)
```
bash build.sh
```

## Run the docker image
```
bash run.sh
```

## Docker image usage guide
* The system has multiple nodes so I either recommend using tmux (installed in container) or just using multiple docker containers (cycloneDDS will handle the container to container communication for you)
* If you want to start tmux
```commandline
tmux
```
* Ctrl B + % to vertically split a terminal
* Ctrl B + " to horizonally split a terminal
* Ctrl B + o to move around the split terminals
1. Source ROS2
```commandline
source tf_ws/install/setup.bash
```
2. Start the tensorflow object detection server
```commandline
ros2 run tf_detection_py server
```
* This process will download the object detection model from the tensorflow object detection zoo and will take around 2-3 minutes
* A sample workload can be ran if you want to see if the server is capable of object detection through
```commandline
ros2 run tf_detection_py client_test
```

3. Start the image input pipeline
```commandline
ros2 run image_tools cam2image --ros-args -p frequency:=2.0
```

4. Start the openCV servo movement
```commandline
ros2 run tf_classification opencv
```
