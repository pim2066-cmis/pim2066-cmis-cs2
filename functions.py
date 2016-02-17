import math
def add(a, b):	        
	return a + b	    		    
c = add(3,7)	
print c	  


def sub(a, b):
	return a - b
d = sub(9, 6)
print d

def mul(a, b):
	return a * b
e = mul(9,66)
print e

def div(a, b):
	return a/b
f= div(9, 3)
print f

def	div(seconds, secondsinhr):
	return seconds/secondsinhr
hrs= div(86400, 3600)
print hrs

def mul(radius, radius1, pi):
	return radius * radius1 * pi
area= mul(5, 5, 3.14159265359)
print area

def mul(fourth, pi, radius, radius1, radius2):
	return fourth * pi * radius * radius * radius
volume = mul(4/3, 3.14159265359, 6, 6, 6)
print volume

def mul(fourth, pi, radius, radius1, radius2):
	return fourth * pi * radius * radius * radius
volume10 = mul(4/3, 3.14159265359, 10, 10, 10)
def mul(fourth, pi, radius, radius1, radius2):
	return fourth * pi * radius * radius * radius
volume20 = mul(4/3, 3.14159265359, 20, 20, 20)

def div(volume10, volume20, half):
	return ((volume10 + volume20)/half)
avgvolume = div( float(volume10), float(volume20), 2)
print avgvolume

def div(a, b, c, half):
	return ((a + b + c) / half)
ze = div(1, 2, 2.5, 2)
def area(a,b,c):
	x = (a + b + c)/2
	return math.sqrt(x*(x-a)*(x-b)*(x-c))
print area(1,2,2.5)

def hi_right(word):
	return str ((80-len(word))*" " + word)
print hi_right("Hello")

def hi_mid(term):
	return str ((40-len(term))*" " + term) 
print hi_mid("Hello")
	
def msg(word):
	return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word)+ 4)*"-") + "+"
print msg("Hello")
print msg("I eat cats!")






