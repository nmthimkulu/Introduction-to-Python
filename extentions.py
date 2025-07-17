"""
In a file called extensions.py, 
implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, 
case-insensitively, in any of these suffixes:
"""

def file():
    extention = input("Enter File name: ").lower()
    
    if ".gif" in extention:
        print("image/gif")
    elif ".jpg" in extention:
            print("image/jpg")
    elif ".jpeg" in extention:
            print("image/jpeg")
    elif ".png" in extention:
            print("image/png")
    elif ".pdf" in extention:
            print("text/pdf")
    elif ".txt" in extention:
            print("text/txt")
    elif ".zip" in extention:
            print("text/zip")
    else:
            print("appllication error")  
   
file()     
    
