FROM python:3.6.1-slim

MAINTAINER Joao Paulo Barraca

RUN pip install cherrypy
RUN pip install opencv-utils

CMD mkdir /app

COPY app.py /app/app.py

WORKDIR /app

EXPOSE 8080

# Finally
CMD ["python3", "app.py"]

