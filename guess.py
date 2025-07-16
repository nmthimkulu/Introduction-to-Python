#variables
"""
guess = 10
print(guess)
"""
"""
def get_guess():
    guess = 10
    return guess

print(get_guess())
"""

def get_guess():
    guess = int(input("type guess: "))
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("correct!")
    else:
        print("incorrect!")

main()