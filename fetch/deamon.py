import time
import check_services
import check_ports
import check_libs
import check_regs
import check_others

import expectation


from execute_sql import *
helper = sql_helper()
task_id = -1

def new_task_coming():
    all = helper.exe_select_sql('''select * from Task where status !='done' and type = 'F' ''')
    if len(all) > 0:
        return all[0][0]  # return id
    else:
        return -1


def fetch():
    pass


def listener_working():
    if new_task_coming():
        fetch()


def insert_expectation(task_id):
    exp = expectation.exceptions()
    exp.load_expectation(task_id)
    pass


def check_service(task_id):
    checker = check_services.service_checker(task_id)
    checker.check()


def check_port(task_id):
    checker = check_ports.port_checker(task_id)
    checker.check()


def check_lib(task_id):
    checker = check_libs.lib_checker(task_id)
    checker.check()


def check_mstr_reg(task_id):
    checker = check_regs.reg_checker(task_id)
    checker.check()


def check_other(task_id):
    checker = check_others.others_checker(task_id)
    checker.check()
    pass


def update_task(task_id):
    helper.exe_update_sql('''select Task where status !='done' and id={0} '''.format(task_id))


def do_once():
    id = new_task_coming()
    if id != -1:
        print "task {0} should start".format(id)
        insert_expectation(int(id))
        check_service(id)
        check_port(id)
        check_lib(id)
        check_mstr_reg(id)
        check_other(id)
        update_task(id)

    else:
        print "{0} no task coming".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

if __name__ == "__main__":
    do_once()


# if __name__ == "__main__":
#     while 1:
#         listener_working()
#         time.sleep(1)