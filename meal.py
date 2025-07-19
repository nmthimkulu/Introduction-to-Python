"""
In meal.py, implement a program that prompts the user for a time and outputs 
whether it’s breakfast time, 
lunch time, or dinner time. 
If it’s not time for a meal, don’t output anything at all. 
Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. 
And assume that each meal’s time range is inclusive. 
For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, 
it’s time for breakfast.
"""

def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("Breakfast Time")
    elif 12 <= time <= 13:
        print("Lunch Time")
    elif 18 <= time <= 19:
        print("Dinner time")

    
def convert(time):
    hour, minutes = time.split(':')
    return float(hour) + (float(minutes)/60)
    
    

main()

