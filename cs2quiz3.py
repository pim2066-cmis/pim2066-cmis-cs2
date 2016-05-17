
#Section 1: Terminology
# 1) What is a recursive function?
#		function consisting of a base case which it has the options where there's no recursive call and the recursive case. Then there's an option which it goes to the calculation where it repeats till it reaches it goal in the base case
#
#
# 2) What happens if there is no base case defined in a recursive function?
#		it will continue to run forever
#
#
# 3) What is the first thing to consider when designing a recursive function?
#		where and how it stops running and what are you trying to recurse 
#
#
# 4) How do we put data into a function call?
#		setting a variable then a value to it in the function such as z=5 
#
# 
# 5) How do we get data out of a function call?
#		using return of that valiable such as return z
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 2
#a2 = 6
#a3 = -1

#b1 = 4
#b2 = 0
#b3 = -2

#c1 = -2
#c2 = 4
#c3 = 5
 
#d1 =
#d2 =
#d3 =

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def number(total = 0):
#start of base case
	given = raw_input("Next Number: ")
	if given != "":
		print "The average is {}".format(total)
#end of base case
#start of recursive case
	elif given % 2 == 0:
		given = 0
		amount += 0
		number(total)
	else:
		amount += 1
		total = (total + float(given)) / amount
		number(total)
		

number()


#def adder2(running_total = 0):
#	print "The running total is {}.".format(running_total)
#	number = raw_input("Next Number: ")
#	if number != "":
#		running_total += float(number)
#		adder2(running_total) 
#	else:
#		print "The sum is {}.".format(running_total)
#adder2()




