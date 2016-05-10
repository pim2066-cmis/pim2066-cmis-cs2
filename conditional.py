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
		point_1 = str(15)
	elif help == "C":
		print """The kit dies and you were called a coward for the rest of your life"""
		point_1 = str(5)

#DEN
def den():
	print """After you reached the den, it was nealy completely covered with water leaving only the top part of the den and the water is slowly raising up. Your ears picked a soft desperate mewings from inside the den. 
Do you choose to go into the den by creating a hole from the top or go under the water to enter from the entrance?
A. Through the entrance
B. Dig a hole up top"""
	life = raw_input("Which do you choose?(A or B): ")
	if life == "A":

		print	"You drown while trying to get into the entrance because you got tangled with the twigs. END GAME"
		return True
	else:
		print "You and your friend help dig a hole from the top of the entrance and sucessfully helped the kitten out"
		return False
		point_2 = str(20)

#HUNT
def hunt():
	print """After all of the flooding event and fixing the camp. There's an event called HUNTING GAME where participants hunts of prey and who ever gain the most point wins. Do you choose to join?

Yes
No"""
	join = raw_input("Your decision (yes or no): ")

	if join == "yes":
		print "Let the game begin!!"
		location()
		point_3 = str(25)
	elif join == "no":
		print "You just watch and observe the game while the participants are having fun."
		point_3 = str(5)

#LOCATION
def location():
	print """Where do you choose to hunt in the territory? Sunning Rocks, in the forest, near the road?

A. Sunning Rocks
B. Forest
C. Near the road"""
	decision = raw_input("Where would you like to hunt? (A, B, C): ")
	if decision == "A":
		print "You head to the Sunning Rocks. Choosing this location means you having a risk of getting bitten by snakes that are hidden in the cracks of the rocks"
		point_4 = str(25)
	elif decision == "B":
		print "You head to the Forest. Choosing this location means you have a great advantage of hunting plump preys because the forest's lushed bushes helps you camonflage."
		point_4 = str(35)
	elif decision == "C":
		print "You head to the road. Choosing this location means that the preys will be scared away from the loud noises and foul smell of burning tires and car engine."
		point_4 = str(10)	


#GAME_POINT
def game_point():
	final_score = point_1 + point_2 + point_3 + point_4
	
		
def main():
	urCharacter = """We have chosen your character and your name is {}. Here is what you look like (vaguely)
	Fur Color: {}
	Hybrid: {}
	Eye Color: {}
	Gender: {}""".format(ur_name, ur_fur, ur_hybrid, ur_eyes, ur_gender)
	print urCharacter

	safe(help)
	den()
	hunt()
	location()
	game_point()

	final = """Your final score is {} out of""".format(final_score)



	


main()
