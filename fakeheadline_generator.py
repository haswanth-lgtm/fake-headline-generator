import random

subjects = [
    "sharukan",
    "virat kohli",
    "nirmala sitharaman",
    "A mumbai cat",
    "A group of monkeys",
    "prime minister modi",
    "auto rickshaw driver from delhi"
        ]

actions  = [
    "launches",
    "cancels",
    "eats",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"

]   

places_or_things = [
    "at red fort",
    "in mumbai local train",
    "a plate of biryani",
    "inside a parliment",
    "at ganga ghat",
    "during a ipl match",
    "at india gate",


]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want to generate another headline? (yes/no): ").strip().lower()
    if user_input == "NO":
        break

    print("\nThanks for using the Fake Headline Generator! Goodbye!")