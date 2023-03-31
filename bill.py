import math
import random

while True: #Total of meal
  try:
    MealTotal = float(input("What is the total cost of your group's meal without tip?"))
    print(round(MealTotal,2))
    break
  except ValueError:
    print("The input was not valid. Please try again.")
    continue   # total of meal
while True:
  try:
    people_at_table = int(input("How many people are at your table?"))
    print(people_at_table)
    break
  except ValueError:
    print("The input was not valid. Please try again.")
    continue # people at table
while True:
  try:
    percent_table_tipping = float(input("What percent is the table tipping?"))
    print(percent_table_tipping)
    break
  except ValueError:
    print("The input was not valid. Please try again.")
    continue # percent table tipping
# the percent people are tipping

while True:
  try:
    TipSplit = str(input("If the tip is split evenly amongst everyone, type 'Yes'. If the tip is split proportionally to each person's meal, type 'No'.")).casefold()
    print(TipSplit)
    break
  except ValueError:
    print("The input was not valid. Please type 'Yes' or 'No'.")
    continue #group tip
while True: # sales tax percentage
  try:
    sales_tax_percentage = float(input("Enter the sales tax percentage of the area you are currently in: "))
    print(sales_tax_percentage)
    break
  except ValueError:
    print("The input was not valid. Please try again.")
    continue   # sales tax percentage
actualPercentage = (sales_tax_percentage/100)+1

def NameAndPrice():
  prePrice = []
  prices= []
  ogPrice = []
  splitTip = []
  names = []
  tip = MealTotal * (percent_table_tipping/100)
  while len(names) < people_at_table:
    name = str(input("Enter your name."))
    items = int(input("How many items did you have?"))
    x = range(0, items)
    TotalIndPrice = 0
    price2 = 0
    for i in x:
        price = float(input("Enter the price of the item."))
        prePrice.append(price)
        price2 += price
        print(round((price*actualPercentage),2))
        TotalIndPrice += round((price * actualPercentage),2)
    ogPrice.append(price2)
    prices.append((TotalIndPrice) + tip)
    print("Your total is " + str(TotalIndPrice))
    names.append(name)
  #TotalWithTip = MealTotal/people_at_table + tip
  if TipSplit == ("Yes").casefold():
    print("Each person owes " + str(tip) + " in tips.")
  elif TipSplit == ("No").casefold():
    for i in range(0,len(ogPrice)):
      splitTip.append(((ogPrice[i]/MealTotal)*tip))
      print(str(names[i]) + "'s total tip was " + str(splitTip[i]))
  print(ogPrice)
  print(names)
  print(prices)
  TotalPrice= sum(prePrice) 
  if TotalPrice != MealTotal:
    print("Your total before tax and tip is not equal to the bill. Please check again.")
    NameAndPrice()
  else:
    for i in range(0,len(prices)):
      print(str(names[i]) + "'s total was " + str(prices[i]))
    print("Everything matches up! The total before tax and tip was " + str(TotalPrice) + ".")
    print("Thank you! Hope you enjoyed your meal!")
NameAndPrice()
