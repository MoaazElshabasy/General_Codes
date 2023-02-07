import random
import math
def temp(i,team):
    l = []
    l = i
    stop = len(l)/team
    c = 0
    x =0
    while c < team:
        temp = []
        i = 0
        if len(l) == math.ceil(stop):
            stop = stop
        elif c == team - 2:
            stop = len(l)/2
        while i < stop:
            if len(l) >0 :
                player = random.randint(0, len(l)-1)
                temp.append(l[player])
                l.remove(l[player])
                i += 1  
            else:
                break
        if temp == []:
            break
        else:         
            print(temp)
        c+=1
if __name__ == "__main__":
    players = ['Matthew','Moaaz','Aaron','Luke','Miguel','Mezo','Matt','son of odin', 'Mig', 'Civil guy', 'Galactic Commander','Blood Prince', 'Mezosphere', 'Crashex', 'Time bender Mozetron', 'Raging Phoneix', 'night claw', 'Dark banishers']
    print(len(players))
    temp(players,8)
