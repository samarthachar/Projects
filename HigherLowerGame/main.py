import art
import random
from game_data import data

def same():
    global a,b
    if a == b:
        b = random.choice(data)
        same()


def game_control(answer, a, b):
    try:
        if answer == "a":
            return a["follower_count"] >= b["follower_count"]
        elif answer == "b":
            return b["follower_count"] >= a["follower_count"]
        else:
            return False
    except:
        return False


a = random.choice(data)
b = random.choice(data)

print(art.logo)
game_on = True
score = 0
while game_on:
    same()
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.\n")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    inp = input("Who has more followers? Type 'A' or 'B': ").lower()
    ans = game_control(inp,a,b)
    a = b
    b = random.choice(data)
    print("\n" * 50)
    print(art.logo)
    if ans:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_on = False
print(f"Sorry, that's wrong. Final score: {score}")