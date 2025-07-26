def celcius_to_fahrenheit(c):
    print(f"{c} C = {(c*(9/5))+32} F")


def fahrenheit_to_kelvin(f):
    print(f"{f} F = {(f-32)*(5/9)+273.15} K")

    
def kelvin_to_celcius(k):
    print(f"{k} K = {(k-273.15):.2} C")
    
celcius_to_fahrenheit(0)
fahrenheit_to_kelvin(32)
kelvin_to_celcius(300)