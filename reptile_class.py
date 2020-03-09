from animal_class import *

class Reptile(Animal):

    def __init__(self,name,age,colour, scales, blood_temp):
        super().__init__(name, age,colour)
        self.scales = scales
        self.blood_temp = blood_temp

    def make_sound(self):
        return 'ZLSLZSLZSLZLSZLSZLSZPYTHON'


animal1 = Animal('Nacho', 20, 'Yellowish')

reptile1 = Reptile('Ringo',30,'yellowish', 'lots', 'very cold')