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
clubs=["♣️A01","♣️️02","♣️️03","♣️04","♣️️05","♣️06","♣️️07","♣️️08","♣️️09","♣️️10","♣️️J11","♣️️Q12","♣️️K13"]
diamonds=["♦️A01","♦️02","♦️03","♦️04","♦️05","♦️06","♦️07","♦️08","♦️09","♦️10","♦️J11","♦️Q12","♦️K13"]
hearts=["❤️A01","❤️02","❤️03","❤️️04","❤️️05","❤️06","❤️07","❤️️08","❤️09","❤️️10","❤️️J11","❤️️Q12","❤️️K13"]
spades=["♠️A01","♠️️02","♠️️03","♠️04","♠️️05","♠️️06","♠️️07","♠️️08","♠️️09","♠️️10","♠️️J11","♠️️Q12","♠️️K13"]
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
# print(cards_deck)
no_of_decks=8
cards_deck_dict={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0}
for i in range(1,14):
    cards_deck_dict[i]=no_of_decks*4
cards_left=8*52
cards_out_in_shoe =0
decks_out_in_shoe=0
Running_count=0

curr_result=""
FS_slots=[[],[]]

game_number=1
first_card_wins=0
second_card_wins=0
results_list=[]
# slots=[0,0,0,0,0,0]
while len(cards_deck)>=110:
    first_card=cards_deck.pop(0)
    first_card_number=int(first_card[-2:])
    second_card=cards_deck.pop(0)
    second_card_number = int(second_card[-2:])

    cards_deck_dict[first_card_number]-=1
    cards_deck_dict[second_card_number]-=1

    if first_card_number>=1 and first_card_number<=6:
        Running_count-=1
    elif first_card_number>=8 and first_card_number<=13:
        Running_count+=1

    if second_card_number>=1 and second_card_number<=6:
        Running_count-=1
    elif second_card_number>=8 and second_card_number<=13:
        Running_count+=1

    print("gamecount------>",game_number)
    game_number+=1
    print("fcard           scard")
    print(first_card,"           ",second_card)
    if first_card_number > second_card_number:
        first_card_wins+=1
        results_list.append("F")
        curr_result="F"
        print("first card wins")
    elif first_card_number < second_card_number:
        second_card_wins+=1
        results_list.append("S")
        curr_result="S"
        print("second card wins")
    else:
        results_list.append("T")
        curr_result="T"
        print("Tie")

    if game_number>80:
        if test_fs == "S":
            FS_slots[0].append(curr_result)
        else:
            FS_slots[1].append(curr_result)

    cards_left -= 2
    cards_out_in_shoe += 2
    if cards_out_in_shoe // 52 > decks_out_in_shoe:
        decks_out_in_shoe = cards_out_in_shoe // 52
        remaining_decks = no_of_decks - decks_out_in_shoe
        if abs(Running_count) > remaining_decks:
            Running_count = Running_count // remaining_decks
    print("Cards still left : ", cards_left, "    Cards Out : ", cards_out_in_shoe)
    print("Decks still left : ", round(cards_left / 52, 1), "    Decks Out : ", round(cards_out_in_shoe / 52, 1))
    print("\n")
    print("Running Count : ", Running_count)
    test_RC = Running_count

    print("Remaining Cards Stats")
    sorted_dict = Sort_dict_reverse(cards_deck_dict)
    for i, j in sorted_dict.items():
        print(i, " = ", j, "    (", round((j / cards_left) * 100, 1), " %)")
    sorted_dict_keys = list(sorted_dict.keys())
    # print(sorted_dict_keys)
    top6_keys = sorted_dict_keys[0:7]
    bignumbers = 0
    top3_list=top6_keys[:3]
    top_second3_list=top6_keys[3:6]
    
    if 7 in top6_keys:
        top6_keys.remove(7)
    else:
        top6_keys=top6_keys[:6]

    smallnumbers = 0
    for i in top6_keys:
        if i>=8 and i<=13:
            bignumbers+=1
        elif i>=1 and i<=6:
            smallnumbers+=1

    if bignumbers>smallnumbers:
        print("Big Numbers == First")
        print("Top 3 : ",top3_list," , Next 3 : ",top_second3_list)
        test_fs="B"
    else:
        print("Small Numbers  == Second")
        print("Top 3 : ",top3_list," , Next 3 : ",top_second3_list)
        test_fs="S"

for i in FS_slots:
    print(i," =====> ",Counter(i))
print("\n")

print("first card wins =",first_card_wins)
print("second card wins =",second_card_wins)
print(results_list)
first_card_seq_count=0
second_card_seq_count=0
temp_f=0
temp_s=0
for i in range(1,len(results_list)):
    if results_list[i]==results_list[i-1] and results_list[i]=="F":
        temp_s=0
        temp_f+=1
        if temp_f>first_card_seq_count:
            first_card_seq_count=temp_f
    elif results_list[i]==results_list[i-1] and results_list[i]=="S":
        temp_f=0
        temp_s+=1
        if temp_s>second_card_seq_count:
            second_card_seq_count=temp_s
print("first_card_seq_count : ",first_card_seq_count)
print("second_card_seq_count : ",second_card_seq_count)
prev_winner=results_list[0]

bet_amt=10
bet_wins=0
bet_loses=0
total_current_amount=10
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
        bet_amt=10
        # if bet_amt<100:
        #     bet_amt=100
    else:
        if results_list[i]=="T":
            total_current_amount -= bet_amt//2
        else:
            bet_loses+=1
            prev_winner=results_list[i]
            total_current_amount-=bet_amt
            current_amount_list.append(total_current_amount)
            bet_amt=(bet_amt*2)+10
            if bet_amt>5000:
                bet_amt=5000
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




