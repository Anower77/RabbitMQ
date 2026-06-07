import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.queue_declare(queue="task_queue")

def callback(ch, method, properties, body):
    task = body.decode()
    print(f"\n Processing task: {task}")
    time.sleep(1)                                           # Simulate work by sleeping for 2 seconds
    print(f"Completed task: {task}")
    ch.basic_ack(delivery_tag=method.delivery_tag)          # Acknowledge the message after processing

channel.basic_consume(queue="task_queue", on_message_callback=callback, auto_ack=False)


print("Worker started...")
print("Waiting for tasks...\n")

channel.start_consuming()

