# Kafka programming with python

There are a lot of code define already in [this EDA reference project](https://ibm-cloud-architecture.github.io/refarch-kc)

## Basic consumer and producer

In the kafka folder I used a very simple setting to run kafka locally with docker compose and python environment.

[KafkaConsumer.py](https://github.com/jbcodeforce/python-code/blob/master/kafka/KafkaConsumer.py) is for just connecting to a brokers defined in env variables and use confluent_kafka library.

To run this consumer using local kafka, first start kafka and zookeeper using docker compose:

```shell
cd kafka
docker-compose up
```

```shell
docker rm Env1
./startPythonDocker.sh Env1
root@19d06f7d163e:/home# cd kafka/
root@19d06f7d163e:/home/kafka# python KafkaConsumer.py
```

The producer code [KafkaProducer.py](https://github.com/jbcodeforce/python-code/blob/master/kafka/KafkaProducer.py) is in separate program and run in a second container

```shell
docker rm Env2
./startPythonDocker.sh Env2 5001
root@44e827a5c2cc:/home# cd kafka/
root@44e827a5c2cc:/home/kafka# python KafkaProducer.py
```

### Using event streams on Cloud

Set the KAFKA_BROKERS to the brokers URL of the event streams instance. The setenv.sh is used for that:

```shell
root@44e827a5c2cc:/home/kafka# source ./setenv.sh IBMCLOUD
echo $KAFKA_BROKERS
python KafkaConsumer.py   
# or 
python KafkaProducer.py
```


## Faust

The other API is to use faust for streamings. To execute the first basic faust agent and producer code: [FaustEasiestApp.py](https://github.com/jbcodeforce/python-code/blob/master/kafka/FaustEasiestApp.py) do the following:

As previously start a docker container with python env

```shell
root@44e827a5c2cc:/home# pip install faust & cd kafka
root@44e827a5c2cc:/home/kafka# faust -A FaustEasiestApp worker -l info
```

