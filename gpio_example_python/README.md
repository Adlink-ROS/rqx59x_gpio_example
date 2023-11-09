# GPIO example
The repo would show how to use gpio (General Purpose Input Output) in command and code.

For now, the example code was written in python.

# Outline
- [Check GPIO status](https://github.com/Jason-Lee0/controller_example/blob/main/gpio_example_python/README.md#check-gpio-status
)
- [Use the command to control gpio](https://github.com/Jason-Lee0/controller_example/blob/main/gpio_example_python/README.md#use-the-command-to-control-gpio)
- [Run the code to controll gpio](https://github.com/Jason-Lee0/controller_example/blob/main/gpio_example_python/README.md#run-the-code-to-controll-gpio)

# Check GPIO status
You could check the status of GPIO in the following command.
```
sudo cat /sys/kernel/debug/gpio
```

The result contained the chip name which connected with your device and the io number in the chip. When the gpio status showed "out lo", it mean the io was getting on low status. 

In the following tutorial, you would learn how to use the command to make the specific io stay on high status or not.

# Use the command to control gpio
It need the authenticator to do this tutorial.
```
sudo su
```
Then you could use the terminal command to controll.

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

You could also unexport the gpio if you want to release the controll of system.
```
echo 285 > /sys/class/gpio/unexport
```

Next section, We will use code to controll the gpio.

# Run the code to controll gpio










 

