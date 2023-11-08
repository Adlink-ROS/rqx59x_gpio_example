import cantools
import can

# Load the dbc file
db = cantools.database.load_file('config/motohawk.dbc')
example_message = db.get_message_by_name('ExampleMessage')

# Declare the can_bus class "can.interface.Bus('<interface_name>', bustype='socketcan')
can_bus = can.interface.Bus('can1', bustype='socketcan')

# Use send() function & encode() can send message to canbus
data = example_message.encode({'Temperature':258,'AverageRadius':3.2, 'Enable':1})
message = can.Message(arbitration_id=example_message.frame_id, data=data)
can_bus.send(message)


# Use recv() function & decode() can receive the message from canbus.
message = can_bus.recv()
print(db.decode_message(message.arbitration_id, message.data))
