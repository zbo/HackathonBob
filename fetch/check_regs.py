import remote
import logger
import execute_sql



class reg_checker():

    def __init__(self, task_id):
        self.task_id = task_id
        self.sqlhelper = execute_sql.sql_helper()
        self.regs = []
        all = self.sqlhelper.exe_select_sql(''' select * from DefinedExpectation where item_type = 'reg' ''')
        for item in all:
            self.regs.append([item[4], item[2]])

    def check(self):
        self.sqlhelper.exe_update_sql('''  update FetchResult set ui_status =  
        'running' where item_type = 'reg' and task_id={0}'''.format(self.task_id))
        r = remote.remote()
        r.connect()
        stdout, stderr = r.run_command('cat /iserver-install/BIN/Linux/MSIReg.reg ')
        check_result = stdout.readlines()
        r.close()
        for line in check_result:
            logger.reg_log(line)
        for item in self.regs:
            if self.regs_contain(check_result, item):
                self.update_item(item[0], 'match')
            else:
                self.update_item(item[0], 'notmatch')

    def regs_contain(self, check_result_list, item):
        for i in range(len(check_result_list)):
            if str(item[0]).strip() == str(check_result_list[i]).strip():
                content = self.grab_reg_content(i, check_result_list)
                if content.replace('\r','').replace('\n','') == str(item[1]).strip().replace('\n',''):
                    return True
        return False

    def update_item(self, item, match):
        sql = ''' update FetchResult set ui_status =  '{0}' where item_type = 'reg' and task_id={1} and  item_checkname='{2}' '''.format(
            match, self.task_id, item
        )
        self.sqlhelper.exe_update_sql(sql)

    def grab_reg_content(self, i, check_result_list):
        j = i+1
        ret = ''
        current_row = check_result_list[j]
        result = []
        while '[' not in current_row:
            result.append(current_row)
            j = j + 1
            current_row = check_result_list[j]
        for item in result:
            ret = ret + item
        return ret


if __name__ == "__main__":
    sc = reg_checker()
    sc.check()