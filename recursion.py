"""def countup(start,stop):
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

main()"""




def cal(run, next_no):
	if total != "":
		run(total)
	else:
		print run
		cal(run + next_no)

def main():
	total = 0.0
	next = 0.0

	next_no =  float(raw_input("Running total: "))
	if next_no == " ":
		print cal()


	run = float(raw_input("Running total: "))
	if run == int():
		return cal()
	elif run == None:
		print "Good BYE"
	else:
		print float(raw_input("Running total: "))

	


main()
	
