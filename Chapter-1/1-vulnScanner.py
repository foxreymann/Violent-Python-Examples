import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner.decode().strip('\n').strip('\r')
    except:
        return

def checkVulns(banner):
    f = open("Chapter-1/vuln-banners.txt", 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            return banner + " is vulnerable"

def main():
    ports = [21, 22, 80]
    for host in range(109, 112):
        ip = '100.109.237.' + str(host)
        for port in ports:
            banner = retBanner(ip, port)
            if banner:
                print(ip + ':' + str(port) + ': ' + banner)
                print(checkVulns(banner))

if __name__ == '__main__':
    main()
