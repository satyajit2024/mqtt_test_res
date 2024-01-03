import paho.mqtt.client as mqtt
import time

broker_address = "mqtt.eclipseprojects.io"
topic = "test/topic"
client = mqtt.Client("UnsubscribeSubscriber")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

client.on_message = on_message

client.connect(broker_address)
client.subscribe(topic)
time.sleep(2)  # Wait for subscription to take effect

# Unsubscribe after receiving a message
client.unsubscribe(topic)
print(f"Unsubscribed from {topic}")

# Keep the script running to allow time for the unsubscribe action
client.loop_forever()
