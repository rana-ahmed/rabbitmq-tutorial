import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue')

message = ''.join(sys.argv[1:]) or 'Hello World'

for i in range(100):
    channel.basic_publish(
	    exchange='',
	    routing_key='task_queue',
	    body="#Task "+str(i),
	    properties=pika.BasicProperties(
		delivery_mode=2
	    )
    )

#message = ''.join(sys.argv[1:]) or 'hello world'
