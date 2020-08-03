from pycoingecko import CoinGeckoAPI
import os, json, crython
from paho.mqtt import publish

print("started")
topic = os.environ.get('MQTT_TOPIC')
host = os.environ.get('MQTT_HOST')
port = os.environ.get('MQTT_PORT')

currencies = os.environ.get('CURRENCIES')
vs_currencies = os.environ.get('VS_CURRENCIES')

schedule = os.getenv('SCHEDULE')

@crython.job(expr=schedule)
def process():
    cg = CoinGeckoAPI()
    data = cg.get_price(ids=currencies, vs_currencies=vs_currencies)
    jsonString = json.dumps(data)
    print(jsonString)
    publish.single(topic, jsonString, hostname=host, port=port)


if __name__ == "__main__":
    if schedule is None:
        process()
    else:
        crython.start()
        crython.join()
