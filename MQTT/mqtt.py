import paho.mqtt.client as mqtt
from random import uniform , randrange
import time
import threading


class ThreadNew:

    def insidPub(self):
        mqttBroker = "localhost"
        client = mqtt.Client("Temprature_Inside")
        client.connect(mqttBroker)

        i = 0

        while i<11:
            randNumber = uniform(20.0,21.0)
            client.publish("TEMPERATURE",randNumber)
            # print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
            time.sleep(1)
            i +=1


    def outSidePub(self):
        mqttBroker = "localhost"
        client = mqtt.Client("Temprature_OutSide")
        client.connect(mqttBroker)


        i = 0
        while i<11:
            randNumber = randrange(10)
            client.publish("TEMPERATURE",randNumber)
            # print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
            time.sleep(1)
            i +=1


    def Sub(self):
        def on_message(client ,userdata , message):
            print("Recived message: " , str(message.payload.decode()))


        mqttBroker = "localhost"
        client = mqtt.Client("SmartPhone")
        client.connect(mqttBroker)

        client.loop_start()
        client.subscribe("TEMPERATURE")
         
        client.on_message = on_message

        time.sleep(11)
        client.loop_stop()



s1 = ThreadNew()

if __name__ == '__main__':
    t1 = threading.Thread(target=s1.Sub)
    t2 = threading.Thread(target=s1.insidPub)
    t3 = threading.Thread(target=s1.outSidePub)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("| Done |")