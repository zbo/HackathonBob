import mysql.connector

config = {
        #'host': '127.0.0.1',
        'host': '10.197.32.135',
        'user': 'root',
        'password': '123456',
        'port': 3306,
        'database': 'hackathon',
        'charset': 'utf8'
    }


class sql_helper:

    def __init__(self):
        pass

    def exe_select_sql(self, query):
        try:
            cnn = mysql.connector.connect(**config)
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))
        cursor = cnn.cursor()
        try:
            sql_query = query
            cursor.execute(sql_query)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print('query error!{}'.format(e))
        finally:
            cnn.commit()
            cursor.close()
            cnn.close()


    def exe_insert_sql(self, query):
        try:
            cnn = mysql.connector.connect(**config)
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))
        cursor = cnn.cursor()
        try:
            sql_query = query
            cursor.execute(sql_query)
            return cursor.lastrowid
        except mysql.connector.Error as e:
            print('query error!{}'.format(e))
        finally:
            cnn.commit()
            cursor.close()
            cnn.close()

    def exe_update_sql(self, query):
        try:
            cnn = mysql.connector.connect(**config)
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))
        cursor = cnn.cursor()
        try:
            sql_query = query
            cursor.execute(sql_query)
        except mysql.connector.Error as e:
            print('query error!{}'.format(e))
        finally:
            cnn.commit()
            cursor.close()
            cnn.close()


