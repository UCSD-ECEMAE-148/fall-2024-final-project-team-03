#!/usr/bin/env python3

def servocontrol(x,y):
	import cv2
	import depthai as dai
	import numpy as np
	from adafruit_servokit import ServoKit
	kit = ServoKit(channels = 16,frequency = 100)
	y_axis = kit.servo[1]
	x_axis = kit.servo[0]
	x_axis.set_pulse_width_range(750,2250)
	y_axis.set_pulse_width_range(1400,2800)
	coordrange = range(0,801)
	x_range = np.linspace(104,72,len(coordrange))
	y_range = np.linspace(146,93,len(coordrange))
	xindex = coordrange.index(x)
	yindex = coordrange.index(y)
	x_axis.angle = x_range[xindex]
	y_axis.angle = y_range[yindex]
