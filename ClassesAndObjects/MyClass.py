# Demonstration of Classes and Objects


class Vehicle:
    kind = "Vehicle"

    def __init__(self, name, tyres, color, price, steering):
        self.name = name
        self.tyres = tyres
        self.color = color
        self.price = price
        self.steering = steering

    def VehFunc(self):
        return "The {} is of color {} which has {} tyres, with {} steering and priced at {}. The kind is of {}.".format(self.name, self.color, self.tyres, self.steering, self.price,
                                                       self.kind)


obj1 = Vehicle("Camry", 4, "Red", 28000.00, "Powered")

print(obj1.VehFunc())
