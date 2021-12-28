"""CP1404/CP5632 Practical - Client code to use the Car class."""

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


# 1.
limo = Car(100)
# 2.
limo.add_fuel(20)
# 3.
print(f"Limo's fuel =. {limo.fuel} units")
# 4.
limo.drive(115)
# 5.
print(f"Limo's odometer => {limo.odometer} km travelled")
# 6.
print_car = Car(42)
print_car.odometer = 277
print(print_car)  # Car, fuel=42, odometer=277
# 7.
limo = Car("limo", 100)
limo.odometer = 115
print(limo)  # limo, fuel=100, odometer=115
another_car = Car("another car", 100)
another_car.add_fuel(50)
another_car.drive(125)
print(another_car)  # my car, fuel=25, odometer=125
# 8.
print(limo)
print(Car())


main()
