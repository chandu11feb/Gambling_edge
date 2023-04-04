import random
cards_deck=[]
# clubs=["♣️A01","♣️️02","♣️️03","♣️04","♣️️05","♣️06","♣️️07","♣️️08","♣️️09","♣️️10","♣️️J11","♣️️Q12","♣️️K13"]
# diamonds=["♦️A01","♦️02","♦️03","♦️04","♦️05","♦️06","♦️07","♦️08","♦️09","♦️10","♦️J11","♦️Q12","♦️K13"]
# hearts=["❤️A01","❤️02","❤️03","❤️️04","❤️️05","❤️06","❤️07","❤️️08","❤️09","❤️️10","❤️️J11","❤️️Q12","❤️️K13"]
# spades=["♠️A01","♠️️02","♠️️03","♠️04","♠️️05","♠️️06","♠️️07","♠️️08","♠️️09","♠️️10","♠️️J11","♠️️Q12","♠️️K13"]
deck = [f"{suit}{rank}" for rank in "23456789TJQKA" for suit in "SCDH"]
for _ in range(8):
    cards_deck.extend(deck)
    random.shuffle(cards_deck)
print(cards_deck)
print(len(cards_deck))
for _ in range(3):
    random.shuffle(cards_deck)
searching_deck_list=[]
current_cards_list=['D5','S3','H5']
if current_cards_list[0] in "".join(cards_deck):
    print(current_cards_list)
print(cards_deck)