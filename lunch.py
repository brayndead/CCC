import math
nPpl = int(input()) #len(people)
people = []
positionsMap = {}
positions = []
#all positions where ideal concert can possibly be held
for i in range(nPpl):
    person = input().split(' ')
    pos = int(person[0])
    hear = int(person[2])
    people.append({
        'pos': int(person[0]),
        'vel': int(person[1]),
        'hear': int(person[2])
    })
    positionsMap[int(person[0])] = True
    positionsMap[pos - hear] = True
    positionsMap[pos + hear] = True
for i in positionsMap:
    positions.append(i)
positions.sort()
searching = True
if nPpl ==  1:
    print(0)
else:
    while searching:
        wLeft = 0
        wRight = 0
        mid = math.floor(len(positions)/2)
        pos = positions[mid]
        # check whether left w is bigger or right w is bigger at this position
        for i in people:
            dist = i['pos'] - pos
            if dist > 0:
                #right
                dist = dist - i['hear']
                if dist < 0:
                    #its actually ontop
                    continue
                else:
                    #we add the w
                    wRight += i['vel']
            elif dist < 0:
                #left
                dist = dist + i['hear']
                if dist > 0:
                    #its actually ontop
                    continue
                else:
                    #we add the  w
                    wLeft += i['vel']
        if wLeft> wRight:
            positions = positions[0:mid+ 1]
            #move left, get rid of the right
        else:
            positions = positions[mid:len(positions)]
            #move right, get rid of the left
        if len(positions) == 2:
            searching = False
    timeSum = 0
    for i in people:
        dist = i['pos'] - positions[0]
        if dist > 0:
            #right
            dist = dist - i['hear']
            if dist < 0:
                #its actually ontop
                continue
            else:
                #we add the w
                timeSum +=dist *  i['vel']
        elif dist < 0:
            #left
            dist = dist + i['hear']
            if dist > 0:
                #its actually ontop
                continue
            else:
                dist = -dist
                #we add the time 
                timeSum += dist * i['vel']

    timeSum1 = 0

    for i in people:
        dist = i['pos'] - positions[1]
        if dist > 0:
            #right
            dist = dist - i['hear']
            if dist < 0:
                #its actually ontop
                continue
            else:
                #we add the w
                timeSum1 += dist * i['vel']
        elif dist < 0:
            #left
            dist = dist + i['hear']
            if dist > 0:
                #its actually ontop
                continue
            else:
                dist = -dist
                #we add the time 
                timeSum1 += dist * i['vel']
    print(min(timeSum1, timeSum))
