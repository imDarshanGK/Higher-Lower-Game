import random
import logo_art
import game_Database
import os

print(logo_art.logo)
score = 0
def display_accountinfo(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, follower1, follower2):
    if follower1 < follower2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False
        
account2 = random.choice(game_Database.data)
continu_flag = True

while continu_flag:
    account1 = account2
    account2 = random.choice(game_Database.data)
    while account1 == account2:
        account2 = random.choice(game_Database.data)
    print(f"Compare 1: {display_accountinfo(account1)}")
    print(logo_art.vs)
    print(f"Compare 2: {display_accountinfo(account2)}")
    guess = int(input("Who has more followers? Type 1 or 2: "))
    followers_count_1 = account1["followers"]
    followers_count_2 = account2["followers"]

    is_correct = check_answer(guess, followers_count_1,followers_count_2)
    os.system('cls')
    print(logo_art.logo)
    if is_correct:
        score +=1
        print(f"You are right. Your score is: {score}")
    else:
        print(f"You are wrong. Your final score is: {score}")
        continu_flag = False