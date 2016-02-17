import math
def solve_qua_func(a , b, c):
	x1 = ( - b + math.sqrt ( ( b * b ) - ( 4 * a * c ) ) / 2 * a )
	return x1
def solve_qua_func(a , b, c):
	x2 = ( - b - math.sqrt ( ( b * b ) - ( 4 * a * c ) ) / 2 * a )
	return x2


def main():
	name = raw_input("HELLOO!!! What's your name, pal?: ")
	a = raw_input("Value of a: ")
	b = raw_input("Value of b: ")
	c = raw_input("value of c: ")
	x1 = mul(int(a), int(b), int(c))
	x2 = mul1(int(a), int(b), int(c))
	print output(hello, name, a, b, c, x1, x2)

def output(name, a, b, c, x1, x2):
	return """{}, the equation that you've given was {}x(square) + {}x + {} = 0
	After the calculation, the answer for this is x = {}, {}""".format(name, a, b, c, x1, x2)

main()
	
