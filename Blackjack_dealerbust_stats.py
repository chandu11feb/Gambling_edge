import random

deck_numbers=[1,2,3,4,5,6,7,8,9,10,10,10,10]

cards_deck=[]
for i in range(32):
    cards_deck.extend(deck_numbers)
    random.shuffle(cards_deck)
for i in range(3):
    random.shuffle(cards_deck)
player_slots=[[],[],[],[],[],[],[]]
dealer_slot=[]
player_slots_wins=[0,0,0,0,0,0,0]
dealer_wins=0
dealer_bust_count=0
bjs_for_dealer_count=0
bjs_for_players_count=0
gamecount=0
total_current_amount=3500
bet_slots_amount=[500,500,500,500,500,500,500]
current_amount_list=[3500]
while len(cards_deck)>195:
    gamecount+=1
    player_slots = [[], [], [], [], [], [], []]
    dealer_slot = []
    for i in range(7):
        player_slots[i].append(cards_deck.pop())
    dealer_slot.append(cards_deck.pop())
    for i in range(7):
        player_slots[i].append(cards_deck.pop())
    dealer_slot.append(cards_deck.pop())
    # print(player_slots)
    # print(dealer_slot)
    # break

    #processing sum of each slots and hitting if it is less than 12
    dealer_bj=False
    dealer_slot_sum=sum(dealer_slot)
    dealer_bust=False
    if 1 in dealer_slot:
        if dealer_slot_sum==11:
            dealer_bj=True
            bjs_for_dealer_count+=1
            dealer_slot_sum=21
        else:
            if dealer_slot_sum+10 <=21 and dealer_slot_sum+10>=17:
                dealer_slot_sum+=10

    for i in range(7):
        if dealer_bj:
            break
        player_slots[i].sort()
        slot_sum = sum(player_slots[i])
        if 1 in player_slots[i]:
            if player_slots[i][1]==1:
                while slot_sum<=11:
                    player_slots[i].append(cards_deck.pop())
                    slot_sum=sum(player_slots[i])
            else:
                temp=sum(player_slots[i])
                if temp==11:
                    bjs_for_players_count+=1
                if max(temp,temp+10)<=21 and max(temp,temp+10)>=17:
                    slot_sum=temp+10
                    player_slots[i].clear()
                    player_slots[i].append(temp+10)
        else:
            while slot_sum<=11:
                card_value=cards_deck.pop()
                if card_value==1:
                    if slot_sum<=10:
                        card_value=11
                player_slots[i].append(card_value)
                slot_sum=sum(player_slots[i])

    while dealer_slot_sum<17:
        temp_deal=cards_deck.pop()
        dealer_slot.append(temp_deal)
        dealer_slot_sum=sum(dealer_slot)
        if temp_deal==1:
            if dealer_slot_sum + 10 <= 21 and dealer_slot_sum + 10 >= 17:
                dealer_slot_sum += 10
        else:
            if dealer_slot_sum>21:
                dealer_bust=True
                dealer_bust_count+=1
    if dealer_bj:
        dealer_wins+=7
        total_current_amount-=sum(bet_slots_amount)
    elif dealer_bust:
        for i in range(7):
            player_slots_wins[i]+=1
        total_current_amount+=sum(bet_slots_amount)
    else:
        for i in range(7):
            if sum(player_slots[i]) > dealer_slot_sum:
                player_slots_wins[i]+=1
                total_current_amount+=bet_slots_amount[i]
            elif sum(player_slots[i]) < dealer_slot_sum:
                dealer_wins+=1
                total_current_amount-=bet_slots_amount[i]
            else:
                pass
    current_amount_list.append(total_current_amount)
print("total games ",gamecount)
print("Dealer wins :",dealer_wins)
print("Player slot wins :",player_slots_wins,sum(player_slots_wins))
print("Dealer Blackjacks :",bjs_for_dealer_count)
print("Player Blackjacks :",bjs_for_players_count)
print("Dealer Bust Count :",dealer_bust_count)
print("current amount list :",current_amount_list)
print("Max curr amount :",max(current_amount_list),"  Min Curr amount :",min(current_amount_list))
print("Total Current Amount :",total_current_amount)






