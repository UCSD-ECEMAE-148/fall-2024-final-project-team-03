#### How to run:
## Ublox GPS Configuration
This GPS requires no initial configuration. It starts transmitting data out of the box. Follow the instructions below to configure it in `myconfig.py` for DonkeyCar.

## PointOneNav Configuration
### Steps to Set Up PointOneNav GPS with DonkeyCar:
1. **Add User to Dialout Group**:
    ```bash
    sudo adduser jetson dialout
    sudo reboot now
    ```

2. **Download Required Files**:
   - [PointOneNav Files](https://drive.google.com/file/d/1BK_UjH-He9d_D4eObWMHzpHHCqmtq75h/view?usp=share_link) (Proprietary; cannot be shared outside the class).
   - Alternatively, clone the repository:
     ```bash
     git clone https://github.com/UCSD-ECEMAE-148/quectel
     ```

3. **Extract and Navigate**:
   ```bash
   cd quectel-lg69t-am.0.15.0/p1_runner
   ```
   For GitHub clone:
   ```bash
   cd quectel/p1_runner
   ```

4. **Install Mamba and Set Up Environment**:
   ```bash
   deactivate
   wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-pypy3-Linux-aarch64.sh
   bash Mambaforge-pypy3-Linux-aarch64.sh
   sudo reboot now
   mamba create --name py37 -c conda-forge python=3.7 pip
   mamba activate py37
   pip3 install -e .
   ```
   If installation fails, install missing dependencies manually:
   ```bash
   pip install pyserial
   pip install fusion_engine_client
   pip install pynmea
   pip install ntripstreams
   pip install websockets
   ```

5. **Configure PointOneNav**:
   ```bash
   python3 bin/config_tool.py reset factory
   python3 bin/config_tool.py apply uart2_message_rate nmea gga on
   python3 bin/config_tool.py save
   python3 bin/runner.py --device-id <polaris_username> --polaris <polaris_password> --device-port /dev/ttyUSB1
   ```
   - If no data appears, try using `/dev/ttyUSB0` instead of `/dev/ttyUSB1`.

6. **Automate Runner Startup**:
   Create a `bashrc` command to easily run `runner.py` in a second terminal while using the GPS.

## DonkeyCar Configuration
### Create a Project with Path Follow Template:
1. Open a terminal and activate the DonkeyCar environment:
   ```bash
   source ~/projects/envs/donkey/bin/activate
   cd ~/projects
   donkey createcar --path ./mycar --template path_follow
   ```

2. Update `myconfig.py`:
   ```python
   GPS_SERIAL = "/dev/ttyUSB2"  # PointOneNav (use USB1 if USB0 is used above)
   GPS_SERIAL = "/dev/ttyUSB0"  # Ublox
   GPS_SERIAL_BAUDRATE = 460800  # PointOneNav
   GPS_SERIAL_BAUDRATE = 38400  # Ublox
   GPS_DEBUG = True
   HAVE_GPS = True
   GPS_NMEA_PATH = None
   ```
   - Copy other parameters (e.g., VESC parameters) from a previously created DonkeyCar.

3. Start DonkeyCar:
   ```bash
   python3 manage.py drive
   ```
   - GPS positions will be output if `GPS_DEBUG` is set to `True`.

### Button Actions Configuration:
```python
SAVE_PATH_BTN = "R1"       # Save path
LOAD_PATH_BTN = "X"        # Load path
RESET_ORIGIN_BTN = "B"     # Reset origin
ERASE_PATH_BTN = "Y"       # Erase path
TOGGLE_RECORDING_BTN = "L1" # Toggle recording
INC_PID_D_BTN = None         # Increase PID 'D'
DEC_PID_D_BTN = None         # Decrease PID 'D'
INC_PID_P_BTN = None         # Increase PID 'P'
DEC_PID_P_BTN = None         # Decrease PID 'P'
```

### Recording a Path:
1. Enter User Driving Mode.
2. Move the car to the starting point.
3. Erase the path in memory to reset the origin.
4. Toggle recording on and drive the car manually along the path.
5. Toggle recording off when the path is complete.
6. Save the path if desired.

### Following a Path:
1. Enter User Driving Mode.
2. Move the car to the starting point.
3. Reset the origin (do not erase the path).
4. Load the path.
5. Enter Autosteering or Autopilot Mode.

## Path Follow Parameters:
```python
PATH_SEARCH_LENGTH = None  # Number of points to search for closest point
PATH_LOOK_AHEAD = 1        # Points ahead of the closest point
PATH_LOOK_BEHIND = 1       # Points behind the closest point
```
- Increase `PATH_LOOK_AHEAD` for faster driving to anticipate curves.

## PID Coefficients:
1. **Proportional (P)**: Controls the steering based on cross-track error.
2. **Differential (D)**: Reduces oscillations and overshoot.
3. **Integral (I)**: Reduces accumulated offset errors.

### Steps to Tune PID:
1. Start with `PID_D = 0` and `PID_I = 0`. Tune `PID_P` first.
2. Add `PID_D` to reduce oscillations.
3. Add `PID_I` if needed to correct offsets.

## Data Collection:
### Drive the Robot:
1. Activate the DonkeyCar environment:
   ```bash
   python manage.py drive
   ```
2. If joystick errors occur, ensure the controller is paired and powered on.

### Wipe Collected Data:
```bash
rm -rf ~/projects/d3/data
mkdir ~/projects/d3/data
```

### Transfer Data to PC:
```bash
rsync -a --progress --delete jetson@ucsdrobocar00.local:~/projects/d3/data ~/projects/d3
```

## Training the Model:
1. Train on all data:
   ```bash
   python train.py --model=models/date_name.h5
   ```
2. Train on specific data:
   ```bash
   python train.py --tub ~/projects/d3/data/tub_1_18-01-07 --model=models/model_name.h5
   ```
3. Incremental training:
   ```bash
   python train.py --tub ~/projects/d3/data/NEW_TUBE --transfer=models/OLD_MODEL.h5 --model=models/NEW_MODEL.h5
   ```

## Optional: Clean Up Data:
```bash
donkey tubclean data
```
### Run
```bash
   python main.py
   rsync -a --progress ~/projects/d3/models/ jetson@ucsdrobocar00:~/projects/d3/models/
   python manage.py drive --model=./models/ucsd_12oct17.h5
   ```
