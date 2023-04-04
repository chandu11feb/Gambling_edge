import random
import collections
from collections import Counter
import numpy as np


def cards_sum(lis):
    total=0
    for i in lis:
        last_digit=int(i[-1])
        total+=last_digit
    if total>9:
        return total%10
    return total
def cards_value(lis):
    temp_lis=[]
    for i in lis:
        temp_lis.append(int(i[-2:]))
    return temp_lis

def Sort_dict_reverse(dictionary):
    keys=list(dictionary.keys())
    values=list(dictionary.values())
    sorted_value_index=np.argsort(values)
    sorted_value_index_list=list(sorted_value_index)
    sorted_value_index_list.reverse()
    final_dict ={keys[i] : values[i] for i in sorted_value_index_list}
    return final_dict

cards_deck=[]
clubs=["♣️A01","♣️️02","♣️️03","♣️️04","♣️️05","♣️️06","♣️️07","♣️️08","♣️️09","♣️️10","♣️️J10","♣️️Q10","♣️️K10"]
diamonds=["♦️A01","♦️02","♦️03","♦️04","♦️05","♦️06","♦️07","♦️08","♦️09","♦️10","♦️J10","♦️Q10","♦️K10"]
hearts=["❤️A01","❤️02","❤️03","❤️️04","❤️️05","❤️06","❤️07","❤️️08","❤️09","❤️️10","❤️️J10","❤️️Q10","❤️️K10"]
spades=["♠️A01","♠️️02","♠️️03","♠️️04","♠️️05","♠️️06","♠️️07","♠️️08","♠️️09","♠️️10","♠️️J10","♠️️Q10","♠️️K10"]
for _ in range(8):
    cards_deck.extend(clubs)
    cards_deck.extend(diamonds)
    cards_deck.extend(hearts)
    cards_deck.extend(spades)
print(cards_deck)
print(len(cards_deck))
for _ in range(3):
    random.shuffle(cards_deck)
# cards_deck.pop(0)
# cards_deck=cards_deck[12:]
# no_of_decks=int(input("Enter the Number of Decks..? (6 or 8 )"))

