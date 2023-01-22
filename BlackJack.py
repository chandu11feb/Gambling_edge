import numpy as np

def Sort_dict_reverse(dictionary):
    keys=list(dictionary.keys())
    values=list(dictionary.values())
    sorted_value_index=np.argsort(values)
    sorted_value_index_list=list(sorted_value_index)
    sorted_value_index_list.reverse()
    final_dict ={keys[i] : values[i] for i in sorted_value_index_list}
    return final_dict

no_of_decks=int(input("Enter the Number of Decks..? (6 or 8 )"))
cards_deck_dict={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
for i in range(1,11):
    if i==10:
        cards_deck_dict[i]=no_of_decks*16
    else:
        cards_deck_dict[i]=no_of_decks*4
print(cards_deck_dict)
Running_count=0
cards_left= no_of_decks*52
cards_out_list=[]
cards_out_in_shoe=0
decks_out_in_shoe=0
while True:
    numbers_input=input("Enter Numbers or type 'exit' to stop \n")
    if numbers_input=="exit":
        break
    else:
        numbers_list=list(map(int,numbers_input.split()))
        cards_out_list.extend(numbers_list)
        print("Numbers List : ", *cards_out_list)
        print("Given Numbers :",numbers_list)
        cards_out_in_shoe+=len(numbers_list)
        for i in numbers_list:
            if i>=1 and i<=10:
                cards_deck_dict[i]-=1
                if i>=2 and i<=6:
                    Running_count+=1
                elif i==10 or i==1:
                    Running_count-=1
        if cards_out_in_shoe//52 > decks_out_in_shoe:
            decks_out_in_shoe=cards_out_in_shoe//52
            remaining_decks=no_of_decks-decks_out_in_shoe
            if abs(Running_count) > remaining_decks:
                Running_count=Running_count//remaining_decks
        cards_left-=len(numbers_list)
        print("Cards still left : ", cards_left,"    Cards Out : ", cards_out_in_shoe)
        print("Decks still left : ", round(cards_left/52,1), "    Decks Out : ", round(cards_out_in_shoe/52,1))
        print("\n")
        print("Running Count : ",Running_count)
        print("\n")

        print("Remaining Cards Stats")
        sorted_dict=Sort_dict_reverse(cards_deck_dict)
        for i,j in sorted_dict.items():
            print(i," = ",j ,"    (",round((j/cards_left)*100,1)," %)")
        sorted_dict_keys=list(sorted_dict.keys())
        # print(sorted_dict_keys)
        top5_keys_without10=sorted_dict_keys[1:6]
        bignumbers=0
        smallnumbers=0
        for num in top5_keys_without10:
            if (num>=2 and num <=6):
                smallnumbers+=1
            else:
                bignumbers+=1
        if bignumbers>smallnumbers:
            print("10's or Big Numbers")
        else:
            print("10's or Small Numbers")
        print("\n\n")


