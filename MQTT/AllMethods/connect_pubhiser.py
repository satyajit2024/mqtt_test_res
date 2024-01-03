import paho.mqtt.client as mqtt

broker_address = "mqtt.eclipseprojects.io"
client = mqtt.Client("ConnectPublisher")

client.connect(broker_address)
print("Connected to broker")
client.disconnect()
print("Disconnected from broker")
