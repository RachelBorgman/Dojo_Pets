import ninja

# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

class Pet:
    def __init__(self, name , type , tricks, sound, energy=0, health=0):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.energy = energy
        self.health = health
    
    def sleep(self):
        self.energy =+ 25
        print(self.health)
        return self

    def eat(self):
        self.energy =+ 5
        self.health =+10
        print(self.energy)
        print(self.health)
        return self

    def play(self):
        self.health =+5
        print(self.health)
        return self

    def noise(self):
        print(self.sound)
        return self
    
class Lab(Pet):
    def __init__(self, name, tricks, type, sound, energy, health, is_hungry):
        super().__init__(name, tricks, type, sound, energy, health)	
        self.is_hungry = is_hungry


# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound

pet_gert = Pet("Gert", "Poodle", "sit, shake", "woof!")
ninja_rachel = ninja.Ninja("Rachel","Borgman","pupperoni", "Iams", pet_gert)

ninja_rachel.feed()
ninja_rachel.walk()
ninja_rachel.bathe()

pet_jeff = Lab("Jeff", "cuddle and eat", "Lab", "Zzzzzz", energy=0, health=50, is_hungry=True)
pet_jeff.play()
print(pet_jeff.is_hungry)