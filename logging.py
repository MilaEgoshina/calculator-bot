import datetime

def info_log(val):           # информационные сообщения о рез-тах выполнения операций
    dt_now = datetime.datetime.now()
    with open('log.txt', 'a') as file:
        file.write('{};Info:;{}\n'
                    .format(dt_now, val))

def warning_log(val):        # предупреждающие  сообщения
    dt_now = datetime.datetime.now()
    with open('log.txt', 'a') as file:
        file.write('{};Info:;{}\n'
                    .format(dt_now, val))

def error_log(val):           # сообщения об ошибках
    dt_now = datetime.datetime.now()
    with open('log.txt', 'a') as file:
        file.write('{};Info:;{}\n'
                    .format(dt_now, val))


path = 'log.txt'
file = open(path, 'r')
for line in file:
    print(line)
file.close()