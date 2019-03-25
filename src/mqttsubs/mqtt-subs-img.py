import paho.mqtt.client as paho
import base64
import io
import cv2
from imageio import imread
    
def on_message(mosq, obj, msg):
    print ("{} {} {}".format(msg.topic, msg.qos, msg.payload))
    
   # reconstruct_image(msg.payload)
    img = imread(io.BytesIO(base64.b64decode(msg.payload)))
    cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite("image.jpg", cv2_img)
    mosq.publish('pong', 'ack', 0)

def on_publish(mosq, obj, mid):
    pass

if __name__ == '__main__':
    client = paho.Client()

    client.on_message = on_message
    client.on_publish = on_publish
    
    #client.connect("iot.eclipse.org", 1883, 60)
    client.connect("50.23.173.22", 1883, 60)

    client.subscribe("fc_img_mqtt", 0)

    while client.loop() == 0:
        pass
