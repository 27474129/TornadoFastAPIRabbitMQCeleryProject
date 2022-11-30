"""
    Первый раз на торнадо писал...
"""
import asyncio
import json
import tornado.web
import logging
from sources.rabbitmq_connection import RabbitMQ


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        body = self.request.body_arguments
        # Валидацию параметров тела запроса я не сделал т.к. это тестовое задание, ее можно реализовать к примеру с pydantic
        appeal = {
            "surname": body.get("surname", None)[0].decode("utf-8"),
            "name": body.get("name", None)[0].decode("utf-8"),
            "patronymic": body.get("patronymic", None)[0].decode("utf-8"),
            "phone": body.get("phone", None)[0].decode("utf-8"),
            "appeal_text": body.get("appeal_text", None)[0].decode("utf-8")
        }

        with RabbitMQ() as channel:
            channel.queue_declare(queue="appeals")
            channel.basic_publish(
                exchange="",
                routing_key="appeals",
                body=json.dumps(appeal)
            )

        self.write({"success": True})


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
