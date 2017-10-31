import socket
socket.setdefaulttimeout(2)
s = socket.socket()
try:
    s.connect(("localhost",21))
except Exception as e:
    print('Error' + str(e))

ans = s.recv(1024)
if ("vsFTPd 3.0.3".encode() in ans):
    print ("[+] vsFTPd.")
else:
    print ("[-] FTP Server is not vulnerable.")
