from execute_sql import *
import time


def dummy():
    select_query = 'select * from DefinedExpectation;'
    helper = sql_helper()
    # helper.exe_insert_sql(select_query)
    id = helper.exe_insert_sql('''insert into DefinedExpectation (item_name, expectation) values('port 3306', 'on');''')
    print 'id is {}'.format(id)
    helper.exe_update_sql('''update DefinedExpectation set expectation = 'off' where id = {0}'''.format(id))
    all = helper.exe_select_sql('select * from DefinedExpectation where id = {0}'.format(id))
    print all
    all = helper.exe_select_sql('''select * from Task where status !='done' ''')
    print all

def clean():
    helper = sql_helper()
    helper.exe_insert_sql('''  delete from FetchResult ''')
    print 'clean fetch result table when {0}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))



if __name__ == "__main__":
    clean()
