def add(a, b):	        
	return a + b	    		    
c = add(3,7)		  


def sub(a, b):
	return a - b
d = sub(9, 6)


def mul(a, b):
	return a * b
e = mul(9,66)


def	div(a, b):
	return a/b
f= div(9, 3)

def	div(seconds, secondsinhr):
	return seconds/secondsinhr
hrs= div(86400, 3600)


def mul(radius, radius1, pi):
	return radius * radius1 * pi
area= mul(5, 5, 3.14159265359)

def mul(fourth, pi, radius, radius1, radius2):
	return fourth * pi * radius * radius * radius
volume = mul(4/3, 3.14159265359, 6, 6, 6)

def mul(fourth, pi, radius, radius1, radius2):
	return fourth * pi * radius * radius * radius
volume10 = mul(4/3, 3.14159265359, 10, 10, 10)
def mul(fourth, pi, radius, radius1, radius2):
	return fourth * pi * radius * radius * radius
volume20 = mul(4/3, 3.14159265359, 20, 20, 20)

def div(volume10, volume20, two):
	return volume10 * volume20 * two
avgvolume = div( float(volume10), float(volume20), 2)


print avgvolume





