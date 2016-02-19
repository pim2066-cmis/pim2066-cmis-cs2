import math
def add(a, b):	        
	return a + b	    		    

print  add(3,7)


def sub(a, b):
	return a - b

print sub(9, 6)

def mul(a, b):
	return a * b

print  mul(9,66)

def div(a, b):
	return a/b

print div(9, 3)

def	sec(seconds, secondsinhr):
	return seconds/secondsinhr
hrs= sec(86400, 3600)
print hrs

def ra(radius, radius1, pi):
	return radius * radius1 * pi
area= ra(5, 5, 3.14159265359)
print area

def pi_area(fourth, pi, radius, radius1, radius2):
	return fourth * pi * radius * radius * radius
volume = pi_area(4/3, 3.14159265359, 6, 6, 6)
print volume

def vol10(fourth, pi, radius, radius1, radius2):
	return fourth * pi * radius * radius * radius
volume10 = vol10(4/3, 3.14159265359, 10, 10, 10)
def mul(fourth, pi, radius, radius1, radius2):
	return fourth * pi * radius * radius * radius
volume20 = mul(4/3, 3.14159265359, 20, 20, 20)

def div(volume10, volume20, half):
	return ((volume10 + volume20)/half)
= avgvol( float(volume10), float(volume20), 2)
print avgvolume

def div(a, b, c, half):
	return ((a + b + c) / half)
ze = div(1, 2, 2.5, 2)
def areacir(a,b,c):
	x = (a + b + c)/2
	return math.sqrt(x*(x-a)*(x-b)*(x-c))
print areacir(1,2,2.5)

def hi_right(word):
	return str ((75-len(word))*" " + word)
print hi_right("Hello")

def hi_mid(term):
	return str ((40-len(term))*" " + term) 
print hi_mid("Hello")
	
def msg(word):
	return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word)+ 4)*"-") + "+"
print msg("Hello")
print msg("I eat cats!")

a = add(3,7)
b = sub(9, 6)
c = mul(9,66)
d = div(9, 3)
e = sec(86400, 3600)
f = ra(5, 5, 3.14159265359)
g = pi_area(4/3, 3.14159265359, 6, 6, 6)
h = avgvolume( float(volume10), float(volume20), 2)
i = areacir(1,2,2.5)
j = hi_right("Hello")
k = hi_mid("Hello")

print msg_box(str(a))
print msg_box(str(b))
print msg_box(str(c))
print msg_box(str(d))
print msg_box(str(e))
print msg_box(str(f))
print msg_box(str(g))
print msg_box(str(h))
print msg_box(str(i))
print msg_box(str(j))
print msg_box(str(k))




