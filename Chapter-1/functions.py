import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner.decode().strip('\n')
    except:
        return 'error'

def checkVulns(banner):
    if "vsFTPd 3.0.3" in banner:
        return "vsFTPd is vulnerable"
    else:
        return "FTP Server is not vulnerable"

def main():
    ip1 = 'localhost'
    ip2 = '127.0.0.1'
    port = 21

    banner1 = retBanner(ip1, port)
    print(ip1 + ': ' + banner1)
    print(checkVulns(banner1))
    banner2 = retBanner(ip2, port)
    print(ip2 + ': ' + banner2)
    print(checkVulns(banner2))

if __name__ == '__main__':
    main()
