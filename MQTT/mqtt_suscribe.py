import paho.mqtt.client as mqtt
import time



def on_message(client ,userdata , message):
    print("Recived message: " , str(message.payload.decode()))


mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("SmartPhone")
client.connect(mqttBroker)


client.loop_start()
client.subscribe("TEMPERATURE")

client.on_message = on_message

time.sleep(30)
client.loop_stop()
