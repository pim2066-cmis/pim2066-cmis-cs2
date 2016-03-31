#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) 5 == 5
#b) 6 > 4
#c) "HELLO" != "pig"
#
#2) What does 'return' do?
# It calculates the function and then spits out the result of it
#
#
#
#3) What are 2 ways indentation is important in python code?
#a) 'group' the function together/ to see where it starts
#b) To make it easier to read the function
#
#

#PART 2: Reading
#Type the values for 9 of the 12 of the variables below.
#
#problem1_a) 36
#problem1_b) square root of 3
#problem1_c) 0
#problem1_d) 5
#
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) True
#
#problem3_a) 0.3
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5
#
#problem4_a) 9 = 7
#problem4_b) 6 = 5
#problem4_c) 1.5 = 0.125
#problem4_d) 5.5 = 5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)


def process(a ,b, c):
	if a > b and a > c:
		return a 
	elif b > a and b > c:
		return b
	elif c > a and c > b:    
		return c
	else:
		return False
#function for comparing the numbers

def main():
	type_num = raw_input("Type in three different numbers")
	int_1 = raw_input("A: ")
	int_2 = raw_input("B: ")
	int_3 = raw_input("C: ")
#int stands for the interger that will be typed into

	result = "The largest number is {}". format(process)
	
	print output(result)

def output(result):
	if result == False:
		print "You didn't follow instructions"
 	else:
		print "The largest number is {}". format(process(a ,b, c)) 

main()



