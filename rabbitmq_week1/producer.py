import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue="tasks")
# channel.queue_declare(queue="email_queue")

# METHOD 1
# channel.basic_publish(exchange='', routing_key='Hello', body='Hello World!')

# METHOD 2
# message = input("Enter message: ")
# channel.basic_publish(exchange='', routing_key='Hello', body=message)


# METHOD 3
for i in range(1, 10):
    message = f"Task {i}"
    channel.basic_publish(exchange='', routing_key='tasks', body=message)

    print(" Message Sent!", message)


# Real Example
# METHOD 4
# email = "anower@gmail.com"
# channel.basic_publish(exchange='', routing_key='email_queue', body=email)





connection.close()


