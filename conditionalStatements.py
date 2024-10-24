# if ....else... statement
votes = int(input("Enter the votes"))
if votes > 50000:
    print("You are elected as President")
    print("Startint 2024 upto 2028")
else:
    print("You are not elected as President")
marks = float(input("Kewy in the marks"))
if marks > 80 and marks <=100:
     print("You have a grade A")
elif marks> 70 and marks <=80:
     print("You have a grade B")
elif marks> 60 and marks <=70:
     print("You have a grade C")
elif marks> 50 and marks <=60:
     print("You have a grade D")
elif marks> 40 and marks <=50:
     print("You have a grade E")
elif marks> 20 and marks <=40:
     print("You have a grade F")
elif marks>0 and marks <=20:
     print("You have failed")
else:
     print("Enter a value between 0 and 100")

# create an atm machine that awards discounts  to users depending on their
# withdrawal amount and display the total amount inclusive of the discounts.
# Withdrawal above 10,000 award a discount of 15%, withdrawal above 5000 give
# a discounts of 10% and lastly a withdrawal of above 2000 give a discount of 5%
withdrawal = float(input("Enter the amount of withdrawal "))
if withdrawal >10000:
    print("Total withdrawal is", withdrawal * 0.85)
    print("Total discount is" ,withdrawal * 0.15)
elif withdrawal >5000 and withdrawal<=10000:
    print("Total withdrawal is", withdrawal * 0.90)
    print("Total discount is", withdrawal * 0.10)
elif withdrawal>2000 and withdrawal<=5000:
    print("Total withdrawal is", withdrawal * 0.95)
    print("Total discount is", withdrawal * 0.05)
else:
    print("Withdrawal out range")