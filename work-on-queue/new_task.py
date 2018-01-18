import sys
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
#channel.queue_declare(queue='task_queue')
"""create durable queue"""
channel.queue_declare(queue='task_queue', durable=True)

message = ''.join(sys.argv[1:]) or 'Hello World'

for i in range(100):
    print('Generating Task# ', i)
    channel.basic_publish(
        exchange='',
	    routing_key='task_queue',
	    body="#Task "+str(i),
	    properties=pika.BasicProperties(
	       delivery_mode=2
        )
    )

connection.close()
#message = ''.join(sys.argv[1:]) or 'hello world'
