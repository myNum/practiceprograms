import random

print "Give me a quarter, and I'll tell you your fortune."

question = raw_input("Or you could just ask a question. \n> ")

response = ["Huh?",
            "Speak up! I can't hear you!",
            "Dumb question. Try again.",
            "Reception poor. Ask again.",
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
            "Doubtful",
            "BINGO!"]

print (random.choice(response))