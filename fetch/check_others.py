import remote
import logger
import execute_sql



class others_checker():
    def __init__(self, task_id):
        self.task_id = task_id
        self.sqlhelper = execute_sql.sql_helper()
        self.exp = {}
        all = self.sqlhelper.exe_select_sql(''' select * from DefinedExpectation where item_type = 'others' ''')
        for item in all:
            self.exp[item[4]] = item[2]

    def check(self):
        self.sqlhelper.exe_update_sql('''  update FetchResult set ui_status =  
        'running' where item_type = 'others' and task_id={0}'''.format(self.task_id))
        self.check_filehandlers()

    def check_filehandlers(self):
        r = remote.remote()
        r.connect()
        stdout, stderr = r.run_command(' ulimit -a ')
        check_result = stdout.readlines()
        r.close()
        for line in check_result:
            logger.filehandler_log(line)
            if 'open files' in line:
                array = str(' '.join(line.split())).split(' ')
                filehandlers = int(array[3])
                if filehandlers > int(self.exp['filehandler']):
                    self.update_item('filehandler', True)
                else:
                    self.update_item('filehandler', False)


    def update_item(self, checkname, match):
        sql = ''' update FetchResult set ui_status =  '{0}' where item_type = 'others' and task_id={1} and  item_checkname='{2}' '''.format(
            match, self.task_id, checkname
        )
        self.sqlhelper.exe_update_sql(sql)

if __name__ == "__main__":
    sc = others_checker(3)
    sc.check()