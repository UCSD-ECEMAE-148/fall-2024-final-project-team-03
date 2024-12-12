#for resetting GPS
python3.10 bin/config_tool.py reset factory
python3.10 bin/config_tool.py apply uart2_message_rate nmea gga on
python3.10 bin/config_tool.py save

python3.10 bin/runner.py --device-id Ghhiex3O --polaris keH10zzC --device-port /dev/ttyUSB0
#or
python3.10 bin/runner.py --device-id Ghhiex3O --polaris keH10zzC --device-port /dev/ttyUSB1


#GPIO settings for donkeycar
sudo usermod -aG gpio $USER
sudo chown root.gpio /dev/gpiochip1
sudo chmod 660 /dev/gpiochip1
sudo chmod 660 /dev/gpiochip0
sudo chown root.gpio /dev/gpiochip0