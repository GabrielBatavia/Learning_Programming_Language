# Source
from game_data import data
from art import logo
from art import vs
import random
account = {}
right_guess = True
still_continue = False
point = 0


# All function

def get_compare():
    """This function will make random accounts for comparison

    Returns:
        _dict_: _the account of the famous person_
    """
    global account
    account = random.choice(data)
    return account

def account_name_print(first_account, second_account):
    account_name1 = first_account["name"]
    account_name2 = second_account["name"]
    account_desc1 = first_account["description"]
    account_desc2 = second_account["description"]
    account_country1 = first_account["country"]
    account_country2 = second_account["country"]
    
    print(logo)
    print(f"The first account is {account_name1}, a {account_desc1}, from {account_country1}")
    
    print(vs)
    print(f"The second account is {account_name2}, a {account_desc2}, from {account_country2}")
    
def compare_followers(compare, guess):
    global right_guess, point, still_continue
    
    accountcompare_followers = compare["follower_count"]
    accountguess_followers = guess["follower_count"]
    
    if accountcompare_followers > accountguess_followers:
        print("Your wrong")
        right_guess = False
        return right_guess
    else:
        print("You correct")
        point += 1
        still_continue = True

def main_game():
    while right_guess:
        
        
        account1 = get_compare()
        account2 = get_compare()  
        if account1 == account2:
            account2 = get_compare()

        if still_continue == True:
            account1 = user_account
            
        account_name_print(account1, account2)

        user_guess = input("Which one have more following accounts? 1 or 2? : ")

        if user_guess == "1":
            user_account = account1
            compare_account = account2
        else:
            compare_account = account1
            user_account = account2

        print()
        compare_followers(compare_account, user_account)
        
        print(f"Your point is {point}")

# MAIN
main_game()