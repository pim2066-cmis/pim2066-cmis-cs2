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
def cal_guess_greater(guess, realNum):
	greater = guess - realNum

def cal_guess_less(guess, realNum):
	less = realNum - guess

def guessNreal(guess, realNum):
	realNum = random.random()
	if guess > realNum:
		return True
	else:
		return False


def cal_guess(guess, realNum):
	if result == True:
		calculation = greater
	else:
		calculation = less
	return """The target was {}.
Your guess was {}.
That's under by {}.""".format(realNum, guess, calculation)
	print

def main():
	minimum_num = raw_input("What is the minimun number?: ")
	maximum_num = raw_input("What is the maximum number?: ")

	estimate = raw_input("""I'm thinking of a number from {} to {}""".format(minimum_num, maximum_num))

	guess = raw_input("What do you think it is?: ")
	print 




main()

