import random
print raw_input("Intro: This game will let you choose your own path to become a warrior. You will start off as a kittypet (house cat) that will choose whether to go to the forest or stay in bed. You will face obstacles along the game and will need to make your decision carefully. Will you survive to become the most powerful leader in the forest? Or will you die before becoming an elder? Goodluck and may Starclan light up your path. Let's start with creating your character. (This will be randomize)")


def character(fur, hybrid, eyes, gender, name, urCharacter):
	fur = random.randint("orange", "black", "gray", "white", "tiger-stripe")
	hybrid = random.randint("American Shorthair", "Bengal", "Burmese", "Siamese", "Egyptian Mau")
	eyes = random.randint("yellow", "green", "blue", "red")
	gender = random.randint("female", "male")
	name = random.randint("Tom", "Bob", "Princess", "Jake", "Snow")
	urCharacter = """We have chosen your character and your name is {}. Here is what you look like (vaguely)
	Fur Color: {}
	Hybrid: {}
	Eye Color: {}
	Gender: {}""".format(name, fur, hybrid, eyes, gender)


def fur(color):
	if fur == 1:
		urFur = Orange fur
	elif fur == 2:
		urFur = Black fur
	elif fur == 3:
		urFur = Gray fur
	elif fur == 4:
		urFur = Whtie fur
	elif fur == 5:
		urFur = Tiger-striped fur
	elif fur == 6:
		urFur = Spotted fur
	elif fur == 7:
		urFur = Cream-colored fur
	else:
		urFur = random.randint(0,7)
	return urFur = random.randint(0,7)
	

def hybrid(breed):
	if breed == "American shorthair":
		urHybrid = American Shorthair cat
	elif breed == :"Siamese":
		urHybrid = Siamese cat
	elif breed == :"bengal":
		urHybrid = Bengal cat
	elif breed == :"burmese":
		urHybrid = Burmese cat
	elif breed == :"Egyptian Mau":
		urHybrid = Egyptian Mau cat
	elif breed == :"Siamese":
		urHybrid = Siamese
	elif breed == :"Siamese":
		urHybrid = Siamese
	elif breed == :"Siamese":
		urHybrid = Siamese
def forest(meet):
	meet = raw_input("""One day you decided to go into the forest near your house and while you were just playing with a pine cone, a black-pelt cat pounced out of nowhere and attacked you. You know that this is a fight between life and death but you are inexperience in fighting. This cat is clearly experienced in fighting and it is about 2 inches taller than you. 
How do you choose to attack? OR Do you flee from the attacker?
A. Use your speed to attack whenever you have the chance
B. Pounce at him randomly and aim for his face
C. Run away
D. Stare blankly at him

What do you choose? Type A, B, C, or D
Your answer: """)
	if stranger == "A":
		points = int(9)
		return decision()
	elif stranger == "B":
		points = int(5)
		return decition()
	elif stranger == "C":
		print """ "You shouldn't ever turn your back to your opponent" He hissed at you while you were running. He then caught up with you and clawed out a paw-full of your fur while you flee to your owner (coward). End Game"""
	elif stranger == "D":
		point == int(1)
		return decition()
		
		
def main():
	fur = random.randint("orange", "black", "gray", "white", "tiger-stripe")
	hybrid = random.randint("American Shorthair", "Bengal", "Burmese", "Siamese", "Egyptian Mau")
	eyes = random.randint("yellow", "green", "blue", "red")
	gender = random.randint("female", "male")
	name = random.randint("Tom", "Bob", "Princess", "Jake", "Snow")
	urCharacter = """We have chosen your character and your name is {}. Here is what you look like (vaguely)
	Fur Color: {}
	Hybrid: {}
	Eye Color: {}
	Gender: {}""".format(name, fur, hybrid, eyes, gender)