no_of_decks=8
cards_deck_dict={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
for i in range(1,11):
    if i==10:
        cards_deck_dict[i]=no_of_decks*16
    else:
        cards_deck_dict[i]=no_of_decks*4
print(cards_deck_dict)
Running_count=0
test_RC=-1
small_big_key=0
test_rc_result_slots=[[],[],[],[]]
test_bp_results_slots=[[],[],[],[]]
new_rc_slots=[[],[]]
curr_result=""
curr_bp_highest=""

cards_left= no_of_decks*52
cards_out_list=[]
cards_out_in_shoe=0
decks_out_in_shoe=0

print(cards_deck)
game_count=0
Banker_win_count=0
Player_win_count=0
Tie_count=0
Banker_sum_list=[]
Player_sum_list=[]
low_count = 0
high_count = 0
low_high_pair = 0

pair_stats=[]
results_bp_stats=[]
results_numbers_stats=[]

while len(cards_deck)>=104:

    numbers_list_cards = []

    game_count+=1
    print(game_count, "_____________________________________")
    Banker = []
    Banker_sum = 0
    Player = []
    Player_sum = 0
    x=cards_deck.pop(0)

    Player.append(x)
    x = cards_deck.pop(0)

    Banker.append(x)
    x = cards_deck.pop(0)

    Player.append(x)
    x = cards_deck.pop(0)

    Banker.append(x)
    if cards_sum(Player) <= 7 and cards_sum(Banker) <= 7:
        if cards_sum(Player) <= 5:
            x = cards_deck.pop(0)

            Player.append(x)
        if cards_sum(Banker) <= 5:
            x = cards_deck.pop(0)

            Banker.append(x)

    numbers_list_cards.extend(Player)
    numbers_list_cards.extend(Banker)

    Banker_sum=cards_sum(Banker)
    Banker_sum_list.append(Banker_sum)
    Player_sum=cards_sum(Player)
    Player_sum_list.append(Player_sum)

    if Banker_sum <= 5 and Player_sum <= 5:
        low_count+=1
        pair_stats.append("L")
    elif Banker_sum > 5 and Player_sum >5:
        high_count+=1
        pair_stats.append("H")
    else:
        low_high_pair+=1
        pair_stats.append("B")

    print("Player         Banker")
    print(*Player,"     ",*Banker)
    print("  ",Player_sum,"            ",Banker_sum)
    if Banker_sum>Player_sum:
        Banker_win_count+=1
        results_bp_stats.append("B")
        curr_result="B"
        results_numbers_stats.append(Banker_sum)
        print("  Banker Wins ")
    elif Banker_sum<Player_sum:
        Player_win_count+=1
        print("  Player Wins ")
        results_bp_stats.append("P")
        curr_result="P"
        results_numbers_stats.append(Player_sum)
    else:
        Tie_count+=1
        print("  Tie ")
        results_bp_stats.append("T")
        curr_result="T"
        results_numbers_stats.append(Player_sum)

    if Banker_win_count>=Player_win_count:
        curr_bp_highest="B"
    else:
        curr_bp_highest="P"



    if game_count>10:
        if test_RC >= 0:
            if small_big_key == 2:
                test_rc_result_slots[0].append(curr_result)
                test_bp_results_slots[0].append(curr_bp_highest)
            elif small_big_key == 1:
                test_rc_result_slots[2].append(curr_result)
                test_bp_results_slots[2].append(curr_bp_highest)
        else:
            if small_big_key == 2:
                test_rc_result_slots[1].append(curr_result)
                test_bp_results_slots[1].append(curr_bp_highest)
            elif small_big_key == 1:
                test_rc_result_slots[3].append(curr_result)
                test_bp_results_slots[3].append(curr_bp_highest)

    # if game_count>10:
    #     if test_RC>=0:
    #         new_rc_slots[0].append(curr_result)
    #     else:
    #         new_rc_slots[1].append(curr_result)


    numbers_list=cards_value(numbers_list_cards)
    cards_out_list.extend(numbers_list)
    print("Numbers List : ", *cards_out_list)
    print("Given Numbers :", numbers_list)
    cards_out_in_shoe += len(numbers_list)
    for i in numbers_list:
        if i >= 1 and i <= 10:
            cards_deck_dict[i] -= 1
            if i >= 1 and i <= 4:
                Running_count += 1
            elif i>=6 and i<=9 :
                Running_count -= 1
    if cards_out_in_shoe // 52 > decks_out_in_shoe:
        decks_out_in_shoe = cards_out_in_shoe // 52
        remaining_decks = no_of_decks - decks_out_in_shoe
        if abs(Running_count) > remaining_decks:
            Running_count = Running_count // remaining_decks
    cards_left -= len(numbers_list)
    print("Cards still left : ", cards_left, "    Cards Out : ", cards_out_in_shoe)
    print("Decks still left : ", round(cards_left / 52, 1), "    Decks Out : ", round(cards_out_in_shoe / 52, 1))
    print("\n")
    print("Running Count : ", Running_count)
    test_RC=Running_count

    print("Remaining Cards Stats")
    sorted_dict = Sort_dict_reverse(cards_deck_dict)
    for i, j in sorted_dict.items():
        print(i, " = ", j, "    (", round((j / cards_left) * 100, 1), " %)")
    sorted_dict_keys = list(sorted_dict.keys())
    # print(sorted_dict_keys)
    top5_keys_without10 = sorted_dict_keys[1:6]
    bignumbers = 0
    smallnumbers = 0
    small_big_key=0
    for num in top5_keys_without10:
        if (num >= 1 and num <= 5):
            smallnumbers += 1
            small_big_key=1
        else:
            bignumbers += 1
            small_big_key=2
    if bignumbers > smallnumbers:
        print("10's or Big Numbers")
    else:
        print("10's or Small Numbers")
    print("\n\n")




print(Banker_sum_list)
Banker_stats=collections.Counter(Banker_sum_list)
print("B",Banker_stats)
print(Player_sum_list)
Player_stats=collections.Counter(Player_sum_list)
print("P",Player_stats)

total_sum_list=Banker_sum_list+Player_sum_list
total_stats=collections.Counter(total_sum_list)
print("OVERALL",total_stats)
print("low_high_pair :",low_high_pair)
print("low_count :",low_count)
print("high_count :",high_count)
print(*pair_stats)

print("Banker wins =",Banker_win_count)
print("Player wins =",Player_win_count)
print("Tie         =",Tie_count)

for i in test_bp_results_slots:
    print(i," =====> ",Counter(i))
print("\n")

for i in test_rc_result_slots:
    print(i," =====> ",Counter(i))
print("\n")

# for i in new_rc_slots:
#     print(i," =====> ",Counter(i))
# print("\n")

betwins=0
betlose=0
total_bet_amount=0
current_bet_amount=100
prev_result=results_bp_stats[0]
bet_stats=[]
current_bet_stats=[]
for i in range(1,len(results_bp_stats)-1):
    if results_bp_stats[i]==prev_result and results_bp_stats[i]!="T":
        if results_bp_stats[i]=='B' and results_numbers_stats[i]==6:
            total_bet_amount+=current_bet_amount//2
            current_bet_amount=100
        else:
            total_bet_amount+=current_bet_amount
            current_bet_amount=100
        betwins+=1
    elif results_bp_stats[i]=='T':
        pass
    else:
        prev_result=results_bp_stats[i]
        total_bet_amount-=current_bet_amount
        current_bet_amount=(current_bet_amount*2)+100
        if current_bet_amount>=10000 and total_bet_amount<=2000:
            current_bet_amount=current_bet_amount//2
        betlose+=1
    bet_stats.append(total_bet_amount)
    if total_bet_amount >=10000 or total_bet_amount <=-10000:
        break
    current_bet_stats.append(current_bet_amount)
print(results_bp_stats)
print(results_numbers_stats)
print("betwins :",betwins)
print("betlose :",betlose)
print(bet_stats)
print("maxx",max(bet_stats),"  min",min(bet_stats) ,"game number :",bet_stats.index(max(bet_stats)))
print("first 10 games highest :",max(bet_stats[:10]))
print(current_bet_stats)
print("maxx",max(current_bet_stats),"  min",min(current_bet_stats))
print(total_bet_amount)


