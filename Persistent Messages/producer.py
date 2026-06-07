import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

# Create a durable queue
channel.queue_declare(
    queue="persistent_task_queue",
    durable=True
)

# Send 10 persistent messages
for i in range(1, 11):
    task = f"Task {i}"

    channel.basic_publish(
        exchange="",
        routing_key="persistent_task_queue",
        body=task,
        properties=pika.BasicProperties(
            delivery_mode=2  # Make message persistent
        )
    )

    print(f"Sent: {task}")

print("\nAll tasks sent successfully!")

connection.close()