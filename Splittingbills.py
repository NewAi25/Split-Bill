print("Welcome to the Bil Calculator")
bill_amount = float(input("What is your bill amount? "))
tip = int(input("What is the percentage of tip you would like to give?10,12 or 15 "))
number_of_people = int(input("How many people will split the bill? "))
tip_percent= tip/100
tip_percent +=1
total_bill =round((bill_amount*tip_percent),2)
print(f"Each person should pay {total_bill}")

