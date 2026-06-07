import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.queue_declare(queue="task_queue")

while True:
    task = input("Enter task: ")

    if task.lower() == "q":
        break

    channel.basic_publish(exchange="", routing_key="task_queue", body=task, properties=pika.BasicProperties(delivery_mode=2))  # Make message persistent
    print(f"Added task: {task}")

        
# with open("/mnt/c/Users/anowe/Desktop/practice topic/rebbitMQ/rabbitmq-task-system/tasks.txt", "r") as file:
#     tasks = file.readlines()

# for task in tasks:
#     task = task.strip()

    # channel.basic_publish(exchange="", routing_key="task_queue", body=task)
    # print(f"Sent task: {task}")

connection.close()


