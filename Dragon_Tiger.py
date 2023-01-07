import random
import collections

def cards_sum(lis):
    total=0
    for i in lis:
        last_digit=int(i[-1])
        total+=last_digit
    if total>9:
        return total%10
    return total
cards_deck=[]
clubs=["♣️A01","♣️️02","♣️️03","♣️04","♣️️05","♣️06","♣️️07","♣️️08","♣️️09","♣️️10","♣️️J11","♣️️Q12","♣️️K13"]
diamonds=["♦️A01","♦️02","♦️03","♦️04","♦️05","♦️06","♦️07","♦️08","♦️09","♦️10","♦️J11","♦️Q12","♦️K13"]
hearts=["❤️A01","❤️02","❤️03","❤️️04","❤️️05","❤️06","❤️07","❤️️08","❤️09","❤️️10","❤️️J11","❤️️Q12","❤️️K13"]
spades=["♠️A01","♠️️02","♠️️03","♠️04","♠️️05","♠️️06","♠️️07","♠️️08","♠️️09","♠️️10","♠️️J11","♠️️Q12","♠️️K13"]
for _ in range(6):
    cards_deck.extend(clubs)
    cards_deck.extend(diamonds)
    cards_deck.extend(hearts)
    cards_deck.extend(spades)
print(cards_deck)
print(len(cards_deck))
for _ in range(3):
    random.shuffle(cards_deck)
cards_deck.pop(0)
print(cards_deck)
game_number=1
first_card_wins=0
second_card_wins=0
# slots=[0,0,0,0,0,0]
while len(cards_deck)>=35:
    first_card=cards_deck.pop(0)
    first_card_number=int(first_card[-2:])
    second_card=cards_deck.pop(0)
    second_card_number = int(second_card[-2:])
    print("gamecount------>",game_number)
    game_number+=1
    print("fcard           scard")
    print(first_card,"           ",second_card)
    if first_card_number > second_card_number:
        first_card_wins+=1
        print("first card wins")
    elif first_card_number < second_card_number:
        second_card_wins+=1
        print("second card wins")
    else:
        print("Tie")
print("first card wins =",first_card_wins)
print("second card wins =",second_card_wins)


