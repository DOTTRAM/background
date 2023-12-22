import time
from datetime import datetime
import paramiko

login = 'ciscogtkz'
passw = 'Jkbvgbflf80'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
file = open('C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\Cisco\\device\\device.txt', 'r')

for line in file:
    timestamps = str(datetime.now())
    print('Timestamp:', timestamps)


    def connector():
        print('Connecting to IP:' + line)
        client.connect(line.strip(), username=login, password=passw, look_for_keys=False, allow_agent=False)


    try:
        connector()
        with client.invoke_shell() as ssh:
            ssh.send('enable\n')
            ssh.send('terminal length 0\n')
            ssh.send('show running-config\n')
            time.sleep(10)
            result = ssh.recv(10000).decode("utf-8")
            fo = open(line.strip() + '.txt', 'w')
            fo.writelines(result)
            fo.close()

    except Exception as e:
        error_log = str(e)
        print(error_log + '\n')

file.close()
