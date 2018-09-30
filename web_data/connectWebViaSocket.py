import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.ibm.com",80))

s.close()