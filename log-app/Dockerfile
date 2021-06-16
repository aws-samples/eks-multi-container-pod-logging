FROM python:3.6-alpine

#Implementation of Layer Caching
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "app.py"]