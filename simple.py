import math
def solve_qua_func(a , b, c):
	return (( -b ) +  math.sqrt (( b*b ) - ( 4*a*c ))) / ( 2*a )
def solve_qua_func1(a , b, c):
	return (( -b ) -  math.sqrt (( b*b ) - ( 4*a*c ))) / ( 2*a )

def output(name, a, b, c, x1, x2):
	return """{}, the equation that you've given was {}x(square) + {}x + {} = 0
	After the calculation, the answer for this is x = {}, {}""".format(name, a, b, c, x1, x2)


def main():
	name = raw_input("HELLOO!!! What's your name, pal?: ")
	a = raw_input("Value of a: ")
	b = raw_input("Value of b: ")
	c = raw_input("value of c: ")
	x1 = solve_qua_func(int(a), int(b), int(c))
	x2 = solve_qua_func1(int(a), int(b), int(c))
	print output(name, a, b, c, x1, x2)


main()
	
