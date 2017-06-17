class Person(object):
	def __init__(self, name):
		self.name = name


Joe = Person("Joe")
Matilda = Person("Matilda")
Beatrice = Person("Beatrice")
Fran = Person("Fran")


players = [Joe, Matilda, Beatrice, Fran]






def duck_duck_goose(players, goose):
    
	goose = goose - 1
	
	if goose > len(players):
		goose = goose % len(players)

	print players[goose].name





duck_duck_goose(players, 6)
