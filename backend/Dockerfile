FROM python:latest

ENV PYTHONUNBUFFERED=1

RUN mkdir /backend
WORKDIR /backend
COPY . /backend/
RUN cd /backend/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
