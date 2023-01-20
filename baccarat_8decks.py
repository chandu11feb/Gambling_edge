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
clubs=["♣️A1","♣️️2","♣️️3","♣️️4","♣️️5","♣️️6","♣️️7","♣️️8","♣️️9","♣️️10","♣️️J0","♣️️Q0","♣️️K0"]
diamonds=["♦️A1","♦️2","♦️3","♦️4","♦️5","♦️6","♦️7","♦️8","♦️9","♦️10","♦️J0","♦️Q0","♦️K0"]
hearts=["❤️A1","❤️2","❤️3","❤️️4","❤️️5","❤️6","❤️7","❤️️8","❤️9","❤️️10","❤️️J0","❤️️Q0","❤️️K0"]
spades=["♠️A1","♠️️2","♠️️3","♠️️4","♠️️5","♠️️6","♠️️7","♠️️8","♠️️9","♠️️10","♠️️J0","♠️️Q0","♠️️K0"]
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
cards_deck=cards_deck[12:]
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
running_count1=0
running_count2=0
count_stat_dict={}
nofc_deck=52
pair_stats=[]
results_bp_stats=[]
results_numbers_stats=[]
while len(cards_deck)>=102:
    prev_running_count1=running_count1
    prev_running_count2=running_count2
    game_count+=1
    print(game_count, "_____________________________________")
    Banker = []
    Banker_sum = 0
    Player = []
    Player_sum = 0
    x=cards_deck.pop(0)
    if int(x[-1])<5:
        running_count1-=1
    elif int(x[-1])>5:
        running_count1+=1

    if int(x[-1])==0:
        running_count2+=1
    Player.append(x)
    x = cards_deck.pop(0)
    if int(x[-1]) < 5:
        running_count1 -= 1
    elif int(x[-1]) > 5:
        running_count1 += 1

    if int(x[-1]) == 0:
        running_count2 += 1
    Banker.append(x)
    x = cards_deck.pop(0)
    if int(x[-1]) < 5:
        running_count1 -= 1
    elif int(x[-1]) > 5:
        running_count1 += 1

    if int(x[-1]) == 0:
        running_count2 += 1
    Player.append(x)
    x = cards_deck.pop(0)
    if int(x[-1]) < 5:
        running_count1 -= 1
    elif int(x[-1]) > 5:
        running_count1 += 1

    if int(x[-1]) == 0:
        running_count2 += 1
    Banker.append(x)
    if cards_sum(Player)<=5:
        x = cards_deck.pop(0)
        if int(x[-1]) < 5:
            running_count1 -= 1
        elif int(x[-1]) > 5:
            running_count1 += 1

        if int(x[-1]) == 0:
            running_count2 += 1
        Player.append(x)
    if cards_sum(Banker)<=5:
        x = cards_deck.pop(0)
        if int(x[-1]) < 5:
            running_count1 -= 1
        elif int(x[-1]) > 5:
            running_count1 += 1

        if int(x[-1]) == 0:
            running_count2 += 1
        Banker.append(x)
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

    temp_str1=str(game_count)+") cards_count : "+str(prev_running_count1)+", 10's count : "+str(prev_running_count2)
    temp_str2= "============>>> Banker : "+str(Banker_sum)+", Player : "+str(Player_sum)
    count_stat_dict[temp_str1]=temp_str2
    #print(temp_str1)

    print("Banker         Player")
    print(*Banker,"     ",*Player)
    print("  ",Banker_sum,"            ",Player_sum)
    if Banker_sum>Player_sum:
        Banker_win_count+=1
        results_bp_stats.append("B")
        results_numbers_stats.append(Banker_sum)
        print("  Banker Wins ")
    elif Banker_sum<Player_sum:
        Player_win_count+=1
        print("  Player Wins ")
        results_bp_stats.append("P")
        results_numbers_stats.append(Player_sum)
    else:
        Tie_count+=1
        print("  Tie ")
        results_bp_stats.append("T")
        results_numbers_stats.append(Player_sum)

    cards_outofdeck=312-len(cards_deck)
    if cards_outofdeck >= nofc_deck:
        nofc_deck+=52
        divisor=cards_outofdeck//52
        running_count1//=divisor
        running_count2//=divisor

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

betwins=0
betlose=0
total_bet_amount=0
current_bet_amount=50
prev_result=results_bp_stats[0]
bet_stats=[]
current_bet_stats=[]
for i in range(1,len(results_bp_stats)-9):
    if results_bp_stats[i]==prev_result and results_bp_stats[i]!="T":
        if results_bp_stats[i]=='B' and results_numbers_stats[i]==6:
            total_bet_amount+=current_bet_amount//2
            current_bet_amount=50
        else:
            total_bet_amount+=current_bet_amount
            current_bet_amount=50
        betwins+=1
    elif results_bp_stats[i]=='T':
        pass
    else:
        prev_result=results_bp_stats[i]
        total_bet_amount-=current_bet_amount
        current_bet_amount=(current_bet_amount*2)
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




#for i,j in count_stat_dict.items():
    #print(i,j)