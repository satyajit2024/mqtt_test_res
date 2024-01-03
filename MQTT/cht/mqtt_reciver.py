import paho.mqtt.client as mqtt

# Define the MQTT broker and topic
broker_address = "mqtt.eclipseprojects.io"
topic = "test/topic"

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

# Create a MQTT client
client = mqtt.Client("Subscriber")

# Attach the on_message callback function
client.on_message = on_message

# Connect to the broker
client.connect(broker_address)

# Subscribe to the topic
client.subscribe(topic)

# Loop to listen for messages
client.loop_forever()
