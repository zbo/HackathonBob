import remote
import logger
import execute_sql



class lib_checker():

    def __init__(self, task_id):
        self.task_id = task_id
        self.sqlhelper = execute_sql.sql_helper()
        self.libs = []
        all = self.sqlhelper.exe_select_sql(''' select * from DefinedExpectation where item_type = 'library' ''')
        for item in all:
            self.libs.append(item[4])

    def check(self):
        self.sqlhelper.exe_update_sql('''  update FetchResult set ui_status =  
        'running' where item_type = 'library' and task_id={0}'''.format(self.task_id))
        r = remote.remote()
        r.connect()
        stdout, stderr = r.run_command('sudo yum list installed ')
        check_result = stdout.readlines()
        r.close()
        for line in check_result:
            logger.lib_log(line)
        for item in self.libs:
            if self.libs_contain(check_result, item):
                self.update_item(item, 'match')
            else:
                self.update_item(item, 'notmatch')

    def libs_contain(self, check_result_list, item):
        for result in check_result_list:
            if item in str(result):
                return True
        return False

    def update_item(self, item, match):
        sql = ''' update FetchResult set ui_status =  '{0}' where item_type = 'library' and task_id={1} and  item_checkname='{2}' '''.format(
            match, self.task_id, item
        )
        self.sqlhelper.exe_update_sql(sql)


if __name__ == "__main__":
    sc = lib_checker()
    sc.check()