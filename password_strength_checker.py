#PASSWORD STRENGTH CHECKER

print("-Password must inlude be between 8-16 characters long")
print("-Password must contain atleast one capital letter")
print("-Password must contain atleast one digit")
print("-Password must contain atleast one special character (!, @, #, $, %, &, *, ?)")
print("-Password can not contain spaces")

#Variables/Lists
special = ['!', '@', '#', '$', '%', '&', '*', '?']
points = 0
valid_password = True

#Password input
password = input("Please enter your password: ")


#Restrictions check (Error messages and strength determiner)
for char in password: #Checking for spaces
    if char == ' ':
        print("Password may not contain spaces.")
        valid_password = False

if len(password) < 8: #Checking password length
    print("Password not long enough.")
    valid_password = False
elif len(password) > 16:
    print("Password too long.")
    valid_password = False
elif 8 <= len(password) < 12:
    points += 1
elif 12 <= len(password) < 15:
    points += 2
else:
    points += 3

has_special = False
special_count = 0
for char in password: #Checking for special characters
    if char in special:
        points += 1
        has_special = True
        special_count += 1
    if special_count == 3:
        break
if has_special == False:
    print("Password must include special character")
    valid_password = False

has_digit = False
digit_count = 0
for char in password: #Checking for digits
    if char.isdigit():
        points += 1
        has_digit = True
        digit_count += 1
    if digit_count == 3:
        break
if has_digit == False:
    print("Password must include a digit")
    valid_password = False

checking_case = ''
for char in password: #Checking for capital letters
    if char.isdigit() == False and char not in special:
        checking_case += char
if checking_case.islower() == True or checking_case == '':
    print("Password must contain a capital letter")
    valid_password = False
else:
    points += 1


#Password strength
if valid_password == True:
    if 4 <= points <= 6:
        print("Weak password")
    elif 6 < points <= 8:
        print("Moderate password")
    elif points >= 9:
        print("Strong password")
        
        



        
