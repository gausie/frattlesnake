from frattlesnake import frattlesnake, Familiar

frattlesnake.init()
login = frattlesnake.login("gausie")

my_familiar = Familiar.mine()
print(my_familiar.hatchling.name)