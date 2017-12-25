import remote
import logger

class service_checker():

    def __init__(self):
        pass

    def check(self):
        r = remote.remote()
        r.connect()
        stdout, stderr = r.run_command('ps -A')
        check_result = stdout.readlines()
        for line in check_result:
            logger.service_log(line)
        r.close()

if __name__ == "__main__":
    sc = service_checker()
    sc.check()