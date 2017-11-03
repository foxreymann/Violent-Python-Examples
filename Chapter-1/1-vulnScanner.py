import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner.decode().strip('\n')
    except:
        return

def checkVulns(banner):
    f = open("Chapter-1/vuln-banners.txt"
    for line in f.readlines():
        if line.

def main():
    ports = [22, 80]
    for host in range(105, 115):
        ip = '100.109.237.' + str(host)
        for port in ports:
            banner = retBanner(ip, port)
            if banner:
                print(ip + ':' + port + ': ' + banner)

if __name__ == '__main__':
    main()
