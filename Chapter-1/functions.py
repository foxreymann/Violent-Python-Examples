import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def main():
    ip1 = 'localhost'
    ip2 = '127.0.0.1'
    port = 21

    print(ip1 + ': ' + retBanner(ip1, port).decode())
    print(ip2 + ': ' + retBanner(ip2, port).decode())

if __name__ == '__main__':
    main()
