"""
In a file called interpreter.py, 
implement a program that prompts the user for an arithmetic expression and 
then calculates and outputs the result as a floating-point value formatted to one decimal place. 
Assume that the user’s input will be formatted as x y z, 
with one space between x and y and one space between y 
and z, wherein:
"""

def main():
    x, y, z = input("Expression: ").split(" ")
    if math(x, y, z):
        print(x, y)
        
        
                
def math(a, b, c):
    a = float(a)
    c = float(c)
    if b == "+":
        print(round(a + c,1))
    elif b == "-":
        print(round(a - c,1))
    elif b == "*":
        print(round(a * c,1))
    else:
        print(round(a / c,1))



main()