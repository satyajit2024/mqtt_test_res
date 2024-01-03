import paho.mqtt.client as mqtt
from random import randrange
import time

mqttBroker = "localhost"
client = mqtt.Client("Temprature_OutSide")
client.connect(mqttBroker)


i = 0
while i<11:
    randNumber = randrange(10)
    client.publish("TEMPERATURE",randNumber)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)
    i +=1
    