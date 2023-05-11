string = []
temp = input().split(' ') 
n = int(temp[0])
m = int(temp[1])
k  = int(temp[2])
string = []
if m >n:
    m = n
if k >= n and k <= (m * (2*n - m + 1))//2:
    count = 1
    while k >0: #seems unnecessary as will only come into effect if k is exactly something
        #first, check to see if we can add the max. if remaining number of elemtents - 1 + max is less than k, then we can add the max
        if len(string) < m:
            if n - len(string) -1 + count <= k:
                string.append(str(count))
                k -= count
                count += 1
            else: # ok we cant add the max, we have to add either 1,2,3 . . . max -1 followed by a bunch of 1s.
                diff = k -  (n - len(string) - 1)#how much we have to add right now This is obviously less than count
                string.append(string[len(string) - diff]) #does this make sense? there is exactly diff yes. This makes sense
                for i in range(n - len(string)):
                    string.append(string[len(string) - 1]) #append a bunch of +1s to full
                break
        else:
            if n - len(string) - 1 + m <= k:
                string.append(str(count))
                k -= m
                count += 1
            else:
                diff = k -  (n - len(string) - 1)
                string.append(string[len(string) - diff])
                for i in range(n - len(string)):
                    string.append(string[len(string) - 1])
                break
        if count == m+1: #count cycles
            count = 1
    print(' '.join(string))
else:
    print('-1')
