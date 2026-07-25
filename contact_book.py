# Build a command-line contact book
name = input("Enter your name: ").strip().title()
phone = int(input("Enter your phone number: "))
email = input("Enter your email: ").strip()
contact =  [{"name": name}, {"phone": phone}, {"email": email}]
contact.append(contact)
    
print(contact)


