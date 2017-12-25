import execute_sql

class exceptions():

    def __init__(self):
        pass

    def load_expectation(self, task_id):
        sqlhelper = execute_sql.sql_helper()
        all = sqlhelper.exe_select_sql('''  select * from DefinedExpectation ''')
        print all
        for item in all:
            sql = '''insert into FetchResult (task_id, ui_status, item_name, item_type, item_checkname, expectation_id) values 
            ({0},'{1}','{2}','{3}', '{4}', '{5}')'''.format(
                task_id, 'pending', item[1], item[3], item[4], item[0]
            )
            print sql
            sqlhelper.exe_insert_sql(sql)

if __name__ == "__main__":
    exp = exceptions()
    exp.load_expectation(3)