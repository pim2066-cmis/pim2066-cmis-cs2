def fur(color):
	if color == 1:
		urFur = "Orange fur"
	elif color == 2:
		urFur = "Black fur"
	elif color == 3:
		urFur = "Gray fur"
	elif color == 4:
		urFur = "Whtie fur"
	elif color == 5:
		urFur = "Tiger-striped fur"
	elif color == 6:
		urFur = "Spotted fur"
	elif color == 7:
		urFur = "Cream-colored fur"
	else:
		urFur = random.randint(0,7)
	return random.randint(0,7)
	
def main():
	Color = """You got {}.""".format(urFur)
	
print 
main()
