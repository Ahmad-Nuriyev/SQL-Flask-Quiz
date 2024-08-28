import pymysql

connection = pymysql.connect(
    host = "127.0.0.1",
    user = 'root',
    password = '1234',
    db = 'Testing',
    port = 3306,
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)


def create_table():
    with connection:
        with connection.cursor() as cursor:
            sql = """ create table if not exists Testing.Movie_info(
                        id int auto_increment primary key,
                        title varchar(50) not null,
                        released date,
                        director varchar(100) not null,
                        genre varchar(50)
                        );"""
            cursor.execute(sql)
        connection.commit()

create_table()