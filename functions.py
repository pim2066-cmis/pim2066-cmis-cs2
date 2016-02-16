import math
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

def div(volume10, volume20, half):
	return ((volume10 + volume20)/half)
avgvolume = div( float(volume10), float(volume20), 2)

def div(a, b, c, half):
	return ((a + b + c) / half)
ze = div(1, 2, 2.5, 2)
def area(a,b,c):
	x = (a + b + c)/2
	return math.sqrt(x*(x-a)*(x-b)*(x-c))
print area(1,2,2.5)








