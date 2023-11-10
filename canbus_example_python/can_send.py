import cantools
import can
import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'config/motohawk.dbc')


# Load the dbc file
db = cantools.database.load_file(filename)
example_message = db.get_message_by_name('ExampleMessage')

# Declare the can_bus class "can.interface.Bus('<interface_name>', bustype='socketcan')
with can.interface.Bus('can1', bustype='socketcan') as can_bus:
    
    # Use send() function & encode() can send message to canbus
    data = example_message.encode({'Temperature':258,'AverageRadius':3.12, 'Enable':1})
    message = can.Message(arbitration_id=example_message.frame_id, data=data)
    can_bus.send(message)
    print("send message: {'Temperature':258,'AverageRadius':3.12, 'Enable':1} ")