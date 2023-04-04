from collections import Counter
# dice_list=[345, 356, 234, 235, 244, 155, 235, 334, 136, 355, 113, 445, 335, 346, 136, 145, 235, 224, 245, 166, 555, 566, 145, 113, 456, 156, 144, 156, 123, 122, 155, 446, 666, 126, 156, 245, 223, 116, 246, 455, 236, 134, 366, 146, 136, 246, 146, 123, 124, 235, 335, 123, 246, 466, 145, 344, 224, 223, 135, 556, 333, 256, 134, 166, 366, 244, 444, 234, 123, 366, 344, 134, 225, 113, 144, 246, 266, 156, 235, 456, 256, 236, 455, 124, 114, 235, 255, 256, 146, 366, 256, 123, 155, 114, 446, 123, 355, 234, 245, 223, 144, 245, 146, 556, 114, 136, 126, 156, 223, 126, 256, 345, 366, 136, 145, 346, 126, 345, 236, 345, 356, 456, 124, 455, 226, 125, 334, 466, 133, 134, 156, 236, 133, 556, 133, 344, 223, 226, 134, 222, 566, 333, 113, 245, 116, 136, 135, 334, 245, 334, 356, 113, 346, 366, 455, 356, 345, 346, 245, 112, 223, 225, 116, 113, 245, 134, 115, 124, 466, 246, 355, 256, 125, 123, 235, 145, 356, 334, 155, 335, 346, 223, 223, 122, 455, 344, 222, 234, 346, 236, 366, 225, 115, 115, 124, 444, 244, 115, 333, 245, 126, 226, 344, 124, 226, 235, 244, 236, 234, 156, 145, 136, 136, 245, 222, 336, 114, 222, 145, 344, 166, 125, 156, 146, 456, 111, 236, 334, 144, 156, 136, 355, 0, 125, 225, 255, 456, 234, 222, 445, 555, 566, 223, 135, 245, 134, 124, 234, 136, 166, 246, 234, 135, 566, 355, 124, 466, 114, 125, 236, 446, 234, 336, 126, 115, 114, 133, 256, 233, 136, 566, 236, 346, 345, 236, 125, 115, 455, 456, 223, 556, 136, 135, 136, 266, 222, 124, 113, 112, 146, 556, 112, 233, 122, 135, 346, 246, 113, 255, 135, 255, 455, 125, 113, 146, 566, 226, 224, 156, 123, 335, 223, 125, 146, 346, 366, 225, 166, 366, 455, 125, 126, 133, 336, 123, 135, 135, 335, 133, 235, 455, 226, 446, 666, 155, 122, 246, 0, 125, 236, 556, 124, 114, 233, 124, 355, 333, 145, 155, 145, 144, 123, 134, 244, 135, 244, 145, 245, 335, 125, 134, 224, 223, 246, 133, 123, 455, 456, 115, 123, 566, 245, 366, 256, 112, 255, 124, 236, 114, 333, 155, 146, 246, 136, 355, 244, 456, 456, 134, 334, 156, 145, 144, 123, 135, 256, 366, 155, 124, 345, 346, 111, 155, 345, 255, 125, 366, 556, 336, 355, 246, 146, 346, 125, 156, 236, 136, 456, 134, 334, 135, 123, 366, 124, 122, 124, 345, 146, 134, 336, 156, 156, 233, 366, 112, 135, 145, 236, 122, 256, 246, 156, 233, 556, 156, 245, 355, 135, 134, 456, 226, 245, 0, 366, 113, 336, 113, 256, 236, 134, 236, 455, 155, 444, 235, 355, 344, 455, 236, 455, 255, 116, 356, 166, 125, 255, 226, 566, 235, 336, 225, 345, 336, 136, 134, 246, 235, 156, 144, 455, 346, 566, 126, 235, 223, 444, 234, 556, 455, 246, 356, 146, 235, 246, 244, 344, 336, 125, 113, 244, 115, 246, 135, 456, 125, 355, 556, 126, 233, 556, 236, 115, 226, 155, 245, 115, 346, 456, 456, 136, 234, 245, 466, 136, 445, 355, 146, 125, 236, 125, 122, 166, 346, 345, 234, 456, 366, 0, 122, 155, 256, 335, 234, 166, 236, 125, 125, 146, 234, 344, 444, 136, 445, 455, 356, 255, 255, 145, 256, 135, 234, 135, 346, 245, 125, 123, 244, 124, 124, 346, 126, 345, 223, 355, 125, 246, 236, 124, 334, 346, 115, 446, 133, 336, 345, 335, 466, 144, 146, 344, 144, 456, 245, 566, 466, 145, 456, 345, 123, 144, 124, 135, 266, 346, 146, 155, 236, 0, 126, 115, 135, 145, 156, 115, 123, 126, 355, 113, 234, 356, 236, 123, 344, 456, 125, 0]
# ezugi
# dice_list=[122, 224, 346, 466, 355, 126, 115, 355, 356, 345, 126, 136, 156, 345, 356, 226, 256, 126, 566, 566, 126, 145, 145, 125, 124, 223, 234, 223, 466, 234, 126, 455, 114, 456, 224, 235, 135, 346, 124, 122, 445, 334, 556, 236, 166, 124, 114, 134, 345, 245, 245, 346, 235, 134, 466, 144, 116, 366, 345, 146, 346, 226, 256, 144, 445, 356, 145, 156, 124, 125, 114, 112, 336, 566, 346, 235, 133, 345, 224, 344, 124, 146, 144, 123, 236, 356, 255, 245, 234, 155, 133, 146, 226, 113, 156, 135, 226, 345, 245, 236, 124, 666, 245, 335, 246, 144, 225, 135, 256, 445, 111, 556, 134, 166, 122, 125, 125, 135, 226, 224, 124, 235, 344, 135, 245, 256, 235, 455, 456, 334, 135, 466, 466, 156, 124, 223, 345, 456, 136, 466, 166, 225, 245, 255, 136, 156, 226, 155, 126, 156, 446, 146, 466, 125, 246, 125, 125, 346, 233, 124, 346, 244, 236, 125, 356, 236, 124, 445, 125, 456, 134, 146, 135, 245, 122, 356, 245, 136, 466, 136, 244, 122, 256, 245, 166, 245, 356, 125, 456, 126, 125, 145, 566, 112, 235, 345, 235, 134, 123, 245, 134, 114, 135, 456, 356, 236, 456, 123, 134, 135, 236, 346, 133, 456, 246, 155, 355, 155, 136, 346, 456, 112, 255, 266, 345, 445, 145, 234, 123, 126, 123, 266, 255, 256, 346, 233, 235, 223, 244, 226, 125, 446, 146, 226, 236, 233, 355, 134, 135, 112, 116, 146, 356, 234, 136, 246, 115, 224, 116, 126, 445, 455, 245, 136, 566, 0]
# xpro
dice_list=[122, 224, 346, 466, 355, 126, 115, 355, 356, 345, 126, 136, 156, 345, 356, 226, 256, 126, 566, 566, 126, 145, 145, 125, 124, 223, 234, 223, 466, 234, 126, 455, 114, 456, 224, 235, 135, 346, 124, 122, 445, 334, 556, 236, 166, 124, 114, 134, 345, 245, 245, 346, 235, 134, 466, 144, 116, 366, 345, 146, 346, 226, 256, 144, 445, 356, 145, 156, 124, 125, 114, 112, 336, 566, 346, 235, 133, 345, 224, 344, 124, 146, 144, 123, 236, 356, 255, 245, 234, 155, 133, 146, 226, 113, 156, 135, 226, 345, 245, 236, 124, 666, 245, 335, 246, 144, 225, 135, 256, 445, 111, 556, 134, 166, 122, 125, 125, 135, 226, 224, 124, 235, 344, 135, 245, 256, 235, 455, 456, 334, 135, 466, 466, 156, 124, 223, 345, 456, 136, 466, 166, 225, 245, 255, 136, 156, 226, 155, 126, 156, 446, 146, 466, 125, 246, 125, 125, 346, 233, 124, 346, 244, 236, 125, 356, 236, 124, 445, 125, 456, 134, 146, 135, 245, 122, 356, 245, 136, 466, 136, 244, 122, 256, 245, 166, 245, 356, 125, 456, 126, 125, 145, 566, 112, 235, 345, 235, 134, 123, 245, 134, 114, 135, 456, 356, 236, 456, 123, 134, 135, 236, 346, 133, 456, 246, 155, 355, 155, 136, 346, 456, 112, 255, 266, 345, 445, 145, 234, 123, 126, 123, 266, 255, 256, 346, 233, 235, 223, 244, 226, 125, 446, 146, 226, 236, 233, 355, 134, 135, 112, 116, 146, 356, 234, 136, 246, 115, 224, 116, 126, 445, 455, 245, 136, 566, 0, 245, 166, 333, 234, 245, 255, 145, 456, 125, 236, 466, 115, 556, 115, 336, 346, 126, 445, 356, 124, 236, 225, 226, 144, 335, 255, 222, 126, 445, 115, 456, 136, 356, 135, 456, 133, 124, 112, 123, 134, 356, 126, 336, 112, 334, 456, 455, 255, 444, 335, 124, 126, 346, 116, 112, 112, 134, 244, 144, 145, 115, 135, 225, 556, 236, 123, 112, 126, 224, 256, 144, 456, 125, 224, 145, 256, 236, 226, 236, 366, 123, 226, 345, 456, 122, 145, 266, 126, 225, 124, 144, 136, 144, 355, 346, 126, 234, 445, 244, 355, 356, 126, 245, 256, 236, 556, 246, 445, 112, 256, 115, 124, 246, 126, 126, 124, 366, 0, 166, 334, 145, 126, 145, 456, 124, 244, 145, 445, 156, 116, 133, 136, 0, 146, 124, 122, 244, 446, 134, 235, 356, 134, 355, 123, 223, 446, 345, 235, 256, 446, 145, 0]
def is_triple(num):
    s=str(num)
    if s.count(s[0])==3:
        return True
    else:
        return False
