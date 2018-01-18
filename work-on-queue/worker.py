import pika
import random


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare('task_queue', durable=True)


def callback(ch, method, properties, body):
    print('Starting Task#', body)
    l = [random.random() for i in range(2000000)]
    l.sort()
    print('Task#', body, ' Done')
    # we are sending manual acknowledgement that the task is done
    ch.basic_ack(delivery_tag=method.delivery_tag)

"""by using no_ack we are telling that not manual acknowledgement needed"""
#channel.basic_consume(callback, queue='task_queue', no_ack=True)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='task_queue')
channel.start_consuming()

connection.close()
