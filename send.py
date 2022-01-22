import socket as socklib

IP = {"Kinan" : "192.168.195.184", "Zhillan" : "192.168.195.137", "Jundan" : "192.168.195.117", "Ishlah" : "192.168.195.97", "Zaky" : "192.168.195.66", "Kent" : "192.168.195.148", "Nadif" : "192.168.195.38", "Habib" : "192.168.195.160"}

nama = ""
targetPort = 12345
mysocket = socklib.socket(socklib.AF_INET, socklib.SOCK_DGRAM)

while nama != "QUIT":
    try:
        nama = input("Masukkan nama penerima: ")
        message = input("Masukkan pesan: ")
        targetIP = IP[nama]
        mysocket.sendto(message.encode(), (targetIP, targetPort))

    except:
        print("Nama tidak dikenali!")