"""CP1404/CP5632 Practical - guitars client program."""


from guitar import Guitar

guitars = []

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} added.")
    name = input("Name: ")

print("\n... snip ...\n")
print("These are my guitars:")
for i, guitar in enumerate(guitars):  # enumerate can also take a second parameter, the starting number for iteration
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")