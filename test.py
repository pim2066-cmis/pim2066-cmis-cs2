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
	if a > 0:
		while a > 0:
			a += 1
			if a % 2 != 0:
				while a % 2 == 0:
					a += a
					print a
	elif a < 0:
		while a < 0:
			a -= 1
			if a % 2 != 0:
				while a % 2 != 0:
					a -= a
					print a
add(90)

				











