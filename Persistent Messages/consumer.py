import pika
import time
import os


# Connect to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

# Create the same durable queue
channel.queue_declare(
    queue="persistent_task_queue",
    durable=True
)


# Process one message at a time
channel.basic_qos(
    prefetch_count=1
)

worker_id = os.getenv("WORKER_ID", "1")
print(f"Worker {worker_id} is ready to process tasks.")


def process_task(ch, method, properties, body):
    task = body.decode()

    print(f"\nProcessing: {task}")

    # Simulate work
    time.sleep(5)

    print(f"Completed: {task}")

    # Acknowledge message
    ch.basic_ack(
        delivery_tag=method.delivery_tag
    )

# Start consuming
channel.basic_consume(
    queue="persistent_task_queue",
    on_message_callback=process_task
)

print("Worker started")
print("Waiting for tasks...\n")

channel.start_consuming()