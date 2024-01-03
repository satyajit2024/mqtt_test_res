import paho.mqtt.client as mqtt
import time

broker_address = "localhost"
topic = "test/topic"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, 1883, 60)
client.loop_start()

# Publish a message every second
for i in range(5):
    message = f"Hello, this is message {i+1}"
    client.publish(topic, message)
    print(f"Published: {message}")
    time.sleep(1)

# Disconnect from the broker
client.disconnect()
