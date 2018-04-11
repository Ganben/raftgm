# README
Aaron Cao

## deps

### python packages

pip install -U Celery  # the message queue service/client for node to 

pip install raftos # the consensus protocol for distri KV to 

pip install snakemq # replace Celery/RabbitMQ [DOC](http://www.snakemq.net)

pip install paho-mqtt # another mq solution

pip install hbmqtt # another mq/mqtt client/broker solution

### system envs

Erlang [Win](http://www.erlang.org/downloads) # for RabbitMQ runtime

RabbitMQ [Win](https://www.rabbitmq.com/install-windows.html) # for Celery backends

MQTT:Mosquitto: [Ubuntu] https://mosquitto.org/download/ ```https://mosquitto.org/download/ ``` apt install mosquitto