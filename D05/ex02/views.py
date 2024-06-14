from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.

def init(request):
    try:
        conn = psycopg2.connect('dbname=mydb user=tahaexo password=secret host=localhost')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex02_movies(
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb SERIAL PRIMARY KEY,
                opening_crawl Text,
                director VARCHAR(32) NOT NULL,
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

def set_to_dict(p):
    dictionaries = []
    for elem in p :
        dictionary = {}
        spl = elem.split(' - ')
        for dic_elem in spl :
            dic_splited = dic_elem.split(':')
            dictionary[dic_splited[0].strip()] = dic_splited[1].strip()
        dictionaries.append(dictionary)
    return dictionaries
    
def Populate(request):
    raw_data = [
        'episode_nb: 1 - title: The Phantom Menace - director: George Lucas - producer: Rick McCallum - release_date: 1999-05-19',
        'episode_nb: 2 - title: Attack of the Clones - director: George Lucas - producer: Rick McCallum - release_date: 2002-05-16',
        'episode_nb: 3 - title: Revenge of the Sith - director: George Lucas - producer: Rick McCallum - release_date: 2005-05-19',
        'episode_nb: 4 - title: A New Hope - director: George Lucas - producer: Gary Kurtz, Rick McCallum - release_date: 1977-05-25',
        'episode_nb: 5 - title: The Empire Strikes Back - director: Irvin Kershner - producer: Gary Kurtz, Rick McCallum - release_date: 1980-05-17',
        'episode_nb: 6 - title: Return of the Jedi - director: Richard Marquand - producer: Howard G. Kazanjian, George Lucas, Rick McCallum - release_date: 1983-05-25',
        'episode_nb: 7 - title: The Force Awakens - director: J. J. Abrams - producer: Kathleen Kennedy, J. J. Abrams, Bryan Burk - release_date: 2015-12-11',
    ]
    dictionaries = set_to_dict(raw_data)

    sql = "INSERT INTO ex02_movies ({}) VALUES ({})".format(
    ', '.join(dictionaries[0].keys()),
    ', '.join(['%s'] * len(dictionaries[0]))
)
    try:
        conn = psycopg2.connect('dbname=mydb user=tahaexo password=secret host=localhost')
        cursor = conn.cursor()
        for data in dictionaries:
            cursor.execute(sql, list(data.values()))
            conn.commit()
        cursor.close()
        conn.close()
        return HttpResponse('Ok2')
    except Exception as e:
        return HttpResponse(f'{e}') 