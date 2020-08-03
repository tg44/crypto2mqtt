[![Docker Build Status](https://img.shields.io/docker/cloud/build/tg44/crypto2mqtt?style=flat-square)](https://hub.docker.com/r/tg44/crypto2mqtt)

# Crypto2MQTT

Gets crypto data from [CoinGecko](https://www.coingecko.com/) and publishes to MQTT.

### Docker
```
docker run \
-it \
-e MQTT_HOST=example.com \
-e MQTT_PORT=1883 \
-e MQTT_TOPIC=crypto/stats \
-e CURRENCIES=bitcoin,ethereum \
-e VS_CURRENCIES=usd \
-e SCHEDULE=@minutely \
tg44/crypto2mqtt
```
Currency list; https://api.coingecko.com/api/v3/coins/list (HUGE list, Firefox will parse it for you and you can filter in it)

vs_currency lise; https://api.coingecko.com/api/v3/simple/supported_vs_currencies (smaller list)

You can use both currencies and vs_currencies as a coma separated list!

SCHEDULE is an optional setting to schedule with [crython](https://github.com/ahawker/crython) expression.
