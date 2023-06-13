class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.walk = self.pet.play()
        return self

    def feed(self):
        self.feed = self.pet.eat()
        return self

    def bathe(self):
        self.bathe = self.pet.noise()
        return self
