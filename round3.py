import random
def round_first(times_1 = 0):
	number = random.randint(0,50)

	round_1 = raw_input("Guess a Number: ")
	if round_1 == str(number):
		print "That's correct!"
	elif round_1 > str(number):
		print "That's too high!"
		times_1 += int(1)
		if times_1 == int(10):
			print "You ran out of guesses"
		else:
			round_first(times_1)
	elif round_1 < str(number):
		print "That's too low!"
		times_1 += int(1)
		if times_1 == int(10):
			print "You ran out of guesses"
		else:
			round_first(times_1)

def round_second(times_2 = 0):
	number_2 = random.randint(0,50)

	round_2 = raw_input("Guess a Number: ")
	if round_2 == str(number_2):
		print "That's correct!"
	elif round_2 > str(number_2):
		print "That's too high!"
		times_2 += int(1)
		if times_2 == int(10):
			print "You ran out of guesses"
		else:
			round_second(times_2)
	elif round_2 < str(number_2):
		print "That's too low!"
		times_2 += int(1)
		if times_2 == int(10):
			print "You ran out of guesses"
		else:
			round_second(times_2)

def round_third(times_3 = 0):
	number_3 = random.randint(0,50)

	round_3 = raw_input("Guess a Number: ")
	if round_3 == str(number_3):
		print "That's correct!"
	elif round_3 > str(number_3):
		print "That's too high!"
		times_3 += int(1)
		if times_3 == int(10):
			print "You ran out of guesses"
		else:
			round_third(times_3)
	elif round_3 < str(number_3):
		print "That's too low!"
		times_3 += int(1)
		if times_3 == int(10):
			print "You ran out of guesses"
		else:
			round_third(times_3)

def rounds():
	print "Starting round One"
	round_first()
	print """
Starting round Two"""
	round_second()
	print """
Starting round Three"""
	round_third()
			
		

rounds()
