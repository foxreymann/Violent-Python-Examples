import socket
import sys
import os

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner.decode().strip('\n').strip('\r')
    except:
        return

def checkVulns(banner, filename):
    f = open(filename, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            return banner + " is vulnerable"

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]

        if not os.path.isfile(filename):
            print(filename + ' does not exist.')
            exit(0)

        if not os.access(filename, os.R_OK):
            print(filename + ' access denied.')
            exit(0)
    else:
        print('Usage: ' + str(sys.argv[0]) + ' <vuln filename>')
        exit(0)

    ports = [21, 22, 80]
    for host in range(109, 112):
        ip = '100.109.237.' + str(host)
        for port in ports:
            banner = retBanner(ip, port)
            if banner:
                print(ip + ':' + str(port) + ': ' + banner)
                print(checkVulns(banner, filename))

if __name__ == '__main__':
    main()
