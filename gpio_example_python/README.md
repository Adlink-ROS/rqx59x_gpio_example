# GPIO controll example for RQX-59 series

RQX-59 series are embedded robotic controller powered by NVIDIA® Jetson AGX Orin ™ Module.

<img src="https://github.com/Jason-Lee0/controller_example/assets/56862464/40ff2e3c-6e1e-473c-aa6c-a81547dec9e2" height="200" width="300">

The platform provides multi-I/O DB-50 Connector comprehensive I/O for autonomous robotics via a DB-50 connector on the right side of the chassis.

# DB-50 connector pin table


<img src="https://github.com/Jason-Lee0/controller_example/assets/56862464/0ffa6ff3-b554-4376-a75e-b43f8968f743" height="600" width="400">



# Check GPIO status
You can check the status of GPIO with the following command.
```
sudo cat /sys/kernel/debug/gpio
```
![image](https://github.com/Jason-Lee0/controller_example/assets/56862464/9d999e57-3bba-4876-b642-db78a6143294)

You can see the chip name and the gpio name in the result. "out lo" means the gpio is on low status.


# Correspondence table (sysfs gpio & DB-50 gpio name)
The "gpio284/base_gpio0"  corresponds to GPIO 0 of the DB-50 connector located in Pin no.5.

<img src="https://github.com/Jason-Lee0/controller_example/assets/56862464/8085cd8b-1117-48a7-bfa0-e0c604eb35ad" height="400" width="400">

# Controll gpio with command
1. Open the bash terminal and set to root.
```
sudo su
```
2. Initialize the GPIO you want to use (for example: GPIO285).

```
echo 285 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio285/direction
```
3. Controll the gpio
```
#set gpio285 to high
echo 1 > /sys/class/gpio/gpio285/value
```

![image](https://github.com/Jason-Lee0/controller_example/assets/56862464/0be53e01-2d30-42e8-ac2f-31cf95f9160e)


4. Check the current status of gpio285.

```
sudo cat /sys/kernel/debug/gpio
```
![image](https://github.com/Jason-Lee0/controller_example/assets/56862464/8a1d7a88-5f80-440c-bc9d-76e597e92797)


5. Release the system controll of gpio285
```
echo 285 > /sys/class/gpio/unexport
```



# Controll gpio with code

1. Install the related package
(gpiod - https://pypi.org/project/gpiod/)

```
sudo pip install gpiod
```
2. Run the example code. (For example: Controll gpio285 on/off)

```
git clone https://github.com/Adlink-ROS/rqx59x_gpio_example
cd rqx59x_gpio_example/gpio_example
sudo python3 gpio.py
```

You can check out the function explaination in the code.

- Result
  
![image](https://github.com/Jason-Lee0/controller_example/assets/56862464/2a2a1238-767b-4761-9fde-d22a3a9936cf)



 












 

