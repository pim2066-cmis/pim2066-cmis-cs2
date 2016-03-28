def meet_cats():
       return """You explore the forest and find a big group of cats made up of four cats. A young light brown she-cat, A massive black tom, A gray and white she-cat, and a young Black and brown Tom.


"What do you want?!" the gray and white she-cat hissed, claws out.


"Stop, Lilypetal" the Black and brown tom meowed


"Do you want to join?" the young light brown she-cat meowed"""


def intro(introduction):
	introduction = raw_input("This game will let you choose your own path to become a warrior. You will start off as a kittypet (house cat) that will choose whether to go to the forest or stay in bed. You will face obstacles along the game and will need to make your decision carefully. Will you survive to become the most powerful leader in the forest? Or will you die before becoming an elder? Goodluck and may Starclan light up your path.")

def wakes_up():
	in_bed = ("""
You wake up on your owner's bed and wonder what to do.
    Go to the forest
    Begs for food
    Stay in bed
Type in one of the choice: """)

	if wakes_up == "Go to the Forest":
		return meet_cats

	elif wakes_up == "Begs for food":
		return choose("""You beg your owner for food and it goes back to sleep.


What to do now?
    Go to the Forest
    Go Back to Sleep
""")
		if choose == "Go to the Forest":
			def meet_cats():

	    else wakes_up == "Go Back to Sleep":
            return """You go back to sleep and never join a clan and enjoy your dream. 

End Game 
"""

		



