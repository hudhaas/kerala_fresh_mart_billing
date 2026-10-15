name=input("Customer name: ")
item=input("Item name: ")
qty=int(input("Quantity: "))
price=int(input("Price per unit (Rs): "))
member=input("Loyalty member? [y/n]: ")
payment=input("Payment mode (cash/upi/card): ")
amount=qty*price
dis=0

member=="y"
y=0


print("=" *50)
print("KERALA FRESH MART".center(50) + "\n" + "SMART BILLING".center(50) + "\n" + "=" *50)

print(" " *50)

print(f"Customer: {name}")
print("-" *50)
print(f"{'Item'}{'Qty':>21}{'Price':>12}{'Amount':>13}")
print(f"{item}{qty:>15}{price:>13,.2f}{amount:>13,.2f}")

print("-" *50)
print(f"Amount: {amount:>42,.2f}")



if(amount >=2000):
  print(f"Discount rate: {'10%':>35}")
  dis=amount*.1
elif(amount >=1000 and amount <2000):
  print(f"Discount rate: {'5%':>35}")
  dis=amount*.05
elif(amount >=500 and amount <1000):
  print(f"Discount rate: {'2%':>35}")
  dis=amount*.02
else:
  print(f"Discount rate: {0:>34.1%}")
print(f"Discount :{dis:>40,.2f}")



if(amount >=500 and member.lower()=="y"):
  y=25
  print(f"{'Loyalty bonus:'}{y:>36,.2f}")
else:
  print(f"{'Loyalty bonus:'}{0:>36.2f}")

ta= amount-dis-y

print(f"Taxable amount:{ta:>35,.2f}")


gst=ta*0.05

print(f"GST (5%):{gst:>41,.2f}")

total=ta+gst

print(f"Grand total:{total:>38,.2f}")
print("=" *50)
