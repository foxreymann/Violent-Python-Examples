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
    if "vsFTPd 3.0.3" in banner:
        return "vsFTPd is vulnerable"
    else:
        return "FTP Server is not vulnerable"

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
