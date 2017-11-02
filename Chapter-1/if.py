import socket
import sys

socket.setdefaulttimeout(2)
s = socket.socket()

try:
    s.connect(("localhost",21))
except Exception as e:
    print('Error' + str(e))
    sys.exit()

banner = s.recv(1024).decode()

if ("vsFTPd 3.0.3" in banner):
    print ("[+] vsFTPd.")
else:
    print ("[-] FTP Server is not vulnerable.")
