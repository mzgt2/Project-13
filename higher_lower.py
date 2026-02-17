import random
from art import logo
from art import vs
from game_data import data

# need to choose a random element from game data
# compare a against b to see which is higher
# if you guess right then you keep the winning answer to compare to the next random element
# if you guess wrong then you lose and the game ends there
game_end = False
current_score = 0
print(logo)


A = random.choice(data)
print(f"Compare A: {A['name']}, {A['description']}, {A['country']}")


print(vs)
B = random.choice(data)
print(f"Against B: {B['name']}, {B['description']}, {B['country']}")




while not game_end:

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == 'a':
        if A['follower_count'] > B['follower_count']:
            print("\n" * 20)
            print(logo)
            current_score += 1
            print(f"Correct answer! Your score is {current_score}.")
            A = A
            print(f"Compare A: {A['name']}, {A['description']}, {A['country']}")
            print(vs)
            B = random.choice(data)
            print(f"Against B: {B['name']}, {B['description']}, {B['country']}")
        else:
            game_end = True
            print(f"Wrong answer. Your final score is {current_score}")
    elif guess == 'b':
        if B['follower_count'] > A['follower_count']:
            print("\n" * 20)
            print(logo)
            current_score += 1
            print(f"Correct answer! Your score is {current_score}.")
            A = B
            print(f"Compare A: {A['name']}, {A['description']}, {A['country']}")
            print(vs)
            B = random.choice(data)
            print(f"Against B: {B['name']}, {B['description']}, {B['country']}")
        else:
            game_end = True
            print(f"Wrong answer. Your final score is {current_score}")
