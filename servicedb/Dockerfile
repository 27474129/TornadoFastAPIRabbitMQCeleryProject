FROM python:latest

ENV PYTHONUNBUFFERED=1

RUN mkdir /servicedb
WORKDIR /servicedb
COPY . /servicedb/
RUN cd /servicedb/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


CMD ["uvicorn", "app:app", "--reload", "--host", "servicedb", "--port", "8000"]
CMD ["python3", "consumer.py"]