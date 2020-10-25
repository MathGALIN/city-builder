"""expérience pour savoir comment faire pour détecter si les batiments sont connecter entre eux"""

h = "h"
r = "r"
v = "v"



map = [
[h, r, r],
[v, v, r]
]



"""Système pour faire les connexion entre plusieurs lieux"""

redo = True

while redo == True :
    redo = False

    for y in range(0, len(map)) :
        for x in range(0, len(map[y])) :
            if map[y][x] == r :

                for s in [-1, 1] :

                    """Pour l'axe x"""
                    if x + s >= 0 :
                        try :
                            if map[y][x+s] == h :
                                map[y][x] = h
                                redo = True
                        except : pass


                    """Pour l'axe y"""
                    if y + s >= 0 :
                        try :
                            if map[y+s][x] == h :
                                map[y][x] = h
                                redo = True
                        except : pass

for y in map :
    print(y)