import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def receive(ch, method, properties, body):
    print(body)


channel.basic_consume(receive, queue='hello', no_ack=True)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
