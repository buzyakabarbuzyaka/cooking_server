FROM python:3.8
COPY requirements.txt /
RUN pip install -r requirements.txt

RUN mkdir app
COPY main.py /app

CMD python3 /app/main.py