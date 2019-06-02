class Animal:
    
    def __init(self,name,species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"Hey, I'm {self.name} the {self.species}")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 'Cat')

    def greet(self):
        print(f"Meow! {self.name} the {self.species}")

class FriendlyCat(Cat):

    def greet(self):
        msg = super().greet()
        print(msg + "you seem awesome")


fido = Cat("Sally")
fido.greet()
