import time
def compare(*options):
	user = input(':')
	if(user in options):
		return user
	return False
print("""\n\n\nWelcome to my game, you poor sod. You must have known going in
to this that I have no writing skills, so you have brought this upon
yourself. I guess I'll have to do something interesting to make up for
this.\n""")
time.sleep(0.5)
print("""IMPORTANT: To exit right now, you're going to have to press Ctr-C. 
With all that sweet text you're going to be inputing, its going to take some 
effort to detect the escape key, so its not going to do anything. Sorry, not sorry.""")
time.sleep(0.5)
print("""\nHowever, I am sorry that there's no saving at the moment, I'll add it once there's something worth saving. Until then, enjoy this placeholder text.""")
time.sleep(0.5)
print("\nIf you want to start a new game, type in \'new\' and press that enter key")
while(not compare("new")):
	print("""Come on, I know you can do it""")
print("""\n\n\nNananananananananana, intro song!\n""")
time.sleep(2)
print("Cut to huge space ships\n")
time.sleep(2)
print("Cut to a dragon flying over New Zealand\n")
time.sleep(2)
print("""Cut to a poorly made video-game room with roughly 6 polygons. At least there is a 
crudly-made image of a door on one wall. Did the developer make that in paint?\n""")
time.sleep(5)
print("""Oh, wait, the models are slowly loading in. I'm pretty sure thats a stock model
for the vase. Oh well, its an indie game, so maybe its for the best he just went with
a royalty-free vase instead of making it himself.\n""")
time.sleep(5)
print("""Ok, I think everything has loaded in now. I'm pretty sure the controls are WASD,
although I don't remember anything about controls on the menu screen. Maybe instructions
will come in the first patch.""")
while(not compare("W","A","S","D","w","a","s","d")):
	print("Yup, nothing happens. How dissapointing.")
print("""Gosh darn it, I clipped through a wall and hit a kill wall. So much for getting the
no-deaths achievement.\n""")
time.sleep(3)
print("""I guess I could exit to the main menu and come back. It wouldn't take too long, but
what are the chances of me getting through the game the first time without dying anyways?\n""")















