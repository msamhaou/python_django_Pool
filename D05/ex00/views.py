from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
# Create your views here.

def init(request):
    try:
        conn = psycopg2.connect('dbname=mydb user=tahaexo password=secret host=localhost')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex00_movies(
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb SERIAL PRIMARY KEY,
                opening_crawl Text,
                directory VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );
        """)
        conn.commit();
        cursor.close()
        conn.close();
        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(f'{e}')
    