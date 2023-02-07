import random
from array import *

i = 0
while i == 0:
    print (" quit\n massum\n sort\n hash table")
    k = input ()

    if k == 'massum':

        print("enter len mass")
        n=1
        n=int(input (n))
        mass1 = [0]*n
        mass2 = [0]*n
        for m in range(n):
            mass1[m] = int(input(mass1 [m]))
        print("enter mass2")
        for m in range(n):
            mass2[m] = int(input(mass2[m]))
        for m in range(n):
            mass1[m] += mass2[m]
            print (mass1[m])
        print (mass1)

    if k == 'sort':
        j = 9
        j = int(input(j))
        sortmass = [0]*j
        for m in range(j):
            sortmass[m] = random.randint(1,99)
            print (sortmass[m])
        def sort(sortmass):
            if len(sortmass)<=1:
                return sortmass
            piv= sortmass[0]
            left = list (filter(lambda x: x<piv, sortmass))
            center = [i for i in sortmass if i == piv]
            right = list(filter(lambda x: x > piv, sortmass))
            return sort(left) + center + sort(right)
        print(sort(sortmass))

    if k == 'hash table':


    if k == 'quit':
         i = 1
    print (i)

print ('end with ', i)