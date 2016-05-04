def countup(start,stop):
	if start >= stop:
		print "BOOM!!"
	else:
		print start
		countup(start+1,stop)

def main():
	start = int(raw_input("Start: "))
	stop = int(raw_input("Stop: "))

	countup(start,stop)
	return

main()



def countup(start,stop):
	if start <= stop:
		print "BOOM!!"
	else:
		print start
		countup(start-1,stop)

def main():
	start = int(raw_input("Start: "))
	stop = int(raw_input("Stop: "))

	countup(start,stop)
	return

main()


def adder2(running_total = 0):
	print "The running total is {}.".format(running_total)
	number = raw_input("Next Number: ")
	if number != "":
		running_total += float(number)
		adder2(running_total) 
	else:
		print "The sum is {}.".format(running_total)
adder2()


def adder2(running_total = 0):
	print "The running total is {}.".format(running_total)
	number = raw_input("Next Number: ")
	if number != "":
		running_total += float(number)
		adder2(running_total) 
	else:
		print "The sum is {}.".format(running_total)
adder2()



def biggest(big = 0):
	number_1 = raw_input("Next: ")
	if number_1 == "":
		print "The biggest number is {}.".format(big)
	elif float(number_1) < float(big):
		biggest(big)
	elif float(number_1) > float(big):
		big = number_1
		biggest(big)

biggest()


def biggest(big = float('inf')):
	number_1 = raw_input("Next: ")
	if number_1 == "":
		print "The biggest number is {}.".format(big)
	elif float(number_1) < float(big):
		biggest(big)
	elif float(number_1) > float(big):
		big = number_1
		biggest(big)

biggest()
