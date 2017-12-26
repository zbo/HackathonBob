
def deamon_log(content):
    path = '/Users/zhu/Desktop/logs/deamon.txt'
    append(content, path)

def port_log(content):
    path = '/Users/zhu/Desktop/logs/port.txt'
    append(content, path)

def service_log(content):
    path = '/Users/zhu/Desktop/logs/service.txt'
    append(content, path)

def lib_log(content):
    path = '/Users/zhu/Desktop/logs/lib.txt'
    append(content, path)

def reg_log(content):
    path = '/Users/zhu/Desktop/logs/reg.txt'
    append(content, path)

def other_log(content):
    path = '/Users/zhu/Desktop/logs/other.txt'
    append(content, path)

def append(content, path):
    file_object = open(path, 'a')
    try:
        file_object.write(content+'\r')
    finally:
        file_object.close()


if __name__ == "__main__":
    deamon_log('should contain several lines')
    other_log('should contain only one line')