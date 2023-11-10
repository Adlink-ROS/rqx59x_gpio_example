# CANBUS controll example of RQX-59 series

RQX-59 series are embedded robotic controller powered by NVIDIA® Jetson AGX Orin ™ Module.

<img src="https://github.com/Jason-Lee0/controller_example/assets/56862464/40ff2e3c-6e1e-473c-aa6c-a81547dec9e2" height="200" width="300">

The platform provides multi-I/O DB-50 Connector comprehensive I/O for autonomous robotics via a DB-50 connector on the right side of the chassis.

# DB-50 connector pin table


<img src="https://github.com/Jason-Lee0/controller_example/assets/56862464/0ffa6ff3-b554-4376-a75e-b43f8968f743" height="600" width="400">

# Setup CAN driver interface
1. Check if can0 and can1 exist. (If exist, you can skip the setup.)
```
ifconfig
```
2. Check if can drivers (mttcan, can_dev) have been loaded
```
lsmod | grep can
```
![image](https://github.com/Jason-Lee0/controller_example/assets/56862464/f2bae98c-d0c5-4df1-a2ac-13630bc206b7)

3.  initialize can0 and can1
```
sudo ip link set can0 type can bitrate 500000 
sudo ip link set can0 up
sudo ip link set can1 type can bitrate 500000 
sudo ip link set can1 up
```

4. Use "ifconfig" to ensure can0 and can1 exist. 
```
ifconfig
```
![image](https://github.com/Jason-Lee0/controller_example/assets/56862464/b1082010-1d5f-42a7-8238-86b2c447965d)

# Check Can interface status

- Use "ip link show" to know the can status.

```
ip -detail link show can0
```
![image](https://github.com/Jason-Lee0/controller_example/assets/56862464/ce35ca6d-8866-4485-bc45-7e607156f512)

ERROR-ACTIVE is the normal state. If occur error, it will show ERROR-PASSIVE/ BUS-OFF .

- Use "dmesg" to check the setup info of can device.
```
sudo dmesg
```
![image](https://github.com/Jason-Lee0/controller_example/assets/56862464/5ae78b1e-805a-4838-8419-917a238b2c78)

# Test CANBUS with command 
(Reference : https://sgframework.readthedocs.io/en/latest/cantutorial.html)

1. Install the related package 
(can-utils - https://github.com/linux-can/can-utils )
```
sudo apt-get install can-utils
```

2. If you didn't connect any devices, you can connect can0 & can1 with cables for test. 
( can0-H <-> can1-H ,  can0-L <-> can1-L )


<img src="https://github.com/Jason-Lee0/controller_example/assets/56862464/f75de317-f13f-4cab-9dbe-b94e30976f87" height="200" width ="400">


3. Use candump  to print all data that is being received by a CAN interface.
```
#candump <can_interface>
candump can0
```
4. Open a new terminal and send a CAN frame with identifier 0x1A (26 dec) and 8 bytes of data

```
cansend can1 01a#11223344AABBCCDD
```
This will appear in the previous terminal window which is running candump


![image](https://github.com/Jason-Lee0/controller_example/assets/56862464/e005f007-8510-4d46-9411-c41bbbc62622)

If you want to learn more details, you can refer to the above reference link.

# Use CANBUS with code
(Reference : https://cantools.readthedocs.io/en/latest/)

1. Install the related package 
(can_tool - https://pypi.org/project/cantools/)

```
pip install can-tools
```

2. Start the receive script (can_recv.py) in terminal 1 :

The receive script shows how to load the dbc file and receive the message from can_interface.  

```
git clone https://github.com/Jason-Lee0/controller_example
cd controller_example/canbus_example_python
python3 can_recv.py
```

3. Open a second terminal and start the send script (can_send.py):
   
The send script shows how to load the dbc file and send the message to can_interface.

```
python3 can_send.py
```


- Result :
The message will appear in the terminal 1 which is running the receive script.

![image](https://github.com/Jason-Lee0/controller_example/assets/56862464/61825f65-9ae3-4817-9fba-149ee65ec897)

You can see more examples on this [examples link](https://github.com/cantools/cantools/tree/master/examples). 


