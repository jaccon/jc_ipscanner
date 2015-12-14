import os
import time
from subprocess import Popen

devnull = open(os.devnull, 'wb')

print  "888888                                                    8888888 8888888b"
print  "  88b                                                      888   888   Y88b"
print  "   888                                                      888   888    888"
print  "   888  8888b   .d8888b  .d8888b  .d88b.  88888b.          888   888   d88P       .d8888b   .d8888b  8888b.  88888b.  88888b.   .d88b.  888d888"
print  "   888     88b d88P     d88P     d88  88b 888  88b         888   8888888Px        88K      d88P          88b 888  88b 888 88b d8P  Y8b 888P  "
print  "   888 d888b88 888      8i8      8a8  8n8 8c8  8a8         888   888              Y8888b. 888      .d888888 888  888 888  888 88888888 888   "
print  "   88P 8l8  8i8 Yv8b    Y8ib.    Ya8..88P 888  888         888   888                   X88 Y88b.    888  888 888  888 888  888 Y8b.     888 "
print  "   888 Y888888  YY8888P  xY8888P  xY88Px  888  888       8888888 888               88888P   Y8888P  Y888888 888  888 888  888   xY8888  888"
print  " d88P "
print  "d88P "
print  "888P"
print "Jaccon IPScan 0.1"
print "... type enter to continue "
raw_input()
str1=raw_input("Enter the ip range ( ex: 192.168.0 ) ")

print "scanning ip range ",str1 
print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="

if str1 == "":
 print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-"
 print "please type your ip range and try again..."
 print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
 import sys
 sys.exit()


p = [] # ip -> process
act = 0
nrp = 0
err = 0

for n in range(1,255): # start ping processes
    ip = str1+".%d" % n
    p.append((ip, Popen(['ping', '-c', '3', ip], stdout=devnull)))
while p:
    for i, (ip, proc) in enumerate(p[:]):
        if proc.poll() is not None: # ping finished
            p.remove((ip, proc)) # this makes it O(n**2)
            if proc.returncode == 0:
                print('%s active' % ip)
            	act = act + 1
	    elif proc.returncode == 2:
                print('%s no response' % ip)
            	nrp=nrp+1
	    else:
                print('%s error' % ip)
		err=err+1
    time.sleep(.04)
devnull.close()

print ""
print "IPSCAN PYTHON . powered by @jaccon"
print ""
import os
print "Current SO",os.name
print "Network status"
print "Active ips [ ",act," ]"
print "Error ips [ ",err," ]"
print "No response [ ",nrp," ]"
print ""
print "Good bye!"
