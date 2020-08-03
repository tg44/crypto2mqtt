from pycoingecko import CoinGeckoAPI
import os, json, crython, traceback
from paho.mqtt import publish

print("started")
topic = os.environ.get('MQTT_TOPIC')
host = os.environ.get('MQTT_HOST')
port = int(os.getenv('MQTT_PORT', '1883'))

currencies = os.environ.get('CURRENCIES')
vs_currencies = os.environ.get('VS_CURRENCIES')

schedule = os.getenv('SCHEDULE')
cg = CoinGeckoAPI()

@crython.job(expr=schedule)
def process():
    try:
        data = cg.get_price(ids=currencies, vs_currencies=vs_currencies)
        jsonString = json.dumps(data)
        print(jsonString)
        publish.single(topic, jsonString, hostname=host, port=port)
    except Exception as e:
        print("Unknown error:" + str(e))
        traceback.print_exc()


if __name__ == "__main__":
    if schedule is None:
        process()
    else:
        crython.start()
        crython.join()
