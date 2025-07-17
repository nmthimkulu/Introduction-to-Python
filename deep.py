""""
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, 
the Universe and Everything,
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. 
Otherwise output No.
"""

def deep():
    prompt = input("What is the Answer to the Great Question of Life, the Unviverse and Everything? ").lower().replace("-", " ")
    
    if prompt == 42 or prompt == "forty two":
        print("Yes")
    else:
        print("No")

deep()
    