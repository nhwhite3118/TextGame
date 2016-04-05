import time
name = "______"

def compare(*options):
	user = input(name+':')
	if(user in options):
		return user
	return False
def say(words,wait=0):
	print(words)
	print("...")
	time.sleep(wait)
say("""Welcome to my game, you poor sod. You must have known going in
to this that I have no writing skills, so you have brought this upon
yourself. I guess I'll have to do something interesting to make up for
this.""")
time.sleep(0.5)
say("""IMPORTANT: To exit right now, you're going to have to press Ctr-C. 
With all that sweet text you're going to be inputing, its going to take some 
effort to detect the escape key, so its not going to do anything. Sorry, not sorry.""")
time.sleep(0.5)
say("""However, I am sorry that there's no saving at the moment, I'll add it once there's something worth saving. Until then, enjoy this placeholder text.""")
time.sleep(0.5)
say("If you want to start a new game, type in \'new\' and press that enter key")
while(not compare("new")):
	say("""Come on, I know you can do it""")
say("""Nice job. Have an achievement. I'll save it somewhere and come up with a whitty name
for it later.""")
time.sleep(3)
say("""Now, I just have one question before we start. What's your name?""")
name = input(name+":")
say("Ok, "+name+", strap in that seat belt and get ready!")
time.sleep(5)
say("***COUGH***",0.5)
say("***COUGH***",0.5)
say("AhahahaHERM",1)
say("""Nananananananananana, intro song!""")
time.sleep(2)
say("Cut to huge space ships")
time.sleep(2)
say("Cut to a dragon flying over New Zealand")
time.sleep(2)
say("""Cut to a poorly made video-game room with roughly 6 polygons. At least there is a 
crudly-made image of a door on one wall. Did the developer make that in paint?""")
time.sleep(5)
say("""Oh, wait, the models are slowly loading in. I'm pretty sure thats a stock model
for the vase. Oh well, its an indie game, so maybe its for the best he just went with
a royalty-free vase instead of making it himself.""")
time.sleep(8)
say("""Ok, I think everything has loaded in now. I'm pretty sure the controls are WASD,
although I don't remember anything about controls on the menu screen. Maybe instructions
will come in the first patch.""")
while(not compare("W","A","S","D","w","a","s","d")):
	say("Yup, nothing happens. How dissapointing.")
say("""Gosh darn it, I clipped through a wall and hit a kill wall. So much for getting the
no-deaths achievement.""")
time.sleep(3)
say("""I guess I could exit to the main menu and come back. It wouldn't take too long, but
what are the chances of me getting through the game the first time without dying anyways?""")















