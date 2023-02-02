#!/usr/bin/python3

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#
#
#	File Name 	 	: BannerGrabbing
#	Author	 	 	: Sandip Das
#	last modified		: 20 Jan 2023
#	Language		: Python
#	python version 		: python3.10
#	Requirment 		: socket , pyfiglet , colored , termcolor
#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


import socket
import pyfiglet
from termcolor import colored
from time import time
from datetime import datetime
front_banner=pyfiglet.figlet_format(" PORT SCANNER")
print(colored(front_banner,'green'))



#Banner
print("_"*50)
print("_"*50)
print(colored("Scanning Taget: ",'green'))
print(colored("Scanning started at: " +str(datetime.now()),'green'))
print("_"*50)
print("_"*50) 


def banner(ip, port):
	s = socket.socket()
	s.connect((ip, int(port)))
	print(str(s.recv(1024)).strip('b'))

def main():
	ip = input("Please enter the IP: ")
	port = str(input("Please enter the port: "))
	banner(ip, port)

main()
