# GPIO example
The repo will show how to use gpio (General Purpose Input Output) in command and code.

For now, the example code is written in python.

# Outline
- [Check GPIO status](https://github.com/Jason-Lee0/controller_example/blob/main/gpio_example_python/README.md#check-gpio-status
)
- [Use the command to control gpio](https://github.com/Jason-Lee0/controller_example/blob/main/gpio_example_python/README.md#use-the-command-to-control-gpio)
- [Run the code to controll gpio](https://github.com/Jason-Lee0/controller_example/blob/main/gpio_example_python/README.md#run-the-code-to-controll-gpio)

# Check GPIO status
You can check the status of GPIO in the following command.
```
sudo cat /sys/kernel/debug/gpio
```

The result contains the chip name which connected with your device and the io number in the chip. When the gpio status shows "out lo", it means the io was getting on low status. 

In the following tutorial, you will learn how to use the command to make the specific io stay on high status or not.

# Use the command to control gpio
It needs the authenticator to do this tutorial.
```
sudo su
```
Then you can use the terminal command to controll.

First, choose the gpio you want to controll and export it in sys gpio class. 
(Here I use gpio285 for example.) 

(Notice: If you use the gpio number which is not in the gpio table, it will show the warning log called write error: Invalid argument )

```
echo 285 > /sys/class/gpio/export
```

Second, change the direction and value.
(Notice : The <gpio*> path depends on the gpio number you called.)

```
echo out > /sys/class/gpio/gpio285/direction
echo 1 > /sys/class/gpio/gpio285/value
```

If it didn't show any error, then you could check the gpio status.

```
sudo cat /sys/kernel/debug/gpio
```
In the result, the status of gpio285 show "out hi". It means the gpio is on high status. (value:1)

```
 gpio-285 (base_gpio1          |sysfs               ) out hi 
```

You can also unexport the gpio if you want to release the controll of system.
```
echo 285 > /sys/class/gpio/unexport
```

Next section, We will use code to controll the gpio.

# Run the code to controll gpio
To run properly,it needs to install the related package.
(gpiod - https://pypi.org/project/gpiod/)

```
sudo pip install gpiod
```
After installing it, the repo provides the example code (./gpio.py) to run the specific gpio.
You can clone this "controll_example" package or just copy the python file to your another file.

```
#clone
git clone https://github.com/Jason-Lee0/controller_example
cd controller_example/gpio_example
sudo python3 gpio.py
```
Then,you will see the result below. You can also use the check command to check the gpio status.
```
initial value : 0

change state 0 -> 1
current value : 1
change state 1 -> 0
current value : 0
....
```
In the code, I controll the 1st gpio of gpiochip3. You can change the defined gpio.  The detail explaination is in the code.









 

