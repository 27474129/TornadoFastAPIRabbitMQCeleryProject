import psycopg2
import logging
from servicedb_config import DB_NAME, DB_USERNAME, DB_PASSWORD

logger = logging.getLogger(__name__)


# контекстный менеджер для открытия конектов с бд, чтобы не использовать try except
class Postgresql(object):
    __slots__ = ["connection"]

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                f"dbname={DB_NAME} user={DB_USERNAME} password={DB_PASSWORD} host=postgres"
            )
            logger.debug("Соединение с БД установленно")
        except Exception as e:
            logger.error(e)

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        logger.debug("Соединение с БД закрыто")
