import cantools
import can
import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'config/motohawk.dbc')


# Load the dbc file
db = cantools.database.load_file(filename)


# Declare the can_bus class "can.interface.Bus('<interface_name>', bustype='socketcan')

with can.interface.Bus('can0', bustype='socketcan') as can_bus:

# Use recv() function & decode() can receive the message from canbus.
    message = can_bus.recv()
    print(db.decode_message(message.arbitration_id, message.data))
