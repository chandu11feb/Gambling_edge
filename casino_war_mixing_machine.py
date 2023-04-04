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
clubs=["♣️A14","♣️️02","♣️️03","♣️04","♣️️05","♣️06","♣️️07","♣️️08","♣️️09","♣️️10","♣️️J11","♣️️Q12","♣️️K13"]
diamonds=["♦️A14","♦️02","♦️03","♦️04","♦️05","♦️06","♦️07","♦️08","♦️09","♦️10","♦️J11","♦️Q12","♦️K13"]
hearts=["❤️A14","❤️02","❤️03","❤️️04","❤️️05","❤️06","❤️07","❤️️08","❤️09","❤️️10","❤️️J11","❤️️Q12","❤️️K13"]
spades=["♠️A14","♠️️02","♠️️03","♠️04","♠️️05","♠️️06","♠️️07","♠️️08","♠️️09","♠️️10","♠️️J11","♠️️Q12","♠️️K13"]
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
slots=[0,0,0,0,0,0]
bet_amount_slots=[500,500,500,500,500,500]
total_current_amount=3000
casino_wins=0
max_bet_amount_stats=[]
total_bet_amount_stats=[]
current_amount_stats=[]
while len(cards_deck)>=35:
    random.shuffle(cards_deck)
    temp_first_card=cards_deck.pop(0)
    current_slot_card=[]
    for i in range(6):
        curr_card=cards_deck.pop(0)
        current_slot_card.append(int(curr_card[-2:]))
    casino_card=cards_deck.pop(0)
    casino_card_number=int(casino_card[-2:])
    for i in range(6):
        if current_slot_card[i]>casino_card_number:
            slots[i]+=1
            total_current_amount+=bet_amount_slots[i]
            bet_amount_slots[i]=500
        elif current_slot_card[i]<casino_card_number:
            casino_wins+=1
            total_current_amount-=bet_amount_slots[i]
            if bet_amount_slots[i]*2 >=10000:
                pass
            else:
                bet_amount_slots[i] = bet_amount_slots[i] * 2
        else:
            extra_current_card=cards_deck.pop(0)
            extra_current_card_number=int(extra_current_card[-2:])
            extra_casino_card=cards_deck.pop(0)
            extra_casino_card_number = int(extra_casino_card[-2:])
            if extra_current_card_number>extra_casino_card_number:
                slots[i]+=1
                total_current_amount += bet_amount_slots[i] * 2
                bet_amount_slots[i] = 500
            elif extra_casino_card_number > extra_current_card_number:
                casino_wins+=1
                total_current_amount -= bet_amount_slots[i] * 2
                if bet_amount_slots[i] * 2 >= 10000:
                    pass
                else:
                    bet_amount_slots[i] = bet_amount_slots[i] * 2
            else:
                slots[i]+=1
                total_current_amount += bet_amount_slots[i] * 2
                bet_amount_slots[i] = 500
    max_bet_amount_stats.append(max(bet_amount_slots))
    total_bet_amount_stats.append(sum(bet_amount_slots))
    current_amount_stats.append(total_current_amount)
    print("game number ----------------->",game_number)
    game_number+=1
    print("max_bet_amount :",max(bet_amount_slots))
    print("total_bet_amount :",sum(bet_amount_slots))
    print("current amount :",total_current_amount)
    if (total_current_amount<=-1000 and sum(bet_amount_slots) >=4000) :
        break
    # if total_current_amount >=21000 or total_current_amount <= sum(bet_amount_slots):
    #     bet_amount_slots = [500, 500, 500, 500, 500, 500]


print(slots)
print("slot wins",sum(slots))
print("casino wins",casino_wins)

print("max bet amount stats")
print(max_bet_amount_stats)
print(max(max_bet_amount_stats))

print("total bet amount stats")
print(total_bet_amount_stats)
print(max(total_bet_amount_stats))

print("current amount stats")
print(current_amount_stats)
print("max :",max(current_amount_stats),"min: ",min(current_amount_stats))
print(total_current_amount)