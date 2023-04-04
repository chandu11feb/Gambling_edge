dice_list=[122, 224, 346, 466, 355, 126, 115, 355, 356, 345, 126, 136, 156, 345, 356, 226, 256, 126, 566, 566, 126, 145, 145, 125, 124, 223, 234, 223, 466, 234, 126, 455, 114, 456, 224, 235, 135, 346, 124, 122, 445, 334, 556, 236, 166, 124, 114, 134, 345, 245, 245, 346, 235, 134, 466, 144, 116, 366, 345, 146, 346, 226, 256, 144, 445, 356, 145, 156, 124, 125, 114, 112, 336, 566, 346, 235, 133, 345, 224, 344, 124, 146, 144, 123, 236, 356, 255, 245, 234, 155, 133, 146, 226, 113, 156, 135, 226, 345, 245, 236, 124, 666, 245, 335, 246, 144, 225, 135, 256, 445, 111, 556, 134, 166, 122, 125, 125, 135, 226, 224, 124, 235, 344, 135, 245, 256, 235, 455, 456, 334, 135, 466, 466, 156, 124, 223, 345, 456, 136, 466, 166, 225, 245, 255, 136, 156, 226, 155, 126, 156, 446, 146, 466, 125, 246, 125, 125, 346, 233, 124, 346, 244, 236, 125, 356, 236, 124, 445, 125, 456, 134, 146, 135, 245, 122, 356, 245, 136, 466, 136, 244, 122, 256, 245, 166, 245, 356, 125, 456, 126, 125, 145, 566, 112, 235, 345, 235, 134, 123, 245, 134, 114, 135, 456, 356, 236, 456, 123, 134, 135, 236, 346, 133, 456, 246, 155, 355, 155, 136, 346, 456, 112, 255, 266, 345, 445, 145, 234, 123, 126, 123, 266, 255, 256, 346, 233, 235, 223, 244, 226, 125, 446, 146, 226, 236, 233, 355, 134, 135, 112, 116, 146, 356, 234, 136, 246, 115, 224, 116, 126, 445, 455, 245, 136, 566, 0]
small_big_list=[]
numbers_list=[]
def is_triple(num):
    s=str(num)
    if s.count(s[0])==3:
        return True
    else:
        return False
def sum_of_digits(num):
    if num==0:
        return 0
    s=str(num)
    return int(s[0])+int(s[1])+int(s[2])
for i in dice_list:
    cou=sum_of_digits(i)
    numbers_list.append(cou)
    if cou>=4 and cou<=10:
        small_big_list.append("S")
    elif cou>=11 and cou<=17:
        small_big_list.append("B")
triple_count=0
cur=0
triple_list=[]
while cur+1 < len(dice_list):
    trips=0
    for i in dice_list[cur:cur+100]:
        if is_triple(i):
            trips+=1
    triple_list.append(trips)
    cur+=1
print(triple_list)
print(max(triple_list))
print(len(dice_list))
print("triple_count : ",triple_count)
bet_wins=0
bet_lose=0
total_amount=0
total_amount_list=[]
total_bet=100
bet_list=[]

for i in range(1,len(small_big_list)):
    if small_big_list[i]==small_big_list[i-1]:
        total_amount+=total_bet
        if total_amount<0:
            total_bet=abs(total_amount)
        else:
            total_bet=100
        bet_wins+=1
    else:
        total_amount-=total_bet
        if total_amount<0:
            total_bet=abs(total_amount)
        else:
            total_bet=total_bet+total_bet
        bet_lose+=1
    total_amount_list.append(total_amount)
    bet_list.append(total_bet)
print(small_big_list)
print(numbers_list)
print("bet_wins : ",bet_wins)
print("bet_lose : ",bet_lose)
print(total_amount_list)
print("max amount:",max(total_amount_list)," min amount: ",min(total_amount_list))
print(bet_list)
print("max bet:",max(bet_list)," min bet: ",min(bet_list))
print("Final amount : ",total_amount)



