import numpy
import random
import math


##check infinity
##check empty matrix
##check logarithm
##matrix with all infinities



def entropy(m):
    if len(m[0]) != 2:
        raise ValueError()
    if m == []:
        return 0

    values =[]
    ltot = 0
    _max = None
    infs = []
    
    for row in m:
        if row[1] == math.inf:
            infs.append(row)
            continue
        li = row[1] - row[0]
        values.append(li)
        ltot = ltot + li
        if _max == None or _max < row[1]:
            _max = row[1] 

    _max = _max + 1
    for row in infs:
        li = _max - row[0]
        values.append(li)
        ltot = ltot + li
        
        
    ret = 0
    for e in values:
        ret = ret + e/ltot * math.log(e/ltot)
    return -ret

if __name__ == '__main__':
    m = [[1,4],[4,7],[2,10],[5,30]]
    m1 =[[1,4],[4,7],[2,10],[5,math.inf]]
    print(m1)
    print(entropy(m1))
