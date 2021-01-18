import app2

from kafka import KafkaProducer
import json, time

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

try:
    producer = KafkaProducer(bootstrap_servers=['14.52.135.36:29092'],
                             value_serializer=json_serializer)
except Exception as e:
    print('An error has occured when making producer.')


while(True):
    r = app2.run_task()
    # pub to kafka
    try:
        producer.send("hello", "{'hello':'py2'}")
    except Exception as e:
        print('An error has occured.')
    time.sleep(0.5)


