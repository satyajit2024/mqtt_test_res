import paho.mqtt.client as mqtt
import time

broker_address = "mqtt.eclipseprojects.io"
client = mqtt.Client("ConnectSubscriber")

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def on_disconnect(client, userdata, rc):
    print(f"Disconnected with result code {rc}")

client.on_connect = on_connect
client.on_disconnect = on_disconnect

client.connect(broker_address)
client.loop_start()
time.sleep(2)  # Wait for the connection to be established
client.disconnect()
