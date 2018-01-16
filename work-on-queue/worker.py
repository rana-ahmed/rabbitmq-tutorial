import time
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare('task_queue')


def callback(ch, method, properties, body):
    print('The body', body)
    time.sleep(5)
    print(body, ' task done')

channel.basic_consume(callback, queue='task_queue', no_ack=True)
channel.start_consuming()
