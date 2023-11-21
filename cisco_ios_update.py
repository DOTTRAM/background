import paramiko
from getpass import getpass
import time
import datetime
import sys

ip = raw_input("Please enter your IP address: ")
username = "admin"
password = "pwd12pwd"

f = open('NewdayTest.txt', 'a')
old_stdout = sys.stdout
sys.stdout = f
remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, port=22, username=username,  
                        password=password,
                        look_for_keys=False, allow_agent=False)

remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(65535)
print('\n\n\n##############################################################\n')
print (datetime.datetime.now())
print('\n##############################################################\n')
print (output)

remote_conn.send("config t\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print (output)

remote_conn.send("file prompt quiet\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print (output)

remote_conn.send("end\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print (output)

remote_conn.send("copy running-config tftp://192.168.154.5/\n")
time.sleep(2)
stdout = remote_conn.recv(65535)
print (stdout)

remote_conn.send("config t\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print (output)

remote_conn.send("file prompt alert\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print (output)

remote_conn.send("exit\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print (output)

f.close()