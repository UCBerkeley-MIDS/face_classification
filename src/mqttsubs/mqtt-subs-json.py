import paho.mqtt.client as paho

def on_message(mosq, obj, msg):
    print ("{} {} {}".format(msg.topic, msg.qos, msg.payload))
    mosq.publish('pong', 'ack', 0)

def on_publish(mosq, obj, mid):
    pass

if __name__ == '__main__':
    client = paho.Client()
    
    client.on_message = on_message
    client.on_publish = on_publish

    client.connect("50.23.173.22", 1883, 60)

    client.subscribe("fc_json_mqtt", 0)

    while client.loop() == 0:
        pass