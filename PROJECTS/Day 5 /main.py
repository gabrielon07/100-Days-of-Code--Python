import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Wellcome to the Password Generator")
nr_letters = int(input("How many letter would you like in you password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

#Eazy Level
''' password = ""
for char in range (1, nr_letters + 1):
    password += random.choice(letters)
    
for symb in range (1, nr_symbols + 1):
    password += random.choice(symbols)
   

for numb in range (1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)
'''

#hard level 

passworld_list = []

for char in range (1, nr_letters + 1):
    passworld_list += random.choice(letters)
    
for symb in range (1, nr_symbols + 1):
    passworld_list += random.choice(symbols)
   

for numb in range (1, nr_numbers + 1):
    passworld_list += random.choice(numbers)



password = ""

for char in passworld_list:
     password += char   

print(f"You password is: {password}")   