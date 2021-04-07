import paho.mqtt.client as mqtt
from random import uniform
import time
import os

mqtt_publisher_id = os.getenv('MQTT_PUB_ID')
mqttBroker = os.getenv('MQTT_BROKER_HOST')
port = os.getenv('MQTT_BROKER_PORT')

if not str(port):
    port = 1883
else:
    port = int(port)

def on_publish(client,userdata,result):             #create function for callback
    #print("data published \n")
    pass

client = mqtt.Client("Temperature"+str(mqtt_publisher_id))
client.on_publish = on_publish
client.connect(mqttBroker,port=port)

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Publisher"+str(mqtt_publisher_id)+": Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)