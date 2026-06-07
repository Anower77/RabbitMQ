import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue="tasks")
# channel.queue_declare(queue="email_queue")

def callback(ch, method, properties, body):
    # email = body.decode()
    print(" Processing task: ", body.decode())

channel.basic_consume(queue='tasks', on_message_callback=callback, auto_ack=True)

print(' Waiting for messages....')

channel.start_consuming()



