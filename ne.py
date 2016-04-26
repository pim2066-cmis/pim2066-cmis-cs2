def getLargest(a, b, c):
	if a > b and a > c:
		return a
	elif b > a and b > c:
		return b
	else:
		return c

#q28 +1 uses if...else or an equivalent structure
#q29 +1 uses a boolean expression to test equality
#q30 +1 CORRECTLY determines and returns if the numbers are all different
def allDifferent(a, b, c):
	if a == b or b == c or a == c:
		return False
	else:
		return True

#q31 +1 gets and converts 3 values correctly
#q32 +1 uses conditional to give feedback if numbers are not all different
def main():
	print "Type in 3 different numbers (decimals are OK!)"
	a = float(raw_input("A: "))
	b = float(raw_input("B: "))
	c = float(raw_input("C: "))
	
	if allDifferent(a, b, c):
		largest = getLargest(a, b, c)
		print "The largest number was {}".format(largest)
	else:
		print "You didn't follow directions"

main()
