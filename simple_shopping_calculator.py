p1 = int(input("Enter price of item1: "))
q1 = int(input("Enter quantity of item1: "))
p2 = int(input("Enter price of item2: "))
q2 = int(input("Enter quantity of item2: "))
p3 = int(input("Enter price of item3: "))
q3 = int(input("Enter quantity of item3: "))

print(f"Item 1 : {p1} x {q1} = {p1*q1} ")
print(f"Item 2 : {p2} x {q2} = {p2*q2} ")
print(f"Item 3 : {p3} x {q3} = {p3*q3} ")

subtotal = (p1*q1)+(p2*q2)+(p3*q3)
print(f"Subtotal = {subtotal}")
tax = 8.5
result = (subtotal*tax)/100
print(f"Tax (8.5%) = {result}")
print(f"Total = {subtotal+result}")