
#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#   assignment operator
#   used to say what is the variable stand for
#
#2 3pts) Write a technical definition for 'function'
#   named sequence of statement that perform calculation
#
#
#3 1pt) What does the keyword "return" do?
#   give value that can be print o put in variable (spits the output)
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: string str("Pim) str("jello")
#	2: len len("hiii") len("hello teacher")
#	3: float float(8.988757654,3) float(785864375, 4)
#	4: interger int(87) int(74648)
#	5: boolean bool("bingo") bool(45345)
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#       The difference is that function definition are all the lines that makes up the function except the one that starts with "print" while the function call is the one behind the word print
#etc   def add(7,9) - function definition
#            return x = (7 + 9) - function definition
#       print (x)    - function call
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: Programmer writes the code
#	2: Then feed the code to the interpreter
#	3: Inerpreter executes lines of code 1 at a time
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

import math
def find_diameter(u):
	return u / math.pi

def total(a, b, c):
    return a + b + c

def output(a, b, c, d):
    print"""
c1:     {}
c2:     {}
c3:     {}
Totals:     {}
""".format(a,b,c,d)
 

def main():
    C1=raw_input("Area of C1: ")
    C2=raw_input("Area of C2: ")
    C3=raw_input("Area of C3: ")
    
    a = find_diameter(float(C1))
    b = find_diameter(float(C2))
    c = find_diameter(float(C3))
    t = total(a, b, c)
    
    print output(a, b, c, t)

main()





