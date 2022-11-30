import json
from celery import Celery
from servicedb_config import RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS
from sources.rabbitmq_connection import RabbitMQ
from sources.postgresql_connection import Postgresql


app = Celery("chat", broker=f"amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@rabbitmq:5672/%2F")
app.autodiscover_tasks()


def callback(channel, method, properties, body):
    with Postgresql() as connection:
        body = json.loads(body)
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO appeals (surname, name, patronymic, phone, appeal_text)\
         VALUES ('{body.get('surname')}', '{body.get('name')}',\
          '{body.get('patronymic')}', {body.get('phone')}, '{body.get('appeal_text')}');")


@app.task
def consuming():
    with RabbitMQ() as channel:
        channel.queue_declare(queue="appeals")
        channel.basic_consume(on_message_callback=callback, queue="appeals")
        try:
            channel.start_consuming()
        except Exception as e:
            ...
        finally:
            channel.stop_consuming()
