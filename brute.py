import hashlib
import sys

rfile = open(sys.argv[1], 'r') 
rsum = hashlib.sha512(rfile.read()).hexdigest()

ffile = open(sys.argv[2], 'r')
f = ffile.read()

i = 0

while True:
	fsum = hashlib.sha512(f).hexdigest()
	if rsum[:4] == fsum[:4]:
		print "Ilosc bialych znakow: " + str(i)
		print "Checksum : " + fsum
		break
	f += " "
	i += 1

ffile = open(sys.argv[2], 'w')
ffile.write(f)
