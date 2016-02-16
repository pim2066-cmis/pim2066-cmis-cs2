def add(x, y):
	z = x + y
	return z

def main():
	name = raw_input("What's your name?: ")
	x = raw_input("Type a number: ")
	y = raw_input("Type in another: ")
	z = add(int(x), int(y))
	print output(name, x, y, z)


def output(name, x, y, z):
	return """Hello there, {}!
	Did you know:{} + {} = {}""".format(name, x ,y , x)

main()

