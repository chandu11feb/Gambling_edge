from collections import Counter
dice_list=[122, 224, 346, 466, 355, 126, 115, 355, 356, 345, 126, 136, 156, 345, 356, 226, 256, 126, 566, 566, 126, 145, 145, 125, 124, 223, 234, 223, 466, 234, 126, 455, 114, 456, 224, 235, 135, 346, 124, 122, 445, 334, 556, 236, 166, 124, 114, 134, 345, 245, 245, 346, 235, 134, 466, 144, 116, 366, 345, 146, 346, 226, 256, 144, 445, 356, 145, 156, 124, 125, 114, 112, 336, 566, 346, 235, 133, 345, 224, 344, 124, 146, 144, 123, 236, 356, 255, 245, 234, 155, 133, 146, 226, 113, 156, 135, 226, 345, 245, 236, 124, 666, 245, 335, 246, 144, 225, 135, 256, 445, 111, 556, 134, 166, 122, 125, 125, 135, 226, 224, 124, 235, 344, 135, 245, 256, 235, 455, 456, 334, 135, 466, 466, 156, 124, 223, 345, 456, 136, 466, 166, 225, 245, 255, 136, 156, 226, 155, 126, 156, 446, 146, 466, 125, 246, 125, 125, 346, 233, 124, 346, 244, 236, 125, 356, 236, 124, 445, 125, 456, 134, 146, 135, 245, 122, 356, 245, 136, 466, 136, 244, 122, 256, 245, 166, 245, 356, 125, 456, 126, 125, 145, 566, 112, 235, 345, 235, 134, 123, 245, 134, 114, 135, 456, 356, 236, 456, 123, 134, 135, 236, 346, 133, 456, 246, 155, 355, 155, 136, 346, 456, 112, 255, 266, 345, 445, 145, 234, 123, 126, 123, 266, 255, 256, 346, 233, 235, 223, 244, 226, 125, 446, 146, 226, 236, 233, 355, 134, 135, 112, 116, 146, 356, 234, 136, 246, 115, 224, 116, 126, 445, 455, 245, 136, 566, 0]
def compare(x,y):
    if x==0 or y==0:
        return 0
    amount=20
    count=0
    bet_numbers=[]
    bet_combos=[]
    strx=str(x)
    stry=str(y)
    bet_numbers.append(int(strx[0]))
    bet_numbers.append(int(strx[1]))
    bet_numbers.append(int(strx[2]))
    bet_combos.append(int(strx[0]+strx[1]))
    bet_combos.append(int(strx[0] + strx[2]))
    bet_combos.append(int(strx[1] + strx[2]))
    cur_numbers=[]
    cur_combos=[]
    cur_numbers.append(int(stry[0]))
    cur_numbers.append(int(stry[1]))
    cur_numbers.append(int(stry[2]))
    cur_combos.append(int(stry[0] + stry[1]))
    cur_combos.append(int(stry[0] + stry[2]))
    cur_combos.append(int(stry[1] + stry[2]))
    for i in cur_numbers:
        if i in bet_numbers:
            count+=amount
        else:
            count-=amount
    for i in cur_combos:
        if i in bet_combos:
            count+=amount*5
        else:
            count-=amount
    return count
# print(compare(123,234))
amount_list=[]
for i in range(len(dice_list)-12):
    pres_list=dice_list[i:i+21]
    print(pres_list)
    pres_count=0
    for j in range(len(pres_list)-1):
        pres_count+=compare(pres_list[j],pres_list[j+1])
    print(pres_count)
    amount_list.append(pres_count)
print(amount_list)
print(sum(amount_list))




