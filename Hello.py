from MQTT.mqtt import ThreadNew
import threading


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

