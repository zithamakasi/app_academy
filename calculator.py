#Built a python calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add = num1 + num2
print(add)
print(round(add, 2))

sub = num1 - num2
print(sub)
print(round(sub, 2))

mult = num1 * num2
print(mult)
print(round(mult, 2))

if num2 != 0:
    divi = num1 / num2
    print(divi)
    print(round(divi, 2))

    divii =  num1 // num2
    print(divii)
    print(round(divii, 2))

    per = num1 % num2
    print(per)
    print(round(per, 2))
else:    
    print("Second number cannot be 0, please enter another number")
    

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Calculator Results $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 
print(f"| {'Operation':<43} | {'Result':<47} |") 
print(f"| {'$'*45}|{'$'*49}|") 
print(f"| {'Add':<43} | {add:<47} |") 
print(f"| {'Sub':<43} | {sub:<47} |") 
print(f"| {'Mult':<43} | {mult:<47} |") 
print(f"| {'Divi':<43} | {divi:<47} |") 
print(f"| {'Divii':<43} | {divii:<47} |") 
print(f"| {'Per':<43} | {per:<47} |")
