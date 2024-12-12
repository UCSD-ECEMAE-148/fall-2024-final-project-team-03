#!/usr/bin/env python3

import cv2
import depthai as dai
from detectface import detectface
from servocontrol import servocontrol
pipeline = dai.Pipeline()
camRgb = pipeline.create(dai.node.ColorCamera)
xoutVideo = pipeline.create(dai.node.XLinkOut)
xoutVideo.setStreamName("video")
camRgb.setBoardSocket(dai.CameraBoardSocket.CAM_A)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setVideoSize(1920, 1080)
xoutVideo.input.setBlocking(False)
xoutVideo.input.setQueueSize(1)
camRgb.video.link(xoutVideo.input)
with dai.Device(pipeline) as device:

    video = device.getOutputQueue(name="video", maxSize=1, blocking=False)

    while True:
        videoIn = video.get()

        # Get BGR frame from NV12 encoded video frame to show with opencv
        # Visualizing the frame on slower hosts might have overhead
        frame = videoIn.getCvFrame()
        coords = detectface(frame)
        if coords == False:
            pass
        else:
            servocontrol(coords[0],coords[1])
        cv2.imshow("video", frame)

        if cv2.waitKey(1) == ord('q'):
            break
