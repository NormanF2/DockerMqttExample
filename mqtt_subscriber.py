import paho.mqtt.client as mqtt
import time
import logging
import logging.handlers
import sys

logger = logging.getLogger() 
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.WARN)

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)


def on_subscribe(client, userdata, mid, granted_qos):
    logger.warning("subscribed")


mqttBroker = "127.0.0.1"
#mqttBroker = 'localhost'
port=1883
client = mqtt.Client("asdrubale", True, None, mqtt.MQTTv31)


client.on_message=on_message
client.on_connect=on_connect
client.connect('127.0.0.1',1883,keepalive=10)
client.subscribe("TEMPERATURE")
client.loop_forever()