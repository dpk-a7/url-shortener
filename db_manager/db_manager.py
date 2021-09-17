#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras as exts
from datetime import date
import time
import schedule
import os

conn = psycopg2.connect(dbname=os.environ.get('DB_NAME'),
                        user=os.environ.get('DB_USER'),
                        password=os.environ.get('DB_PASS'),
                        host=os.environ.get('DB_HOST'),
                        port=5432)


def get_data():
    with conn:
        with conn.cursor(cursor_factory=exts.DictCursor) as csr:
            try:
                csr.execute("SELECT * FROM shortener_api_app_req_urls;")
                resp = csr.fetchall()
                return resp
            except Exception as e:
                return str(e)


def delete_rec(id: int) -> str:
    with conn:
        with conn.cursor(cursor_factory=exts.DictCursor) as csr:
            try:
                csr.execute(f"DELETE FROM shortener_api_app_req_urls WHERE id = {id};")
            except Exception as e:
                pass


def run():
    for i in range(len(get_data())):
        today = date.today()
        db_date = get_data()[i][-1].date()
        x = today - db_date
        if x.days > 1:
            delete_rec(get_data()[i][0])


if __name__ == '__main__':
    schedule.every().sunday.at("01:00").do(run, "Its 01:00")
    while True:
        schedule.run_pending()
        time.sleep(60)
