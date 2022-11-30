import requests
from multiprocessing import Process


def execute_consuming():
    requests.get("http://servicedb:8000")


process = Process(target=execute_consuming)
process.start()
