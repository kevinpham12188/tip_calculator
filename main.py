print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? ")
tip_amount = input("How much tip would you like to give? 10, 12, or 15? ")
total_people = input("How many people to split the bill? ")
each_tip = (float(total_bill)/int(total_people)) * (int(tip_amount)/100)
each_bill = float(total_bill)/int(total_people)
each_pay = each_tip + each_bill
print("Each person should pay: " + str(round(each_pay, 2)))