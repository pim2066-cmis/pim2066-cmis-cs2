import random
print raw_input("Intro: This game will let you choose your own path to become a warrior. You will start off as a kittypet (house cat) that will choose whether to go to the forest or stay in bed. You will face obstacles along the game and will need to make your decision carefully. Will you survive to become the most powerful leader in the forest? Or will you die before becoming an elder? Goodluck and may Starclan light up your path. Let's start with creating your character. (This will be randomize)")


def character(fur, hybrid, eyes, gender, name):
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


def wakes_up():
	in_bed = raw_input("""You wake up on your owner's bed and wonder what to do."
    Go to the forest
    Begs for food
    Stay in bed
Type in one of the choice (Exactly): """)
	if wakes_up == "Go to the Forest":
		return meet_cats()
	elif wakes_up == "Begs for food":
		return choose()
	elif wakes_up == "Stay in bed":
		print """You go back to sleep and never join a clan and enjoy your dream. 
End Game"""
		
		
def choose(Food):
	Food = raw_input("""You beg your owner for food and it goes back to sleep.
	
What to do now?
 A.   Go to the Forest
 B.   Go Back to Sleep
Type A or B: """)
	if choose() == "A":
		return meet_cats()
	elif choose() == "B":
		print """You go back to sleep and never join a clan and enjoy your dream. 
End Game"""


def meet_cats(stranger):
       stranger =  raw_input("""You explore the forest and find a big group of cats made up of four cats. A young light brown she-cat, A massive black tom, A gray and white she-cat, and a young Black and brown Tom.
'What do you want?!' the gray and white she-cat hissed, claws out.
'Stop, Lilypetal' the Black and brown tom meowed
'Do you want to join?' the young light brown she-cat meowed.

Your Answer:
Yes. I want to join your clan
No thanks. I'm happy with my life
Type Yes or No: """)
	if meet_cats == "Yes":
		return greetings()
	else meet_cats == "No":
		print """You go back to your owner and never achieve your dream"""
		
		
def greeting(welcome):
	welcome = raw_input(""" "Welcome Powder but that name and collar needs to go!" she meowed
You nod and rip your purple collar off and throw it to the ground
"Good and your clan name will be {} and your mentor will be Nightbreeze." the leader meows
"Do you know how to hunt?" Nightbreeze asked to Powder- No Blackpaw
"Slightly" Blackpaw meowed to Nightbreeze
"Let's go training. Who do you want to train with?" He asked """

		
def main(urCharacter, in_bed, food, stranger, the_end):
	the_end: 

		
		
		
		
		
		
		
		
		
		
		


