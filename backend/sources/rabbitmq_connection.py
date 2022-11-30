import pika
import logging
from backend_config import RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS


logger = logging.getLogger(__name__)


class RabbitMQ(object):
    __slots__ = ["connection", "channel"]

    def __init__(self):
        try:
            parameters = pika.URLParameters(f"amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@rabbitmq:5672/%2F")
            self.connection = pika.BlockingConnection(parameters=parameters)
            self.channel = self.connection.channel()
        except Exception as e:
            logger.error(e)

    def __enter__(self):
        return self.channel

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
