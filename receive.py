import socket as socklib

sock = socklib.socket(socklib.AF_INET, socklib.SOCK_DGRAM)
myIP = "192.168.195.184"
myPort = 12345
sock.bind((myIP, myPort))

nama = {"192.168.195.184" : "Kinan", "192.168.195.137" : "Zhillan", "192.168.195.117" : "Jundan", "192.168.195.97" : "Ishlah",  "192.168.195.66" : "Zaky", "192.168.195.148" : "Kent", "192.168.195.38" : "Nadif", "192.168.195.160" : "Habib"}

while True:
    try:
        data, addr = sock.recvfrom(1024)
        ip, _ = addr
        print(f"Received message from {nama[ip]}: {data.decode()}")
    except:
        print(f"Received message from unknown: {data.decode()}")