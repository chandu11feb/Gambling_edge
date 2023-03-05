from collections import Counter
dice_list=[345, 356, 234, 235, 244, 155, 235, 334, 136, 355, 113, 445, 335, 346, 136, 145, 235, 224, 245, 166, 555, 566, 145, 113, 456, 156, 144, 156, 123, 122, 155, 446, 666, 126, 156, 245, 223, 116, 246, 455, 236, 134, 366, 146, 136, 246, 146, 123, 124, 235, 335, 123, 246, 466, 145, 344, 224, 223, 135, 556, 333, 256, 134, 166, 366, 244, 444, 234, 123, 366, 344, 134, 225, 113, 144, 246, 266, 156, 235, 456, 256, 236, 455, 124, 114, 235, 255, 256, 146, 366, 256, 123, 155, 114, 446, 123, 355, 234, 245, 223, 144, 245, 146, 556, 114, 136, 126, 156, 223, 126, 256, 345, 366, 136, 145, 346, 126, 345, 236, 345, 356, 456, 124, 455, 226, 125, 334, 466, 133, 134, 156, 236, 133, 556, 133, 344, 223, 226, 134, 222, 566, 333, 113, 245, 116, 136, 135, 334, 245, 334, 356, 113, 346, 366, 455, 356, 345, 346, 245, 112, 223, 225, 116, 113, 245, 134, 115, 124, 466, 246, 355, 256, 125, 123, 235, 145, 356, 334, 155, 335, 346, 223, 223, 122, 455, 344, 222, 234, 346, 236, 366, 225, 115, 115, 124, 444, 244, 115, 333, 245, 126, 226, 344, 124, 226, 235, 244, 236, 234, 156, 145, 136, 136, 245, 222, 336, 114, 222, 145, 344, 166, 125, 156, 146, 456, 111, 236, 334, 144, 156, 136, 355, 0, 125, 225, 255, 456, 234, 222, 445, 555, 566, 223, 135, 245, 134, 124, 234, 136, 166, 246, 234, 135, 566, 355, 124, 466, 114, 125, 236, 446, 234, 336, 126, 115, 114, 133, 256, 233, 136, 566, 236, 346, 345, 236, 125, 115, 455, 456, 223, 556, 136, 135, 136, 266, 222, 124, 113, 112, 146, 556, 112, 233, 122, 135, 346, 246, 113, 255, 135, 255, 455, 125, 113, 146, 566, 226, 224, 156, 123, 335, 223, 125, 146, 346, 366, 225, 166, 366, 455, 125, 126, 133, 336, 123, 135, 135, 335, 133, 235, 455, 226, 446, 666, 155, 122, 246, 0, 125, 236, 556, 124, 114, 233, 124, 355, 333, 145, 155, 145, 144, 123, 134, 244, 135, 244, 145, 245, 335, 125, 134, 224, 223, 246, 133, 123, 455, 456, 115, 123, 566, 245, 366, 256, 112, 255, 124, 236, 114, 333, 155, 146, 246, 136, 355, 244, 456, 456, 134, 334, 156, 145, 144, 123, 135, 256, 366, 155, 124, 345, 346, 111, 155, 345, 255, 125, 366, 556, 336, 355, 246, 146, 346, 125, 156, 236, 136, 456, 134, 334, 135, 123, 366, 124, 122, 124, 345, 146, 134, 336, 156, 156, 233, 366, 112, 135, 145, 236, 122, 256, 246, 156, 233, 556, 156, 245, 355, 135, 134, 456,226,245,0]
def compare(x,y):
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



