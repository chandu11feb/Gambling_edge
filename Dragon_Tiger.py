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
# cards_deck.pop(0)
cards_deck=cards_deck[12:]
print(cards_deck)
game_number=1
first_card_wins=0
second_card_wins=0
results_list=[]
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
        results_list.append("F")
        print("first card wins")
    elif first_card_number < second_card_number:
        second_card_wins+=1
        results_list.append("S")
        print("second card wins")
    else:
        results_list.append("T")
        print("Tie")
print("first card wins =",first_card_wins)
print("second card wins =",second_card_wins)
print(results_list)

prev_winner=results_list[0]

bet_amt=50
bet_wins=0
bet_loses=0
total_current_amount=50
current_amount_list=[]
bet_amount_list=[]
# -----------------prev_winner card --------------
for i in range(1,len(results_list)):
    bet_amount_list.append(bet_amt)
    if results_list[i]==prev_winner and results_list[i] != "T" :
        prev_winner=results_list[i]
        total_current_amount+=bet_amt
        current_amount_list.append(total_current_amount)
        bet_wins+=1
        bet_amt=50
    else:
        if results_list[i]=="T":
            total_current_amount -= bet_amt
        else:
            bet_loses+=1
            prev_winner=results_list[i]
            total_current_amount-=bet_amt
            current_amount_list.append(total_current_amount)
            bet_amt=bet_amt*3
            if bet_amt>100000:
                bet_amt=100000
# -----------------alternate card --------------
# for i in range(1,len(results_list)):
#     if prev_winner=="F":
#         prev_winner="S"
#     else:
#         prev_winner="F"
#     bet_amount_list.append(bet_amt)
#     if results_list[i]==prev_winner and results_list[i] != "T" :
#         total_current_amount+=bet_amt
#         current_amount_list.append(total_current_amount)
#         bet_wins+=1
#         bet_amt=100
#     else:
#         if results_list[i]=="T":
#             pass
#         else:
#             bet_loses+=1
#             total_current_amount-=bet_amt
#             current_amount_list.append(total_current_amount)
#             bet_amt+=bet_amt
#             # if bet_amt>=5000:
#             #     bet_amt=5000
print("bet_amount_stats",bet_amount_list)
print("max bet amount :",max(bet_amount_list)," , min bet amount : ",min(bet_amount_list))
print("current amount stats",current_amount_list)
print("max current amount :",max(current_amount_list)," , min current amount : ",min(current_amount_list))
print("betwins : ",bet_wins)
print("betloses : ",bet_loses)
print("final amount : ",total_current_amount)


