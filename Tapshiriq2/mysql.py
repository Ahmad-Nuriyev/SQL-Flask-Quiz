import pymysql
import requests
from datetime import datetime

connection = pymysql.connect(
    host = "127.0.0.1",
    user = 'root',
    password = '1234',
    db = 'Testing',
    port = 3306,
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)


# def create_table():
#     with connection:
#         with connection.cursor() as cursor:
#             sql = """ create table if not exists Testing.Movie_info(
#                         id int auto_increment primary key,
#                         title varchar(50) not null,
#                         released date not null,
#                         director varchar(100) not null,
#                         genre varchar(50)
#                         );"""
#             cursor.execute(sql)
#         connection.commit()

# create_table()


extract = requests.get ('https://www.omdbapi.com/?t=Inception&apikey=5d9df2b8')
data = extract.json()


title = data.get('Title')
released_str = data.get('Released')
director = data.get('Director')
genre = data.get('Genre')

released_str = datetime.strptime(released_str, '%d %b %Y').strftime('%Y-%m-%d')

def insert_data(title, released, director, genre):
      with connection:
                with connection.cursor() as cursor:
                    sql = ''' insert into Testing.Movie_info (title, released, director, genre) values (%s, %s, %s, %s)'''
                    cursor.execute(sql, (title, released, director, genre))
                connection.commit()

insert_data(title, released_str, director, genre)