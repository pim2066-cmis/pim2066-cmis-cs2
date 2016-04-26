def countup(start,stop):
	if start >= stop:
		print "BOOM!!"
	else:
		print start
		countup(start+1)

def main():
	start = int(raw_input("Start: "))
	stop = int(raw_input("Stop: "))

	countup(start,stop)
	return

main()
