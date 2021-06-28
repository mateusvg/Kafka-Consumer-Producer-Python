from kafka import KafkaConsumer

#nome do topico para consumir a mensagem
topic = 'MEUTOPICO'

bootstrap_servers = 'localhost:9092'

#https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html
#opção offset EARLIEST é adicionado para recuperar eventos desde o início.
consumer = KafkaConsumer(
    topic, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest')
#verifica a conexao com o kafka
conexao = consumer.bootstrap_connected()

for msg in consumer:
    #retire este comentario abaixo e no prompt/console do consumidor vc verá a mensagem seguido dos propriedades do kafka
    #########print(msg, conexao)

    #Para imprimir os valores diretamente, só precisamos usar a propriedade value
    print(msg.value.decode("utf-8"),conexao)