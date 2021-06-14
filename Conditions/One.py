"""
  Price of a house is $1M. If buyer has good credit, they need to put down 10% otherwise
   they need to put down 20%.
  Print the down payment.
"""
price = 1000000
credit = input("Enter credit condition of the buyer either good or bad : ")

if credit == "good":
    pay1 = 0.1 * price
    print(f"Down payment is : {pay1}")
elif credit == "bad":
    pay2 = 0.2 * price
    print(f"Down payment payment is : {pay2}")
else:
    print("Invalid ! Type again.")