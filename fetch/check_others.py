import remote
import logger
import execute_sql



class others_checker():
    def __init__(self, task_id):
        self.task_id = task_id
        self.sqlhelper = execute_sql.sql_helper()
        self.libs = []
        all = self.sqlhelper.exe_select_sql(''' select * from DefinedExpectation where item_type = 'others' ''')
        for item in all:
            self.libs.append(item[4])

    def check(self):
        self.sqlhelper.exe_update_sql('''  update FetchResult set ui_status =  
        'running' where item_type = 'others' and task_id={0}'''.format(self.task_id))
        r = remote.remote()
        r.connect()
        stdout, stderr = r.run_command(' pwd ')
        check_result = stdout.readlines()
        r.close()