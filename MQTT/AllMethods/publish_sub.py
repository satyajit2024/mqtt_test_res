import paho.mqtt.client as mqtt

broker_address = "mqtt.eclipseprojects.io"
topic = "test/topic"
client = mqtt.Client("SubscribeSubscriber")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

client.on_message = on_message

client.connect(broker_address)
client.subscribe(topic)
client.loop_forever()
