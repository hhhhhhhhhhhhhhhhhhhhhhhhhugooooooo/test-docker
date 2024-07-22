FROM python:3.8

RUN apt-get update && apt-get install -y openssh-client\
    python3-pip

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]