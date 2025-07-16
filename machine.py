emotion = "V_V"

def main():
    global emotion
    say("Hi, there?")
    emotion = "v.v"
    say("oh, its you again")



def say(phrase):
    print(phrase + " " + emotion)

main()