def sum_of_digits(num):
    if num==0:
        return 0,[],[]
    s=str(num)
    cou=int(s[0])+int(s[1])+int(s[2])
    singles=[]
    singles.append(int(s[0]))
    singles.append(int(s[1]))
    singles.append(int(s[2]))
    doubles_combo=[]
    doubles_combo.append(int(s[0] + s[1]))
    doubles_combo.append(int(s[0] + s[2]))
    doubles_combo.append(int(s[1] + s[2]))
    return cou,singles,doubles_combo
def return_highest(l):
    count=0
    tem=l[0]
    for i in l:
        i_count=l.count(i)
        if i_count>count:
            tem=i
    return tem

def process_results(result_dice):
    print(result_dice)
    singles_list=[]
    sum_list=[]
    doubles_list=[]
    for i in result_dice:
        x,y,z=sum_of_digits(i)
        sum_list.append(x)
        singles_list.extend(y)
        doubles_list.extend(z)
    smalls=0
    bigs=0
    evens=0
    odds=0
    for i in sum_list:
        if i>=4 and i<=10:
            smalls+=1
        elif i>=11 and i<=17:
            bigs+=1
    for i in sum_list:
        if i%2==0:
            evens+=1
        else:
            odds+=1
    print("Smalls Count : ",smalls)
    print("Bigs Count   : ",bigs)
    print("\n")
    print("Evens Count  : ",evens)
    print("Odds Count   : ",odds)
    print("\n")
    sum_list_counter=Counter(sum_list)
    singles_counter=Counter(singles_list)
    doubles_counter=Counter(doubles_list)
    print("Numbers :",sum_list_counter)
    print("Singles :",singles_counter)
    print("Doubles :",doubles_counter)
    if len(sum_list)>=1:
        highest_in_sumlist=return_highest(sum_list)
        highest_in_singles=return_highest(singles_list)
        highest_in_doubles=return_highest(doubles_list)

    if smalls>=bigs:
        highest_in_sb=1
    else:
        highest_in_sb=0
    return highest_in_sb,highest_in_sumlist,highest_in_singles,highest_in_doubles
