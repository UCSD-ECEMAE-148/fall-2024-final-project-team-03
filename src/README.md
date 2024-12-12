### How to run:
- set up an environment with:
  - Python 3.6-3.8
  - GNSS Configuration:
      Ublox:
      This GPS doesn't require any configuration out of the gate, it just starts transmitting data right away. Later on the instructions will tell you what to add in myconfig.py to get it to work with donkeycar.
      
      How to Plug PointOneNav to Donkeycar
      Make sure your user is added to the dialout group. If not
      sudo adduser jetson dialout
      sudo reboot now
       Download https://drive.google.com/file/d/1BK_UjH-He9d_D4eObWMHzpHHCqmtq75h/view?usp=share_link (Note that this zip file cannot be shared outside of the class. It is still proprietary as of now)
      Alternatively, git clone https://github.com/UCSD-ECEMAE-148/quectel
      Unzip.
      Run
      cd quectel-lg69t-am.0.15.0/p1_runner (or if you cloned from github, cd quectel/p1_runner)
      deactivate  (This should get you out of the current environment)
      wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-pypy3-Linux-aarch64.sh .
      bash Mambaforge-pypy3-Linux-aarch64.sh
      Reboot the jetson
      mamba create --name py37 -c conda-forge python=3.7 pip 
      mamba activate py37
      pip3 install -e .  
      %If this fails, you can try just going to the p1_runner directory and running the python3 bin/config_tool.py command, and then doing “pip install ____” for all the missing things, you may just need
      pip install pyserial
      pip install fusion_engine_client
      pip install pynmea
      pip install ntripstreams
      pip install websockets
      python3 bin/config_tool.py reset factory
      python3 bin/config_tool.py apply uart2_message_rate nmea gga on
      python3 bin/config_tool.py save
      python3 bin/runner.py --device-id <polaris_username> --polaris <polaris_password> --device-port /dev/ttyUSB1   
      (if not getting any data including Nans try USB0)
      	Note: The GPS corrections will only happen when you are actively running runner.py. I recommend making a bashrc command that you can run to start up the runner.py program easily in a 2nd terminal while using the GPS for anything.
      Create a project with the DonkeyCar path follow template
      Open a new terminal window
      Make sure that the donkey car environment is running
      source ~/projects/envs/donkey/bin/activate
       cd ~/projects
      donkey createcar --path ./mycar --template path_follow
      Set the following in the myconfig.py
      GPS_SERIAL = “/dev/ttyUSB2” (USB1 if USB0 used above) #pointone nav
      GPS_SERIAL = “/dev/ttyUSB0” #ublox
      GPS_SERIAL_BAUDRATE = 460800 #pointone nav
      GPS_SERIAL_BAUDRATE = 38400 #ublox
      GPS_DEBUG = True
      HAVE_GPS = True
      GPS_NMEA_PATH = None
      Also set things like the VESC parameters in myconfig.py. You can copy these over from the donkeycar you created earlier.
      Run
      python3 manage.py drive
      You should see GPS positions being outputted after you run Donkeycar. If you don’t want to output set GPS_DEBUG to False
      Configure button actions
      SAVE_PATH_BTN is the button to save the in-memory path to a file.
      LOAD_PATH_BTN is the button to (re)load path from the csv file into memory.
      RESET_ORIGIN_BTN is the button to set the current position as the origin.
      ERASE_PATH_BTN is the button to erase path from memory and reset the origin.
      TOGGLE_RECORDING_BTN is the button to toggle recording mode on or off. Note that there is a pre-assigned button in the web ui, so there is not need to assign this button to one of the web/w* buttons if you are using the web ui.
      INC_PID_D_BTN is the button to change PID 'D' constant by PID_D_DELTA.
      DEC_PID_D_BTN is the button to change PID 'D' constant by -PID_D_DELTA
      INC_PID_P_BTN is the button to change PID 'P' constant by PID_P_DELTA
      DEC_PID_P_BTN is the button to change PID 'P' constant by -PID_P_DELTA
      The logitech buttons are named stuff like “X” or “R1” See the example config below.
      SAVE_PATH_BTN = "R1"    	# button to save path
      LOAD_PATH_BTN = "X"         	# button (re)load path
      RESET_ORIGIN_BTN = "B" 	# button to press to move car back to origin
      ERASE_PATH_BTN = "Y" 	# button to erase path
      TOGGLE_RECORDING_BTN = "L1" # button to toggle recording mode
      INC_PID_D_BTN = None        	# button to change PID 'D' constant by PID_D_DELTA
      DEC_PID_D_BTN = None        	# button to change PID 'D' constant by -PID_D_DELTA
      INC_PID_P_BTN = "None"        	# button to change PID 'P' constant by PID_P_DELTA
      DEC_PID_P_BTN = "None"        	# button to change PID 'P' constant by -PID_P_DELTA
      #
      
      Recording a path
      The algorithm assumes we will be driving in a continuous connected path such that the start and end are the same. You can adjust the space between recorded waypoints by editing the PATH_MIN_DIST value in myconfig.py You can change the name and location of the saved file by editing the PATH_FILENAME value.
      Enter User driving mode using either the web controller or a game controller.
      Move the car to the desired starting point
      Erase the path in memory (which will also reset the origin).
      Make sure to reset the origin!!! If you didn’t need to erase the path in memory you can just
      Toggle recording on.
      Drive the car manually around the track until you reach the desired starting point again.
      Toggle recording off.
      If desired, save the path.
      Following a path
      Enter User driving mode using either the web controller or a game controller.
      Move the car to the desired starting point - make sure it’s the same one from when you recorded the path
      Reset the origin (be careful; don't erase the path, just reset the origin).
      Load the path
      Enter Autosteering or Autopilot driving mode. This is normally done by pressing the start button either once or twice If you are in Autosteering mode you will need to manually provide throttle for the car to move. If you are in Autopilot mode the car should drive itself completely.
      Configuring Path Follow Parameters
      So the algorithm uses the cross-track error between a desired line and the vehicle's measured position to decide how much and which way to steer. But the path we recorded is not a simple line; it is a lot of points that is typically some kind of circuit. As described above, we use the vehicle's current position to choose a short segment of the path that we use as our desired track. That short segment is recalculated every time we get a new measured car position. There are a few configuration parameters that determine exactly which two points on the path that we use to calculate the desired track line.
      PATH_SEARCH_LENGTH = None   # number of points to search for closest point, None to search entire path
      PATH_LOOK_AHEAD = 1         # number of points ahead of the closest point to include in cte track
      PATH_LOOK_BEHIND = 1        # number of points behind the closest point to include in cte track   
      Generally, if you are driving very fast you might want the look ahead to be larger than if driving slowly so that your steering can anticipate upcoming curves. Increasing the length of the resulting track line, by increasing the look behind and/or look ahead, also acts as a noise filter; it smooths out the track. This reduces the amount of jitter in the controller. However, this must be balanced with the true curves in the path; longer track segments effectively 'flatten' curves and so can result in understeer; not steering enough when on a curve.
      Determining PID Coefficients
      The PID coefficients are the most important (and time consuming) parameters to configure. If they are not correct for your car then it will not follow the path. The coefficients can be changed by editing their values in the myconfig.py file.
      PID_P is the proportional coefficient; it is multiplied with the cross-track error. This is the most important parameter; it contributes the most to the output steering value and in some cases may be all that is needed to follow the line. If this is too small then car will not turn enough when it reaches a curve. If this to too large then it will over-react to small changes in the path and may start turning in circles; especially when it gets to a curve.
      PID_D is the differential coefficient; it is multiplied with the change in the cross-track error. This parameter can be useful in reducing oscillations and overshoot.
      PID_I is the integral coefficient; it is multiplied with the total accumulated cross-track error. This may be useful in reducing offsets caused by accumulated error; such as if one wheel is slightly smaller in diameter than another.
      Determining PID Coefficients can be difficult. One approach is:
      First determine the P coefficient.
      zero out the D and the I coefficients.
      Use a kind of 'binary' search to find a value where the vehicle will roughly follow a recorded straight line; probably oscillating around it. It will be weaving
      Next find a D coefficient that reduces the weaving (oscillations) on a straight line. Then record a path with a tight turn. Find a D coefficient that reduces the overshoot when turning.
      You may not even need the I value. If the car becomes unstable after driving for a while then you may want to start to set this value. It will likely be much smaller than the other values.
      Be patient. Start with a reasonably slow speed. Change one thing at a time and test the change; don't make many changes at once. Write down what is working.
      Once you have a stable PID controller, then you can figure out just how fast you can go with it before autopilot becomes unstable. If you want to go faster then set the desired speed and start tweaking the values again using the method suggested above.








Driving the Robot to Collect data
Remember you are driving at max of x (0.x) Throttle power based on the 
myconfig.py that you edited.
The robot is not controlling speed but power given the motor using PWM values
Transmitted from the Single Board Computer (SBC) like a Jetson Nano (JTN)  to the 
Electronic Speed Controller (ESC).

To reverse you may have to reverse, stop, reverse. This is a feature of some 
ESCs used in RC cars to prevent damaging gears when changing from forward to reverse.

On the JTN
If you are not changing directory automatically when the user logs in
cd ~/projects/d3 

(env) jetson@ucsdrobocar00:~/projects/d3 $ 

python manage.py drive

Note: CTRL-C stop the manage.py drive
---
If you get an error on the joystick or Donkey stops loading the JoyStick 
it is because game controller is off 
or not connected/paired with the JTN

ls
config.py  data  logs  manage.py  models 

ls data
tub_1_17-10-13

If you want to wipe clean the data collected
Remove the content of the ~/projects/d3/data directory. It should be tub_……
You can delete the entire directory then create it again.
~/projects/d3 $ 
rm -rf data
mkdir data


Follow the Donkey Docs to install the Donkey AI framework into your PC http://docs.donkeycar.com

On the PC
Activate the virtual environment. I am assuming you have your virtual environment under
~/projects/envs/donkey
source ~/projects/envs/donkey/bin/activate
cd projects
cd d3

SSH into the JTN
ssh jetson@ucsdrobocar00.local

On the JTN
If you are not changing directory automatically when the user logs in
cd ~/projects/d3 

(env) jetson@ucsdrobocar00:~/projects/d3 $ 

python manage.py drive

Note: CTRL-C stop the manage.py drive
Drive the robot  to collect data

On the PC
Get data from JTN
Transfer all data from the JTN to the PC and delete data that was deleted from the JTN
rsync -a --progress --delete jetson@ucsdrobocar00.local:~/d3/data  ~/projects/d3

ls data
tub_1_17-10-12

Train model on all data (Tubes)
python train.py --model=models/date_name.h5

To train using a particular tube
python train.py --tub ~/projects/d3/data/tub_1_18-01-07 --model=models/model_name.h5


To make an incremental training using a previous model
python train.py --tub ~/projects/d3/data/NAME_OF_NEW_TUBE --transfer=models/NAME_OF_PREVIOUS_MODEL.h5  --model=models/NAME_OF_NEW_MODEL.h5
