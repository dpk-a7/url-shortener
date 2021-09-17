FROM python:3.8-slim-buster
RUN pip install psycopg2-binary>=2.8.3
RUN pip install schedule

COPY . /opt/
WORKDIR /opt

CMD ["python", "db_manager.py"]