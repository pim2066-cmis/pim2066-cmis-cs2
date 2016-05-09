import random
print raw_input("Intro: This game will let you choose your own path to become a warrior. You will start off as a kittypet (house cat) that will choose whether to go to the forest or stay in bed. You will face obstacles along the game and will need to make your decision carefully. Will you survive to become the most powerful leader in the forest? Or will you die before becoming an elder? Goodluck and may Starclan light up your path. Let's start with creating your character. (This will be randomize)")

#variables for CHARACTERS
fur = ["orange", "black", "gray", "white", "tiger-stripe"]
ur_fur = random.choice(fur)
hybrid = ["American Shorthair", "Bengal", "Burmese", "Siamese", "Egyptian Mau"]
ur_hybrid = random.choice(hybrid)
eyes = ["yellow", "green", "blue", "red"]
ur_eyes = random.choice(eyes)
gender = ["female", "male"]
ur_gender = random.choice(gender)
name = ["Tom", "Bob", "Princess", "Jake", "Snow", "John", "Jacky"]
ur_name = random.choice(name)


#SAVE
def safe(help):
	"""You're a part of a clan in the forest called Thunderclan. But apparently, the location of your clan is near the lake which means your home is in a high risk of being flooded. 
	That day came... In the evening came a huge storm that thundered through you clan that shook everyone till the bone. The clan started to flood from the lake's water which came in waves after waves. The clan evacuate the area to the hills but someone shouted that a kit was still in the den which is close to be flooded. 
	What do you do?
A. Go help the kit right away (alone)
B. GO help the kit and get someone to help you
C. Don't go help  """
	help = raw_input("What do you choose [type A, B, or C]: ")
	if help == "A":
		print """You rushed in to help the kit. You started to swim to the den with water dragging you down. Suddently a huge log hit you across your muzzle and with no one to help you, you Die and the kit as well......T_T
End Game"""
	elif help == "B":
		print """You rushed in to help the kit and took a friend of yours to help too. You started to swim to the den with water dragging you down. Suddently a huge log hit you across your muzzle but because your friend was there he helped you to swim to the den."""
	elif help == "C":
		print """The kit dies and you were called a coward for the rest of your life
END GAME COWARD"""

#DEN
def den():
	"""After you reached the den, it was nealy completely covered with water leaving only the top part of the den. Your ears picked a soft desperate mewings from inside the den. 

Do you choose to go into the den by creating a hole from the top or go under the water to enter from the entrance?"""


	
		
def main():
	urCharacter = """We have chosen your character and your name is {}. Here is what you look like (vaguely)
	Fur Color: {}
	Hybrid: {}
	Eye Color: {}
	Gender: {}""".format(ur_name, ur_fur, ur_hybrid, ur_eyes, ur_gender)
	print urCharacter

	safe(help)


main()

		
		
		
		
		
		
		
		
		
		
		


