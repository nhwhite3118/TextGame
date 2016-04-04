
def compare(options):
	user = input()
	if(user == options):
		return True
	return False
print("""Welcome to my game, you poor sod. You must have known going in
to this that I have no writing skills, so you have brought this upon
yourself. I guess I'll have to do something interesting to make up for
this.\n""")
print("""Sorry there's no saving at the moment, I'll add it once there's
something worth saving. Until then, enjoy this placeholder text.""")
print("If you want to start a new game, type new and press that enter key")
while(not compare("new")):
	print("""Come on, I know you can do it""")

