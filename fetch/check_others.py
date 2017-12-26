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
        self.check_iserverfreespace()
        self.check_iserverfreememory()
        self.check_filehandlers()
        self.check_semaphores()
        self.check_iserverprocess()

    def check_iserverprocess(self):
        r = remote.remote()
        r.connect()
        stdout, stderr = r.run_command(''' ps -auxf | grep -v 'grep' | grep 'MSTRSvr' ''')
        check_result = stdout.readlines()
        r.close()
        for line in check_result:
            logger.iserverprocess_log(line)
        if 'MSTRSvr' in check_result[0]:
            self.update_item('iserver-process', 'match')
        else:
            self.update_item('iserver-process', 'notmatch')

    def check_semaphores(self):
        r = remote.remote()
        r.connect()
        stdout, stderr = r.run_command(' cat /proc/sys/kernel/sem ')
        check_result = stdout.readlines()
        r.close()
        for line in check_result:
            logger.semaphores_log(line)
        array = str(check_result[0]).strip().split('\t')
        if int(array[0])>=250 and int(array[1])>=32000 and int(array[2])>=32 and int(array[3])>=4096:
            self.update_item('semaphores', 'match')
        else:
            self.update_item('semaphores', 'notmatch')


    def check_iserverfreememory(self):
        r = remote.remote()
        r.connect()
        stdout, stderr = r.run_command(' free ')
        check_result = stdout.readlines()
        r.close()
        for line in check_result:
            logger.memory_log(line)
            if 'Mem' in line:
                array = str(' '.join(line.split())).split(' ')
                if (float(array[3])+float(array[5]))/float(array[1]) < 0.9:
                    self.update_item('freememory', 'match')
                else:
                    self.update_item('freememory', 'notmatch')

    def check_iserverfreespace(self):
        r = remote.remote()
        r.connect()
        stdout, stderr = r.run_command(' df -k ')
        check_result = stdout.readlines()
        r.close()
        for line in check_result:
            logger.disk_log(line)
            if 'iserver-install' in line:
                array = str(' '.join(line.split())).split(' ')
                if int(array[3])/1024 > 500:
                    self.update_item('iserver-install', 'match')
                else:
                    self.update_item('iserver-install', 'notmatch')


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
                    self.update_item('filehandler', 'match')
                else:
                    self.update_item('filehandler', 'notmatch')


    def update_item(self, checkname, match):
        sql = ''' update FetchResult set ui_status =  '{0}' where item_type = 'others' and task_id={1} and  item_checkname='{2}' '''.format(
            match, self.task_id, checkname
        )
        self.sqlhelper.exe_update_sql(sql)




if __name__ == "__main__":
    sc = others_checker(3)
    sc.check()