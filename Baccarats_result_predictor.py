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
# print(cards_deck)
# print(len(cards_deck))
# cards_deck.pop(0)
# cards_deck=cards_deck[12:]
# print(cards_deck)

Main_result_list=[]



for _ in range(50000):
    results_str = ""
    removed_cards = []
    for _ in range(3):
        random.shuffle(cards_deck)
    very_first_card=cards_deck.pop(0)
    removed_cards.append(very_first_card)
    very_first_card_number=int(very_first_card[-1:])
    if very_first_card_number==0:
        if very_first_card[3]=="J":
            very_first_card_number=11
        elif very_first_card[3]=="Q":
            very_first_card_number=12
        elif very_first_card[3]=="K":
            very_first_card_number=11
        else:
            very_first_card_number=10
    removed_cards.extend(cards_deck[:very_first_card_number])
    cards_deck = cards_deck[very_first_card_number:]
    game_count=0
    while game_count < 68   :
        game_count += 1
        Banker = []
        Banker_sum = 0
        Player = []
        Player_sum = 0
        x = cards_deck.pop(0)
        removed_cards.append(x)

        Player.append(x)
        x = cards_deck.pop(0)
        removed_cards.append(x)

        Banker.append(x)
        x = cards_deck.pop(0)
        removed_cards.append(x)

        Player.append(x)
        x = cards_deck.pop(0)
        removed_cards.append(x)

        Banker.append(x)
        if cards_sum(Player)<=7 and cards_sum(Banker)<=7:
            if cards_sum(Player) <= 5:
                x = cards_deck.pop(0)
                removed_cards.append(x)

                Player.append(x)
            if cards_sum(Banker) <= 5:
                x = cards_deck.pop(0)
                removed_cards.append(x)

                Banker.append(x)


        Banker_sum = cards_sum(Banker)
        Player_sum = cards_sum(Player)

        if Banker_sum > Player_sum:
            results_str+="B"
        elif Banker_sum < Player_sum:
            results_str+="P"
        else:
            results_str+="T"

    cards_deck.extend(removed_cards)
    if results_str not in Main_result_list:
        Main_result_list.append(results_str)
# print(Main_result_list)
print(len(Main_result_list))
result_pattern_search_str=""
temp_search_str=""
filtered_list=[]
temp_filtered_list=[]
test_bpt=""
predict_wins=0
predict_lose=-1
while True:
    char_input=input("Enter Result, For Banker - B , Player - P , Tie - T , Stop - E ")
    char_input=char_input.upper()
    input_result_check=False
    for ch in char_input:
        if ch=="B" or ch=="P" or ch=="T" or ch=="E":
            input_result_check=True
        else:
            input_result_check=False
            break

    if char_input=="E":
        print(result_pattern_search_str)
        if result_pattern_search_str not in Main_result_list and len(result_pattern_search_str)>0:
            Main_result_list.append(result_pattern_search_str)
            # print(Main_result_list)
        break
    elif input_result_check:
        if test_bpt=="E":
            pass
        elif char_input==test_bpt:
            predict_wins+=1
        else:
            predict_lose+=1
        result_pattern_search_str+=char_input
        temp_search_str+=char_input
        print("Current Result Pattern : ",result_pattern_search_str)

        temp_filtered_list=list(filtered_list)
        for fil in filtered_list:
            if temp_search_str not in fil:
                temp_filtered_list.remove(fil)
        filtered_list=list(temp_filtered_list)



        while len(filtered_list)==0:
            for res in Main_result_list:
                if temp_search_str in res and res not in filtered_list:
                    filtered_list.append(res)
            if len(filtered_list)==0:
                temp_search_str=temp_search_str[1:]
        final_results_list=[]
        search_str_len=len(temp_search_str)
        print("Current Search Pattern : ",temp_search_str)
        for fil in filtered_list:
            fil_copy=fil
            pattern_count_in_fil=fil.count(temp_search_str)
            for cou in range(pattern_count_in_fil):
                pattern_index=fil_copy.index(temp_search_str)
                if pattern_index+search_str_len<len(fil):
                    final_results_list.append(fil[pattern_index+search_str_len])
                fil_copy=fil_copy[pattern_index+1:]

        if len(filtered_list)<=10:
            print("Filtered Lists :")
            print(filtered_list)

        B_count=final_results_list.count("B")
        P_count=final_results_list.count("P")
        T_count=final_results_list.count("T")
        bpt_max=max(B_count,P_count,T_count)
        if B_count==P_count:
            test_bpt="E"
        elif B_count==bpt_max:
            test_bpt="B"
        elif P_count==bpt_max:
            test_bpt="P"
        else:
            test_bpt="T"

        # print("Final Results : ")
        # print(final_results_list)
        print("===> ",len(final_results_list)," Matches Found")
        print(collections.Counter(final_results_list))
        print("\n")
        print("Prediction wins : ",predict_wins ," , Prediction Lose : ",predict_lose ," , Net : ",predict_wins-predict_lose)
    else:
        print("Enter Correct Result")

