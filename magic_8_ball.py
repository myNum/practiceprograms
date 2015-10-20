import random

print "Give me a quarter, and I'll tell you your fortune."

question = raw_input("Or you could just ask a question. \n> ")

def magic_eight():
            response = ["Huh?",
                        "Speak up! I can't hear you!",
                        "BINGO!",
                        "Dumb question.",
                        "Reception poor. Try again later.",
                        "You really don't want to know the answer, so I'm just going to pretend you didn't ask that.",
                        "Maybe?",
                        "Hell yes!",
                        "Sure",
                        "Yepper!",
                        "You know it!",
                        "If you're lucky.",
                        "Green means go.",
                        "Eh",
                        "Could be.",
                        "Fuck no.",
                        "No, no, no.",
                        "Yeah, and monkeys might fly out of my butt.",
                        "Outlook not so good. Actually, outlook quite awful.",
                        "Doubtful",]

            print (random.choice(response))

magic_eight()

while True:

    another_question = raw_input("Would you like ask another question? Y or N \n")

    if another_question.lower() in ["y", "yes"]:
        question_two = raw_input("Ask away! \n> ")
        magic_eight()
    elif another_question.lower() in ['n', 'no']:
        print "Later Alligator"
        break
    else:
        print "Im sorry, I did not understand that"
        continue
