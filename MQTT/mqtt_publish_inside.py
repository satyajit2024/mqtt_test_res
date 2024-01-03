import paho.mqtt.client as mqtt
from random import uniform
import time


mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temprature_Inside")
client.connect(mqttBroker)

i = 0

while i<11:
    randNumber = uniform(20.0,21.0)
    client.publish("TEMPERATURE",randNumber)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)
    i +=1
