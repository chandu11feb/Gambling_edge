import random
import collections

cards_deck=[]
clubs=["♣️A01","♣️️02","♣️️03","♣️04","♣️️05","♣️06","♣️️07","♣️️08","♣️️09","♣️️10","♣️️J11","♣️️Q12","♣️️K13"]
diamonds=["♦️A01","♦️02","♦️03","♦️04","♦️05","♦️06","♦️07","♦️08","♦️09","♦️10","♦️J11","♦️Q12","♦️K13"]
hearts=["❤️A01","❤️02","❤️03","❤️️04","❤️️05","❤️06","❤️07","❤️️08","❤️09","❤️️10","❤️️J11","❤️️Q12","❤️️K13"]
spades=["♠️A01","♠️️02","♠️️03","♠️04","♠️️05","♠️️06","♠️️07","♠️️08","♠️️09","♠️️10","♠️️J11","♠️️Q12","♠️️K13"]
for _ in range(1):
    cards_deck.extend(clubs)
    cards_deck.extend(diamonds)
    cards_deck.extend(hearts)
    cards_deck.extend(spades)
print(cards_deck)
print(len(cards_deck))
# for _ in range(3):
#     random.shuffle(cards_deck)
# cards_deck.pop(0)
# cards_deck=cards_deck[12:]

result_dict_100={"01":[],"02":[],"03":[],"04":[],"05":[],"06":[],"07":[],"08":[],"09":[],"10":[],"11":[],"12":[],"13":[]}
result_dict_stats={"01":[],"02":[],"03":[],"04":[],"05":[],"06":[],"07":[],"08":[],"09":[],"10":[],"11":[],"12":[],"13":[]}
card_number_list=[]
card_number_list_stats={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
card_number_slots = ["01-05","06-10","11-15","16-25","26-30","31-35","36-40","41-49"]

for i in range(100):
    playing_cards_deck=[]
    playing_cards_deck.extend(cards_deck)
    for _ in range(3):
        random.shuffle(playing_cards_deck)
    playing_cards_deck=playing_cards_deck[26:]+playing_cards_deck[:26]
    face_card=playing_cards_deck.pop()
    face_card_number=int(face_card[-2:])
    Andhar_list=[]
    Bahar_List=[]
    for card_num in range(len(playing_cards_deck)):
        current_card=playing_cards_deck[card_num]
        current_card_number=int(current_card[-2:])
        if card_num%2==0:
            Andhar_list.append(current_card)
            if face_card_number==current_card_number:
                res="A"+str(card_num)
                result_dict_100[face_card[-2:]].append(res)
                card_number_list.append(card_num)
                break
        else:
            Bahar_List.append(current_card)
            if face_card_number==current_card_number:
                res="B"+str(card_num)
                result_dict_100[face_card[-2:]].append(res)
                card_number_list.append(card_num)
                break
    # print(result_dict_100)
for i in card_number_list:
    if i>=1 and i<=5:
        card_number_list_stats[1].append(i)
    elif i>=6 and i<=10:
        card_number_list_stats[2].append(i)
    elif i>=11 and i<=15:
        card_number_list_stats[3].append(i)
    elif i>=16 and i<=25:
        card_number_list_stats[4].append(i)
    elif i>=26 and i<=30:
        card_number_list_stats[5].append(i)
    elif i>=31 and i<=35:
        card_number_list_stats[6].append(i)
    elif i>=36 and i<=40:
        card_number_list_stats[7].append(i)
    elif i>=41 and i<=49:
        card_number_list_stats[8].append(i)

for i,j in card_number_list_stats.items():
    print(card_number_slots[i-1],"--->",len(j))

for i,j in result_dict_100.items():
    print(i,sorted(j))