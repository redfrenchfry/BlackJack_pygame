#BlackJack




 #imports

import random












# print commands






#data and stuffs
class g:
    cash = 100
    bet = 0
    card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_number1 = random.choice(card_values)
    random_number2 = random.choice(card_values)
    numbers = random_number1 + random_number2
# functions
def save_cash(score):
    x = open(".save_data.TXT","w")
    x.write(score)
    x.close()
def load_cash():
    try:
        x = open(".save_data.TXT","r")
        return int(x.read())
    except:
        x = open(".save_data.TXT","w")
        x.write("100")
        x.close()
        return 100
def draw_card():
    random_number = random.choice(g.card_values)
    next_number = random_number
    g.numbers = g.numbers + next_number
    print(f"{next_number} is the card you drew\n")
    print(g.numbers)

g.cash = load_cash()
print(f"\033[92m {g.random_number1} and {g.random_number2} are your cards. \033[0m ")    
# hitOrStay = input("Do You want to Hit or Stay? ")
while g.numbers < 21:
    print(f'\033[94mcash is {g.cash}\033[93m')
    bet = input("\033[93mBet up\033[0m ")
    g.cash -= int(bet)
    g.bet = int(bet)
    save_cash(str(g.cash))
    hitOrStay = input("Do You want to Hit or Stay? ")
    if hitOrStay == "Hit":
        draw_card()
    elif hitOrStay == "Stay":
        print("Ok\n")        
    else:
        print('Ok, please try again. Remember to make the first letter CAPITOL ( "Hit" or "Stay")')
        exit()
    if g.numbers < 21:
        if g.numbers > 21:
            print('Rip, you lose\n')
            break
        if g.numbers == 21:
            print(f'You WIN! cash is {g.cash}\n')
            g.cash += g.bet*2
            break





#more print command
print(f'cash was {g.cash}')
print ("Game is over.")
print('Rerun to play again.')
