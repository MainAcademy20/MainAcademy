class Building:
    def __init__(self, color, material, number, place=0):
        self.color = color
        self.material = material
        self.number = number
        self.place = place

    @staticmethod
    def create_red_house(number):
        return Building("red", "brick", number) # статический метод класса

    def __str__(self):
        return "<{} building built with {} {}>".format(
            self.color, self.number, self.material)

    def add_material(self, increase):
        self.number += increase

b1 = Building("red", "stone", 10)
b2 = Building("black", "brick", 12)
b1.add_material(40)
print(b1)
print(b2)

