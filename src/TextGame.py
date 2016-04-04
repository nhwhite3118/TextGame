import time
def compare(options):
	user = input()
	if(user == options):
		return True
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
print("""\n\n\nNananananananananana, intro song!""")
time.sleep(1)
print("Cut to huge space ships")
time.sleep(1)
print("Cut to a dragon flying over New Zealand")
