# README
Aaron Cao

## deps

### python packages
pip install -U Celery  # the message queue service/client for node to rpcs
pip install raftos # the consensus protocol for distri KV to simulation
pip install snakemq # replace Celery/RabbitMQ


### system envs
Erlang [Win](http://www.erlang.org/downloads) # for RabbitMQ runtime
RabbitMQ [Win](https://www.rabbitmq.com/install-windows.html) # for Celery backends
