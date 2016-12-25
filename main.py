from Polymorphism import Animal, Dog, Cat

def run_twice(animal):
	animal.run()
	animal.run()

amimal = Animal()
amimal.run()

run_twice(Dog())
