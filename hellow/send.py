import pika



connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

body = input('message: ')

channel.basic_publish(exchange='', routing_key='hello', body=body)
connection.close()
