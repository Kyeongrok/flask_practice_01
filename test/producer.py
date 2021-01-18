from kafka import KafkaProducer
import json, time

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['14.52.135.36:29092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        producer.send("hello", "{'hello':'py'}")
        time.sleep(3)