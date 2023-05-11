M = int(input()) #number of pens
import copy
pens = {}
walls = {}
def get_other(set, pens):
    for i in set:
        if i != 0 and i in pens:
            return i

def get_el(set):
    for i in set:
        return i
def process(w_cost, w_id):
    if w_id in walls: #if this wall has shown up before
        pens[i][w_id] = w_cost
        walls[w_id]['pens'].add(i)
    else:
        walls[w_id] = {}
        walls[w_id]['pens'] = {i}
        walls[w_id]['cost'] = w_cost
        pens[i][w_id] = w_cost
for i in range(M) 
    pens[i] = {}
    t = input().split()
    num_w = int(t.pop(0))
    pens[i] = {}
    for i2 in range(num_w): #add these walls if they are not redundant If this is the first time the wall shows up, it cannot be redundant
        if i2 == num_w - 1:
            process(int(t[num_w + i2]), frozenset({t[i2], t[0]}))
        else:
            process(int(t[num_w + i2]), frozenset({t[i2 + 1], t[i2]}))
tot_cost_1 = 0
tot_cost_2 = 0
pens['out'] = {}
for i in walls:
    if len(walls[i]['pens']) == 1: #this is an outer wall
        pens['out'][i] = walls[i]['cost']
        walls[i]['pens'].add('out')
bens = copy.deepcopy(pens)

while len(pens) > 1: #our get everything route
    pen = pens[0]
    #find the cheapest wall that mayhaps be broken
    wall = ''
    for i in pen:
        if wall == '':
            wall = i
        else:
            if pen[i] < pen[wall]:
                wall = i
    #now we have the cheapest wall, we break it perhaps
    other_p = get_other(walls[wall]['pens'], pens)
    if other_p != None:
        tot_cost_1 += pen[wall]
        del pen[wall]
        del pens[other_p][wall]
        #now we need to add all the walls from other_p to pen
        for i in pens[other_p]:
            pen[i] = pens[other_p][i]
        del pens[other_p]
    else:
        del pen[wall] #this is just a dud
while len(bens) > 2:
    pen = bens[0]
    #find the cheapest wall that mayhaps be broken
    wall = ''
    for i in pen:
        if get_other(walls[i]['pens'], bens) != 'out':
            if wall == '':
                wall = i
            else:
                if pen[i] < pen[wall]:
                    wall = i
    #now we have the cheapest wall, we break it
    if wall == '': #if there is no wall except for out walls and we still have bens remaining, we know this is a dud.
        tot_cost_2 = tot_cost_1 + 1
        break
    else:
        other_p = get_other(walls[wall]['pens'], bens)
        if other_p != None:
            tot_cost_2 += pen[wall]
            del pen[wall]
            del bens[other_p][wall]
            #now we need to add all the walls from other_p to pen
            for i in bens[other_p]:
                pen[i] = bens[other_p][i]
            del bens[other_p]
        else:
            del pen[wall]
print(min(tot_cost_2, tot_cost_1))


