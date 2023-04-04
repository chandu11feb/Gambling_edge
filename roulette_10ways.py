from collections import Counter
bet_number = int(input("Enter the betting number from 0-36"))
bet_amt = int(input("Enter bet amount(same of all placements) Min:500"))
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
first12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
second12 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
third12 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
top12 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
middle12 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
bottom12 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
half_map = {1: [1, 4], 2: [2, 5], 3: [3,6], 4: [4,7], 5: [5,8],6:[6,9],7:[7,10],8:[8,11],9:[9,12],10:[10,13],11:[11,14],12:[12,15],13:[13,16],14:[14,17],15:[15,18],16:[16,19],17:[17,20],18:[18,21],19:[19,22],20:[20,23],21:[21,24],22:[22,25],23:[23,26],24:[24,27],25:[25,28],26:[26,29],27:[27,30],28:[28,31],29:[29,32],30:[30,33],31:[31,34],32:[32,35],33:[33,36],34:[34,31],35:[35,32],36:[36,33]}
quad_map = {1: [1, 4,2,5], 2: [2, 5,3,6], 3: [3,6,2,5], 4: [4,7,8,5], 5: [5,8,9,6],6:[6,9,5,8],7:[7,10,8,11],8:[8,11,9,12],9:[9,12,8,11],10:[10,13,11,14],11:[11,14,12,15],12:[12,15,11,14],13:[13,16,14,17],14:[14,17,15,18],15:[15,18,14,17],16:[16,19,17,20],17:[17,20,18,21],18:[18,21,17,20],19:[19,22,20,23],20:[20,23,21,24],21:[21,24,20,23],22:[22,25,23,26],23:[23,26,24,27],24:[24,27,23,26],25:[25,28,26,29],26:[26,29,27,30],27:[27,30,26,29],28:[28,31,29,32],29:[29,32,30,33],30:[30,33,29,32],31:[31,34,32,35],32:[32,35,33,36],33:[33,36,32,35],34:[34,31,32,35],35:[35,32,33,36],36:[36,33,32,35]}

street_map = {1: [1, 2,3], 2: [1, 2,3], 3: [1, 2,3], 4: [4,5,6], 5: [4,5,6],6:[4,5,6],7:[7,8,9],8:[7,8,9],9:[7,8,9],10:[10,11,12],11:[10,11,12],12:[10,11,12],13:[13,14,15],14:[13,14,15],15:[13,14,15],16:[16,17,18],17:[16,17,18],18:[16,17,18],19:[19,20,21],20:[19,20,21],21:[19,20,21],22:[22,23,24],23:[22,23,24],24:[22,23,24],25:[25,26,27],26:[25,26,27],27:[25,26,27],28:[28,29,30],29:[28,29,30],30:[28,29,30],31:[31,32,33],32:[31,32,33],33:[31,32,33],34:[34,35,36],35:[34,35,36],36:[34,35,36]}

half_street_map = {1: [1, 2,3,4,5,6], 2: [1, 2,3,4,5,6], 3: [1, 2,3,4,5,6], 4: [4,5,6,7,8,9], 5: [4,5,6,7,8,9],6:[4,5,6,7,8,9],7:[7,8,9,10,11,12],8:[7,8,9,10,11,12],9:[7,8,9,10,11,12],10:[10,11,12,13,14,15],11:[10,11,12,13,14,15],12:[10,11,12,13,14,15],13:[13,14,15,16,17,18],14:[13,14,15,16,17,18],15:[13,14,15,16,17,18],16:[16,17,18,19,20,21],17:[16,17,18,19,20,21],18:[16,17,18,19,20,21],19:[19,20,21,22,23,24],20:[19,20,21,22,23,24],21:[19,20,21,22,23,24],22:[22,23,24,25,26,27],23:[22,23,24,25,26,27],24:[22,23,24,25,26,27],25:[25,26,27,28,29,30],26:[25,26,27,28,29,30],27:[25,26,27,28,29,30],28:[28,29,30,31,32,33],29:[28,29,30,31,32,33],30:[28,29,30,31,32,33],31:[31,32,33,34,35,36],32:[31,32,33,34,35,36],33:[31,32,33,34,35,36],34:[31,32,33,34,35,36],35:[31,32,33,34,35,36],36:[31,32,33,34,35,36]}
returns_list=[]
print("If roulette hits below numbers you will get repective amount")
for i in range(1, 37):
    returns = 0
    if i == bet_number:
        returns += (bet_amt * 36)
    # print(returns)
    if i in half_map[bet_number]:
        returns += (bet_amt * 18)
    # print(returns)
    if i in quad_map[bet_number]:
        returns += (bet_amt * 9)
    # print(returns)
    if i in street_map[bet_number]:
        returns += (bet_amt * 12)
    # print(returns)
    if i in half_street_map[bet_number]:
        returns += (bet_amt * 6)
    # print(returns)
    if i in first12 and bet_number in first12:
        returns += (bet_amt * 3)
    # print(returns)
    if i in second12 and bet_number in second12:
        returns += (bet_amt * 3)
    # print(returns)
    if i in third12 and bet_number in third12:
        returns += (bet_amt * 3)
    # print(returns)
    if i in top12 and bet_number in top12:
        returns += (bet_amt * 3)
    # print(returns)
    if i in middle12 and bet_number in middle12:
        returns += (bet_amt * 3)
    # print(returns)
    if i in bottom12 and bet_number in bottom12:
        returns += (bet_amt * 3)
    # print(returns)
    if (i >= 1 and i <= 18) and (bet_number>=1 and bet_number<=18):
        returns += (bet_amt * 2)
    # print(returns)
    if (i >= 19 and i <= 36) and (bet_number>=19 and bet_number<=36):
        returns += (bet_amt * 2)
    # print(returns)
    if i in red_numbers and bet_number in red_numbers:
        returns += (bet_amt * 2)
    # print(returns)
    if i in black_numbers and bet_number in black_numbers:
        returns += (bet_amt * 2)
    # print(returns)
    if i % 2 == 0 and bet_number%2==0:
        returns += (bet_amt * 2)
    # print(returns)
    if i % 2 == 1 and bet_number%2==1:
        returns += (bet_amt * 2)
    # print(returns)
    print(i, "=", returns)
    returns_list.append(returns)
returns_list.sort()
list_counter=Counter(returns_list)
print(list_counter)