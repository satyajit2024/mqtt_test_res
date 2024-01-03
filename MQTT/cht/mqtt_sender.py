import paho.mqtt.client as mqtt
import time

# Define the MQTT broker and topic
broker_address = "mqtt.eclipseprojects.io"
topic = "test/topic"

# Create a MQTT client
client = mqtt.Client("Publisher")

# Connect to the broker
client.connect(broker_address)

# Publish a message every second
for i in range(5):
    message = f"Hello, this is message {i+1}"
    client.publish(topic, message)
    print(f"Published: {message}")
    time.sleep(1)

# Disconnect from the broker
client.disconnect()
