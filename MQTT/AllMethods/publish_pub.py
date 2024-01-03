import paho.mqtt.client as mqtt
import time

broker_address = "mqtt.eclipseprojects.io"
topic = "test/topic"
client = mqtt.Client("PublishPublisher")

client.connect(broker_address)

for i in range(5):
    message = f"Hello, this is message {i+1}"
    client.publish(topic, message)
    print(f"Published: {message}")
    time.sleep(1)

client.disconnect()
