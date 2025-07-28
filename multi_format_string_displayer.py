name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")


print(f"My name is {name}! I am  {age} years old and live in {city}.")
print("My name is %s! I am %i years old and live in %s." % (name, age, city))
print("My name is {0}! I am {1} years old and live in {2}.".format(name, age, city))
