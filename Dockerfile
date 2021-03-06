FROM python:3.8
WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt

ADD app /app

CMD python3 -m app.main