def process_num(num,highest_in_sb,highest_in_sumlist,highest_in_singles,highest_in_doubles):
    result_sb=0
    result_sumlist=0
    result_singles=0
    result_doubles=0
    if num==0 or is_triple(num):
        return 0,0,0,0
    s=str(num)
    cou=int(s[0])+int(s[1])+int(s[2])
    if cou >= 4 and cou <= 10:
        if highest_in_sb==1:
            result_sb=1
        else:
            result_sb=-1
    elif cou >= 11 and cou <= 17:
        if highest_in_sb==0:
            result_sb=1
        else:
            result_sb=-1

    if cou==highest_in_sumlist:
        result_sumlist=1
    else:
        result_sumlist=-1

    if highest_in_singles==int(s[0]) or highest_in_singles==int(s[1]) or highest_in_singles==int(s[2]):
        result_singles=1
    else:
        result_singles=-1

    if highest_in_doubles==int(s[0] + s[1]) or highest_in_doubles==int(s[0] + s[2]) or highest_in_doubles==int(s[1] + s[2]) :
        result_doubles=1
    else:
        result_doubles=-1
    return result_sb,result_sumlist,result_singles,result_doubles
print(len(dice_list))
process_results(dice_list)
# last_10_res=[]
game_count=0
sb_wins,sb_lose,single_wins,single_lose,sum_wins,sum_lose,double_wins,double_lose=0,0,0,0,0,0,0,0

