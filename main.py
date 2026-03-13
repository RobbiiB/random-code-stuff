import re


## Question 1 ##


records = "PaperA 1 PaperB 1 PaperC 1 PaperD 1 PaperE 1"

rawdata:list = records.split(" ")
data:list = []
for row in rawdata:
    try:
        data.append(int(row))
    except:
        pass

#order the data from biggest to smallest
data.sort(reverse=True)    


h:int=0

#iterate through the data to find the smallest index that is bigger than the number of citations
for i,num in enumerate(data):
    if i+1>=num:
        h=num
        break
    else:
        h=0

print(f"The h-index for this author is {h}")


## Question 2 ##

##input
spell_book = {
'Bing': {
'mana': 10,
'damage': 10,
'element': 'wind'
},
'Bong': {
'mana': 20,
'damage': 20,
'element': 'earth'
},
'Bang': {
'mana': 30,
'damage': 30,
'element': 'metal'
}
}
weakness = ['wind', 'earth']
spells_casted = ['Bing', 'Bong', 'Bang']

def damage_dealt(spell_book:dict, weakness:list, spells_casted:list):
    total_damage:int = 0
    for casted_spell in spells_casted:
        try:
            dmg = spell_book[casted_spell]["damage"]
            if spell_book[casted_spell]["element"] in weakness:
                dmg*=2
        except:
            dmg=0
        
        total_damage+=dmg
    return total_damage

print(f"A total of {damage_dealt(spell_book,weakness,spells_casted)} was dealt")


## problem 3 ##


class Box():
    def __init__(self, num_packs = 36, cards_per_pack = 10, card_weight = 1.8, empty_pack_weight = 1.0, empty_box_weight = 121.2):
        self.num_packs:int = num_packs
        self.cards_per_pack:int = cards_per_pack
        self.card_weight:float = card_weight
        self.empty_pack_weight:float = empty_pack_weight
        self.empty_box_weight:float = empty_box_weight
    
    def box_weight(self):
        weight = self.empty_box_weight + self.num_packs*self.empty_pack_weight + self.num_packs*self.cards_per_pack*self.card_weight
        return weight

## input
new_box = Box(num_packs=30, cards_per_pack=5)

print(f"The weight of this box is {new_box.box_weight()}")


## problem 4 ##

##input
k = 2
power = [20, 15, 16, 18]

patronus_power =[]
for i in range(len(power)-1):
    patronus_power.append(power[i] + power[i+1])
patronus_power.sort()


power_diff = 0
for i in range(k):
    power_diff+= patronus_power[-i-1]-patronus_power[i]

print(power_diff)


## problem 5 ##


## input
w = "BAADD"
s = "AD"


while True:
    if w==w.replace(s,""):
        break
    w = w.replace(s,"")
print(w)


## problem 6 ##

## input
w = "ABBBABA"

def does_not_contain_AAB(w): 
    marker="AAB"
    if re.search(marker,w)==None:
        return True
    else:
        return False

print(f"{does_not_contain_AAB(w)}")
