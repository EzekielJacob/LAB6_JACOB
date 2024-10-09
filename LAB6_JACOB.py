Status = input("Enter Status: (type member or non-member only) ")
age = int(input("Enter age: "))

if age >=1 and age <= 18:
    if Status=="member":
        print("Your fee is 450.00 pesos")
    if Status=="non-member":
        print("Your fee is 650.00 pesos")
    else:
        print("syntax error")
        
elif age > 18 and age < 65:
    if Status=="member":
        print("Your fee is 550.00 pesos")
    if Status=="non-member":
        print("Your fee is 750.00 pesos")
    else:
        print("syntax error")
        
elif age >= 65 and age <= 120:
    if Status=="member":
        print("Your fee is 400.00 pesos")
    if Status=="non-member":
        print("Your fee is 600.00 pesos")

else:
    print("You did not follow the instruction")