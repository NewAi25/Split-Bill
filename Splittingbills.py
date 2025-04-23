# printing a Welcome message for the user#
print("Welcome to the Bil Calculator")
#take input from the user#
bill_amount = float(input("What is your bill amount? "))
tip = int(input("What is the percentage of tip you would like to give?10,12 or 15 "))
number_of_people = int(input("How many people will split the bill? "))
#calculate the bill#
tip_percent= tip/100
tip_percent +=1
total_bill =round((bill_amount*tip_percent),2)
#print the final split bill#
print(f"Each person should pay {total_bill}")
