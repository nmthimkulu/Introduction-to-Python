"""
#while loop
i = 0
while i < 3:
    print("meow")
    i += 1
"""

"""
#for loop
for i in range(3):
    print("meow")
"""

"""
while True:
    n = int(input("what's n? "))
    if n > 0:
        break
    
for i in range(n):
    print("meow")
"""
def main():
    number = get_number()
    meow(number)
    
    
def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for i in range(n):
        print("meow")
        
main()