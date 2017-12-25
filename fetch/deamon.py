import time
from execute_sql import *
helper = sql_helper()


def new_task_coming():
    all = helper.exe_select_sql('''select * from Task where status !='done' and type = 'F' ''')
    if len(all) > 0:
        return all[0][0] # return id
    else:
        return -1


def fetch():
    pass


def listener_working():
    if new_task_coming():
        fetch()

if __name__ == "__main__":
    id = new_task_coming()
    if id != -1:
        print "task should start"
    else:
        print "no task coming"


# if __name__ == "__main__":
#     while 1:
#         listener_working()
#         time.sleep(1)