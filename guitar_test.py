"""CP1404/CP5632 Practical - Guitar class test."""

from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(gibson)
another_guitar = Guitar("Another Guitar", 2013, 1650.30)
print(another_guitar)

print(f"Gibson L-5 CES get_age() - Expected 98. Got {gibson.get_age()}")
print(f"Another Guitar get_age() - Expected 7. Got {another_guitar.get_age()}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}")