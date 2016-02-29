import math
def add(a, b):	        
	return a + b	    		    
print  add(3,4)


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
print sec(86400, 3600) 

def area_cir(radius, radius1, pi):
	return radius * radius1 * pi
print area_cir(5, 5, 3.14159265359)

def sph_area(radius):
	return 4/3.0 * math.pi * radius**3
print sph_area(5)

def avg_volume_sph (d1,d2):
    vs1 = pi_area(d1/2)
    vs2 = pi_area(d2/2)
    return (vs1+vs2)/2
print avg_volume_sph

def tri_area(a, b, c, half):
	return ((a + b + c) / half)
print tri_area(1, 2, 2.5, 2)

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

a = add(3,4)
b = sub(9, 6)
c = mul(9,66)
d = div(9, 3)
e = sec(86400, 3600)
f = tri_area(1, 2, 2.5, 2)
g = sph_area(5)
h = avg_volume_sph(10, 20)
i = areacir(1,2,2.5)
j = area_cir(5, 5, 3.14159265359)
k = hi_right("Hello")
l = hi_mid("Hello")
m = add(3,4)
n = sub(9, 6)
o = mul(9,66)
p = div(9, 3)
q = sec(86400, 3600)
r = tri_area(1, 2, 2.5, 2)
s = sph_area(5)
t = avg_volume_sph(10, 20)
u = areacir(1,2,2.5)
v = area_cir(5, 5, 3.14159265359)
w = hi_right("Hello")
x = hi_mid("Hello")


print msg(str(a))
print msg(str(b))
print msg(str(c))
print msg(str(d))
print msg(str(e))
print msg(str(f))
print msg(str(g))
print msg(str(h))
print msg(str(i))
print msg(str(j))
print msg(str(k))
print msg(str(l))
print msg(str(m))
print msg(str(n))
print msg(str(o))
print msg(str(p))
print msg(str(q))
print msg(str(r))
print msg(str(s))
print msg(str(t))
print msg(str(u))
print msg(str(v))
print msg(str(w))
print msg(str(x))