while True:
    game_count+=1
    # sb_wins,sb_lose,single_wins,single_lose,sum_wins,sum_lose,double_wins,double_lose=0,0,0,0,0,0,0,0
    number=int(input("Enter a Number"))
    # number=dice_list[game_count]
    if game_count!=1:
        sb_res, suml_res, sing_res, doub_res = process_num(number, sb, suml, sing, doub)
    dice_list.append(number)
    if number==000:
        print(dice_list)
        break
    else:
        result_dices=[]
        for i in range(len(dice_list)):
            if dice_list[i]==number:
                if i+1<len(dice_list) and dice_list[i+1]!=0:
                    result_dices.append(dice_list[i+1])
        sb,suml,sing,doub=process_results(result_dices)
        # sb_res,suml_res,sing_res,doub_res=process_num(number,sb,suml,sing,doub)
        # if actual_res==target_res:
        #     last_10_res.append(1)
        # else:
        #     last_10_res.append(0)
        # if len(last_10_res)>10:
        #     print("Last 10 results : wins - ",last_10_res[len(last_10_res)-10:].count(1)," Loses - ",last_10_res[len(last_10_res)-10:].count(0), " Net wins/loss : ",last_10_res[1:].count(1)-last_10_res[1:].count(0))
            # print(last_10_res)
    if game_count==1 or sb_res==0:
        pass
    else:
        if sb_res==1:
            sb_wins+=1
        else:
            sb_lose+=1

        if suml_res==1:
            sum_wins+=1
        else:
            sum_lose+=1

        if sing_res==1:
            single_wins+=1
        else:
            single_lose+=1

        if doub_res==1:
            double_wins+=1
        else:
            double_lose+=1

        print("small big - wins = ", sb_wins, " loses = ", sb_lose, " net = ", sb_wins - sb_lose)
        print("Number sum - wins = ", sum_wins, " loses = ", sum_lose, " net = ", sum_wins - sum_lose)
        print("Singles - wins = ", single_wins, " loses = ", single_lose, " net = ", single_wins - single_lose)
        print("Doubles - wins = ",double_wins," loses = ",double_lose," net = ",double_wins-double_lose)






