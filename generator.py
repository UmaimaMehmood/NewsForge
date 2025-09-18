import random

subjects = [
    "A group of penguins",
    "Local grandma",
    "A confused tourist",
    "A team of squirrels",
    "The neighborhood cat",
    "A group of students",
    "An angry goose",
    "A talking fridge"
]

actions = [
    "declares a holiday for",
    "starts dancing in",
    "accidentally eats",
    "bans the use of",
    "challenges everyone to",
    "organizes a party at",
    "claims ownership of",
    "falls asleep inside"
]

places_or_things = [
    "a shopping mall",
    "a giant sandwich",
    "the city fountain",
    "a donut factory",
    "a moving bus",
    "a secret treehouse",
    "the library",
    "a pizza shop"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}!"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        print("\nThanks for using the NewsForge. Have a fun day!")
        break

