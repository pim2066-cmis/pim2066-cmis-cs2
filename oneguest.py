import random
#variables:
#	mimimum_num
#	maximum_num
#	estimate
#	guess
#	realNum
#	difference
#
#
#


#Equation to find the difference when guess is under the real num

def main():
	minimum_num = raw_input("What is the minimun number?: ")
	maximum_num = raw_input("What is the maximum number?: ")

	estimate = """I'm thinking of a number from {} to {}""".format(minimum_num, maximum_num)

	guess = raw_input("What do you think it is?: ")
	print output(minimum_num, maximum_num, estimate, guess)

def output():
	return """The target was {}.
Your guess was {}.
That's under by {}.""".format(realNum, guess, difference)




