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

#variable for types

story1 = """
You're a part of a clan in the forest called Thunderclan. But apparently, the location of your clan is near the lake which means your home is in a high risk of being flooded. 
	That day came... In the evening came a huge storm that thundered through you clan that shook everyone till the bone. The clan started to flood from the lake's water which came in waves after waves. The clan evacuate the area to the hills but someone shouted that a kit was still in the den which is close to be flooded. 
	What do you do?
A. Go help the kit right away (alone)
B. GO help the kit and get someone to help you
C. Don't go help  """
sub_story1 = """
You rushed in to help the kit. You started to swim to the den with water dragging you down. Suddently a huge log hit you across your muzzle and with no one to help you, you Die and the kit as well......T_T
End Game"""


#SAVE
def safe():
	print story1
	help = raw_input("""
What do you choose [type A, B, or C]: """)
	if help == "A":
		print sub_story1
		den()
	elif help == "B":
		print """
You rushed in to help the kit and took a friend of yours to help too. You started to swim to the den with water dragging you down. Suddently a huge log hit you across your muzzle but because your friend was there he helped you to swim to the den."""
		den()
	elif help == "C":
		print """
The kit dies and you were called a coward for the rest of your life"""
		hunt()

#DEN
def den():
	print """
After you reached the den, it was nealy completely covered with water leaving only the top part of the den and the water is slowly raising up. Your ears picked a soft desperate mewings from inside the den. 
Do you choose to go into the den by creating a hole from the top or go under the water to enter from the entrance?
A. Through the entrance
B. Dig a hole up top"""
	life = raw_input("Which do you choose?(A or B): ")
	if life == "A":
		print	"""
You drown while trying to get into the entrance because you got tangled with the twigs. END GAME"""
		return True
		exit()
	else:
		print """
You and your friend help dig a hole from the top of the entrance and sucessfully helped the kitten out"""
		return False
		hunt()


#HUNT
def hunt():
	print """
After all of the flooding event and fixing the camp. There's an event called HUNTING GAME where participants hunts of prey and who ever gain the most point wins. Do you choose to join?

Yes
No"""
	join = raw_input("Your decision (yes or no): ")

	if join == "yes":
		print """
Let the game begin!!"""
		location()
	elif join == "no":
		print """
You just watch and observe the game while the participants are having fun."""
		exit()

#LOCATION
def location():
	print """
Where do you choose to hunt in the territory? Sunning Rocks, in the forest, near the road?

A. Sunning Rocks
B. Forest
C. Near the road"""
	decision = raw_input("Where would you like to hunt? (A, B, C): ")
	if decision == "A":
		print """
You head to the Sunning Rocks. Choosing this location means you having a risk of getting bitten by snakes that are hidden in the cracks of the rocks"""
		point_4 = 25
		return point_4
	elif decision == "B":
		print """
You head to the Forest. Choosing this location means you have a great advantage of hunting plump preys because the forest's lushed bushes helps you camonflage."""
		point_4 = 35
		return point_4
	elif decision == "C":
		print """
You head to the road. Choosing this location means that the preys will be scared away from the loud noises and foul smell of burning tires and car engine."""
		point_4 = 10
		return point_4	

def exit():
	print "Good Game"

		
def main():
	urCharacter = """We have chosen your character and your name is {}. Here is what you look like (vaguely)
	Fur Color: {}
	Hybrid: {}
	Eye Color: {}
	Gender: {}""".format(ur_name, ur_fur, ur_hybrid, ur_eyes, ur_gender)
	print urCharacter

	safe()
	den()
	hunt()
	location()
	exit()

	score1 = safe()
	score2 = den()	
	score3 = hunt()
	score4 = location()

	final_score = int(score1) + int(score2) + int(score3) + int(score4)
	final = """Your final score is {} out of""".format(final_score)



	


main()
