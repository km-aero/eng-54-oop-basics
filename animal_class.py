# Define Animal class

# Characteristics of every animal
    # Heart, Brain, Name, Age, Colour

# Behaviours/Methods
    # eat, sleep, reproduce, potty, make_sound

class Animal():
# characteristics
    def __init__(self,name, age, colour):
        self.name = name
        self.__age = age
        self.colour = colour
        self.heart = True
        self.brain = True
        self.skills = {}

# Create a method that gets age and returns it
    def get_age(self): # getter method gives access to encapsulated resources without changing
        return self.__age

    def set_age(self, __age): # setter method allows you to change attribute
        # Shouldn't be able to change without being admin

        # fake verification
        password = input('Password?')

        if password == 'SuperSecret':
            self.__age = __age
            return True
        else:
            return False

#
    def __increment_age(self):
        self.__age += 1

# Methods below/Behaviours
    def eat(self):
        return 'Nom nom nom'

    def sleep(self):
        self.__increment_age()
        return 'zzZZZzzZzzzZZzZzzz'

    def reproduce(self):
        return 'I\'m going to need some privacy here ... x|'

    def potty(self):
        return '0_0 HUMMM!!! o_0 AHHHH!! SPLOSH! o_o'

    def make_sound(self):
        return 'Woof'

# created instance of class
ringo = Animal('ringo', 200, 'blueish') #

print(ringo)
print(type(ringo))

# Check methods
print(ringo.eat())
print(ringo.potty())
print(ringo.sleep())

# Check characteristics
print(ringo.name)
print(ringo.__age)
print(ringo.colour)
print(ringo.heart)
print(ringo.brain)