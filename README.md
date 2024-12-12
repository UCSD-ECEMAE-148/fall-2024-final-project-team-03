<div id="top"></div>

<h1 align="center">The Tank</h1>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://jacobsschool.ucsd.edu/">
    <img src="images\UCSDLogo_JSOE_BlueGold.png" alt="Logo" width="400" height="100">
  </a>
<h3>ECE/MAE148 Final Project</h3>
<p>
Team 3 Fall 2024
</p>
  
  ![IMG_3811](https://github.com/user-attachments/assets/a44a67d6-e95e-43ee-8ac0-66463c792969)
  
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#team-members">Team Members</a></li>
    <li><a href="#final-project">Final Project</a></li>
      <ul>
        <li><a href="#original-goals">Original Goals</a></li>
          <ul>
            <li><a href="#goals-we-met">Goals We Met</a></li>
            <li><a href="#our-hopes-and-dreams">Our Hopes and Dreams</a></li>
              <ul>
                <li><a href="#stretch-goal-1">Stretch Goal 1</a></li>
                <li><a href="#stretch-goal-2">Stretch Goal 2</a></li>
              </ul>
          </ul>
        <li><a href="#final-project-documentation">Final Project Documentation</a></li>
      </ul>
    <li><a href="#robot-design">Robot Design </a></li>
      <ul>
        <li><a href="#cad-parts">CAD Parts</a></li>
          <ul>
            <li><a href="#custom-designed-parts">Custom Designed Parts</a></li>
          </ul>
        <li><a href="#electronic-hardware">Electronic Hardware</a></li>
        <li><a href="#software">Software</a></li>
          <ul>
            <li><a href="#embedded-systems">Embedded Systems</a></li>
            <li><a href="#ros2">ROS2</a></li>
            <li><a href="#donkeycar-ai">DonkeyCar AI</a></li>
          </ul>
      </ul>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#authors">Authors</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- TEAM MEMBERS -->
## Team Members

<div align="center">
    <p align = "center">Agasthya, Harshit, Minjun, Purab</p>
</div>

<h4>Team Member Major and Class </h4>
<ul>
  <li>Agasthya - Mechanical Engineering, Ctrls & Robotics (MC34) - Class of 2025</li>
  <li>Harshit - Mechanical Engineering, Ctrls & Robotics (MC34) - Class of 2025</li>
  <li>Minjun - Electrical Engineering (EC27) - Class of 2026</li>
  <li>Purab - Computer Engineering (EC26) - Class of 2026</li>
</ul>

<!-- Final Project -->
## Final Project

Our project goal was to develop a car that follows a set path based on GPS cordinates searching for certain objects and shooting it with a laser. We aimed to create a project that could be useful in the defense industry creating autonomus tanks and other vehicles to save lives of military personal. Our project is developed using ROS2 packages that works with the UCSD Robocar framework to be able to control the servos in charge of aiming and shooting the laser, as well as have the car run on its set path using GNSS.


<!-- Original Goals -->
### Original Goals
- Automated Path Setup
  - Develop a package dedicated to extracting the car's path, converting it to corresponding .csv datasets for route mapping and navigation.
    - Upon launch, the car will follow a path based on data obtained from the GNSS, adhering to its route.
    - Adjust the PID variables to correct overcorrection and undercorrection when the car deviates from its path.
    - Implement real-time monitoring and adjustments to ensure the car stays on course.
- Color Recognition
  - Utilize the camera to obtain a real-time view of the environment and track colors. 
    - Determine the coordinates from the center when a color is detected.
    - Once color detection is functional, work on detecting specific objects.
    - Integrate object detection algorithms to enhance the accuracy and reliability of the system.
- CAD Design
  - Design a servo mount capable of rotating along the X and Y axes.
    - Create a mount attached to the servos to enable pointing at different locations.
    - Ensure the design is robust and can withstand the operational stresses of the system.
    - Optimize the mount for ease of assembly and maintenance.
- Servo Motor Control
  - Employ the adafruit_servokit library to move the servos and aim the laser along the X and Y axes.
    - Use coordinates received from the color or object detection model to move the servo and point at the specific object.
    - Implement precise control algorithms to ensure accurate targeting.
    - Test and calibrate the servo movements to achieve optimal performance.
- Laser Control
  - Activate the laser when the object is detected and the laser is aimed at the object.
    - Ensure safety protocols are in place to prevent accidental activation.
    - Integrate feedback mechanisms to confirm successful targeting and firing.
    - Conduct thorough testing to validate the system's reliability and effectiveness.
   
<!-- End Results -->
### Goals We Met (will fix when files are uploaded)
- [`Automated Path`](https://www.youtube.com/watch?v=wxJq66QpAlQ&feature=youtu.be): Automated Path Setup 
- [`Color Recognition with Servo Control`](Servo_control_with_OpenCV/servoControl.py): Color Recognition
- [`Object Recognition`](opencvmethod/detectface.py): Object Detection
- [`CAD Design`](CAD_Design): CAD Design
- [`Servo Control`](opencvmethod/servocontrol.py): Servo Motor Control
- [`Laser Integration`](opencvmethod/main.py): Laser Control

See [`README`](src/README.md) section in our `src` directory for breakdown of how our packages run together

### Our Hopes and Dreams
#### Stretch Goal 1
- Complete package integration with ROS
  - We would like to have ROS integration because it provides a modular and scalable framework for developing robotic applications. ROS allows for seamless communication between different components, enabling more robust control of the car. By integrating ROS, we can enhance the system's modularity, making it easier to implement additional features, debug issues, and ensure compatibility with other robotics projects in the future.

#### Stretch Goal 2
- LiDAR
  - Since our car is only driving using GPS, there are no object avoidance capabilities. LiDAR will allow us to detect obstacles on the path and navigate around them, returning to the GPS-defined route. Incorporating LiDAR enhances the system's situational awareness, making it more adaptable to dynamic environments. This development is inspired by existing projects like autonomous vehicles, which combine GNSS with LiDAR to achieve precision and safety.
### Final Project Documentation

* [Final Project Proposal](https://docs.google.com/presentation/d/1ciqbkGPFqllosRhsaxw-nCjrUmgzkP6osQgYeFSXA8M/edit#slide=id.g27c9638c8a0_0_194)

<!-- Early Quarter -->
## Robot Design

### CAD Parts

#### Custom Designed Parts
| Part | CAD Model |
|------|--------------|
| Camera Mount Top | <img src="https://github.com/user-attachments/assets/e70c9c6a-3d0f-40da-8ad1-6f0b50fabbe3" width="500" height="300" /> 
| Servo Mount | <img src="https://github.com/user-attachments/assets/95872866-f65a-4101-a95e-b4b46e49fafc" width="500" height="300" />
| Acrylic Base | <img src="https://github.com/user-attachments/assets/92d6461e-c488-4de9-8c24-d4043f407916" width="500" height="300" />
| Wire Enclosure Top | <img src="https://github.com/user-attachments/assets/15e95362-c2c0-4333-9c79-afb6ebf51052" width="500" height="300" />
| Wire Enclosure Bottom | <img src="https://github.com/user-attachments/assets/299e3a7f-eb85-44ad-ae1a-ded03609cd35" width="500" height="300" />

# Electronic Hardware
Below is a circuit diagram of the electronic hardware setup for the car.

<img width="610" alt="Screenshot 2024-12-10 173120" src="https://github.com/user-attachments/assets/04ff33a3-9295-4737-bdaa-43daaf4ea177" />

### Software
#### Embedded Systems
To program the Jetson Nano, we accessed the Jetson Nano through a remote SSH connection to an embedded Linux system onboard and ran a docker container with all the necessary dependencies to run our packages. This allowed us to eliminate any incompatibility issues and to maximize resource efficiency on the Jetson. Because of our dependencies, we ran into issues importing all of our libraries together such as cv2 and the adafruit servo library. These issues were resolved when we created a separate python environment rolling the version back for it to all work together.

#### ROS2
The base image we pulled from Docker Hub for our project development included the UCSD Robocar module, which runs on a Linux OS (Ubuntu 20.04). This module, comprising several submodules utilizing ROS/ROS2, was initially developed by Dominic Nightingale, a graduate student at UC San Diego. His framework was designed to work with a wide array of sensors and actuation methods on scale autonomous vehicles, allowing for easy control of a car-like robot while enabling it to perform autonomous tasks simultaneously.

#### DonkeyCar AI
For our early quarter course deliverables, we used DonkeyCar to train a car to drive autonomous GPS laps around a track in a simulated environment. We utilized GNSS to record the coordinates on the track and then trained the car with this data to race on a remote server. This process was instrumental in enabling our car to run autonomously on set paths. By simulating the environment and using the recorded data, we were able to refine our car's navigation capabilities and ensure it could follow predetermined routes accurately.

For path following, we used the DonkeyCar AI framework and tuned our own PID values. With the DonkeyCar framework, we connected through GPS and used PID following of waypoints for the car. This allowed us to achieve precise control and ensure the car stayed on its designated path.

<!-- Badges -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
*Thank you to my teammates, Professor Jack Silberman, and our incredible TA's Winston and Alexander for an amazing Fall 2024 class! Thank you Kiersten and Alexander for the amazing readme template.*

<!-- Authors -->
## Authors
  - [@PurabB](https://github.com/PurabB)  
  - [@MinjunSong068](https://github.com/MinjunSong068) 
  - [@AgasthyaV](https://github.com/AgasthyaV) 
  - [@hgoyal2003](https://github.com/hgoyal2003)

<!-- CONTACT -->
## Contact
* Agasthya | avalluri@ucsd.edu
* Harshit | hgoyal@ucsd.edu 
* Minjun | mis034@ucsd.edu
* Purab | pbalani@ucsd.edu


