#while True:
#	print ":D"

#while False:	
#	print ":c"


#def countdown(x):
#	while x > 0:
#		print x
#		x -= 1

#def main():
#	countdown(9)

#main()

#
#def up(x):
#	while x < 10:
#		print x
#		x += 1

#def main():
#	up(0)

#main()


#def count(z,u):	
#	if z < u:
#		while z < u:
#			print z
#			z += 1
#	elif z > u:
#		while z > u:
#			print z
#			z -= 1
#	while u > z:
#		print u
#		u -= 1
#count(11,6)

def add(a):
	sum = 0
	if a > 0:
		while a > 0:	
			if a % 2 == 1:
				sum += a
			n -= 1

	elif a < 0:
		while a < 0:
			if a % 2 == 1:
				sum += a	
			n += 1
	return sum

def grid(w, h):
	out = " "
	while h != 0:
		print "." * w
		h-=1

print grid(10,10)

				











