#Make a program that collects personal information from the user and displays it in a formatted profile card

first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
fav_number = float(input("Enter your favourite number: "))
Full_Name = first_name + " " + surname

print(f"Welcome, {Full_Name}!")
print(Full_Name.upper())
print(Full_Name.title())
print(age*12)
print(round(fav_number, 2))

print(type(f"Welcome, {first_name} {surname}!"))
print(type(first_name.upper()))
print(type(first_name.title()))
print(type(age*12))
print(type(round(fav_number, 2)))