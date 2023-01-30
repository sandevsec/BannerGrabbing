import socket

def banner(ip, port):
	s = socket.socket()
	s.connect((ip, int(port)))
	print(str(s.recv(1024)).strip('b'))

def main():
	ip = input("Please enter the IP: ")
	port = str(input("Please enter the port: "))
	banner(ip, port)

main()