import gpiod
import time

#Choose Specify chip
#open by chip number = gpiod.chip("<chip_number>", gpiod.chip.OPEN_BY_NUMBER)
chip = gpiod.chip("gpiochip3", gpiod.chip.OPEN_BY_NAME)

#get the gpio  with n-index of chip - chip.get_line(n) 
#For example : GPIO285 (base_gpio1)
io = chip.get_line(1)

#set the request config
config = gpiod.line_request()
config.consumer = "test"
config.request_type = gpiod.line_request.DIRECTION_OUTPUT

#request_type : 
#(1) gpiod.line_request.DIRECTION_OUTPUT
#(2) gpiod.line_request.DIRECTION_INPUT
#(3) gpiod.line_request.DIRECTION_AS_IS
#(4) gpiod.line_request.EVENT_FALLING_EDGE
#(5) gpiod.line_request.EVENT_RISING_EDGE
#(6) gpiod.line_request.EVENT_BOTH_EDGES

#set the request config to gpio 
io.request(config)


print("initial value : {}\n".format(io.get_value()))
last_state = io.get_value()

try:
    
    while True:
        new_state = 1 - last_state
        print("changing state: {} -> {}".format(last_state,new_state))
        io.set_value(new_state)
        time.sleep(1)
        
        print("current value : {}\n".format(io.get_value()))
        last_state = new_state
        
except KeyboardInterrupt:
    pass
    
finally:
    io.release()
    
