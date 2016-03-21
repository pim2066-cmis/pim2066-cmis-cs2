import random
#variables:
#	minimum_num
#	maximum_num
#	estimate
#	guess
#	realNum
#	difference
#
#
#


#Equation to find the difference when guess is under the real num
def cal(realNum, guess):
    result = abs(realNum - guess)

def main():
	minimum_num = raw_input("What is the minimun number?: ")
	maximum_num = raw_input("What is the maximum number?: ")

	estimate = raw_input("""I'm thinking of a number from {} to {}""".format(minimum_num, maximum_num))

	guess = raw_input("What do you think it is?: ")

    realNum = random.random()

    if guess == realNum:
        print """
The target was {}.
Your guess was {}.
That's correct! You must be psychic!
""" .format(guess, realNum)

    elif guess > realNum :
		print """
The target was {}.
Your guess was {}.
That's under by {}.
""" .format(realNum,guess, result)

main()






