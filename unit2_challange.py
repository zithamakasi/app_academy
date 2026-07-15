#Creating a secure password hint tool.
password = input("Enter your password: ").strip()
word = password[0]
secure = password[-1]

print(f"Your password hint: It starts with {word.upper()} and ends with {secure.upper()}.")