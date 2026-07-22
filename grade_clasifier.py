name_learner = input("Enter you name: ")
mark1 = float(input("Enter your mark: "))
mark2 = float(input("Enter your second mark: "))
mark3 = float(input("Enter your third mark: "))
sum = mark1 + mark2 + mark3
list = [mark1, mark2, mark3]
average_mark = sum / int(len(list))
print(average_mark)
letter_grade = average_mark

if letter_grade >= 80:
    letter_grade = "A"
    print(letter_grade)
   
elif letter_grade >= 70 and letter_grade <= 79:
    letter_grade = "B"
    print("B")
    
elif letter_grade >= 60 and letter_grade <= 69: 
    letter_grade = "C"
    print("C")

elif letter_grade >= 50 and letter_grade <= 59:
    letter_grade = "D"
    print("D")
    
else:
    letter_grade < 50
    letter_grade = "F"
    print("F")
    
if average_mark >= 50:
    assign_status = "Pass"
    print(assign_status)
else:
    assign_status = "Fail"
    print("Fail")         
 
intervention = "The test score that has below 40 needs intervention"    
if (mark1 < 40 and mark2 < 40) or mark3 < 40:
    print(intervention)    
    
print("-------------------------------------------------Report Card ------------------------------------------------------") 
print(f"|{"Input":<50} | {"Result":<59} |") 
print(f"|{"-"*51}|{"-"*61}|") 
print(f"|{"Name":<50} | {name_learner:<59} |") 
print(f"|{"Mark1":<50} | {mark1:<59} |") 
print(f"|{"Mark2":<50} | {mark2:<59} |") 
print(f"|{"Mark3":<50} | {mark3:<59} |") 
print(f"|{"Average_mark":<50} | {average_mark:<59} |") 
print(f"|{"Letter_grade":<50} | {letter_grade:<59} |")    
print(f"|{"Assign_status":<50} | {assign_status:<59} |") 
