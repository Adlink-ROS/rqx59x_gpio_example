# GPIO controll example for RQX-59 series

RQX-59 series are embedded robotic controller powered by NVIDIA® Jetson AGX Orin ™ Module.
![computer.png](https://hackmd.io/_uploads/S1AMVAYXT.png)

The platform provides multi-I/O DB-50 Connector comprehensive I/O for autonomous robotics via a DB-50 connector on the right side of the chassis.

# DB-50 connector pin table

![DB50 intro.PNG](https://hackmd.io/_uploads/S1tVuRYma.png)
![pin difination.PNG](https://hackmd.io/_uploads/BJFau0Fmp.png)




# Check GPIO status
You could check the status of GPIO in the following command.
```
sudo cat /sys/kernel/debug/gpio
```
![image](https://github.com/Jason-Lee0/controller_example/assets/56862464/a8f0ca3f-1dad-456c-8aff-2143ccd9ab13)


You can see the chip name and the gpio name in the result. "out lo" means the gpio is on low status.

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
git clone https://github.com/Jason-Lee0/controller_example
cd controller_example/gpio_example
sudo python3 gpio.py
```

You can check out the function explaination in the code.

- Result
![image](https://github.com/Jason-Lee0/controller_example/assets/56862464/2a2a1238-767b-4761-9fde-d22a3a9936cf)



 












 

