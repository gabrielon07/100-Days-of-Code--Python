print("Welcome to the tip calculator!")

bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

total = round(float(bill)*float(1+float(tip)/100),2) 
total_per_person = round(float(total) / float(people),2)  

print(f"Each person should pay: $ {total_per_person}")