

class Mammal():
    def __init__(self, name, role, viviparous=True):
        self.name = name
        self.role = role
        self.viviparous = viviparous

        
class Human(Mammal):
    def __init__(self, name):
        super().__init__(name, role='omnivorous')


class Dog(Mammal):
    def __init__(self, name, breed, color, size):
        super().__init__(name, role='predator')
        self.breed = breed
        self.color = color
        self.size = size



if __name__ == '__main__':