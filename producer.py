from kafka import KafkaProducer
import random

topic = 'MEUTOPICO'

bootstrap_servers = 'localhost:9092'

#É a url de um dos brokers Kafka que você fornece para buscar os metadados iniciais sobre seu cluster Kafka. Os metadados consistem nos tópicos, suas partições, os corretores líderes para essas partições, etc. Dependendo desses metadados, seu produtor ou consumidor produz ou consome os dados.
#Você pode ter vários servidores de bootstrap em sua configuração de produtor ou consumidor. De forma que, se um dos corretores não estiver acessível, ele volta para outro.
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

particao =producer.partitions_for('MEUTOPICO')
#produz um numero aleatório e armazena na variável aleatório
aleatorio = random.randint(500, 50000)
#minha msg kafka f é um template string sintax python
msg = f'test:{aleatorio}'
#https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html
#SEND
future = producer.send(topic, msg.encode('utf-8'))
#no console imprime a mensagem
print(f'Enviando Mensagem: {msg}')
result = future.get(timeout=60)

#mostra as metricas do produtor
#https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html
metrics = producer.metrics()

#printa as metricas do produtor no console/prompt
############print(f'METRICAS: \n {metrics}, \n PARTICAO {particao}')