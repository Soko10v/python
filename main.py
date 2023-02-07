import random
from tkinter import *
from tkinter import ttk
#from array import *

def massum():
    print("enter len mass")
    n = 1
    n = int(input(n))
    mass1 = [0] * n
    mass2 = [0] * n
    for m in range(n):
        mass1[m] = int(input(mass1[m]))
    print("enter mass2")
    for m in range(n):
        mass2[m] = int(input(mass2[m]))
    for m in range(n):
        mass1[m] += mass2[m]
        print(mass1[m])
    print(mass1)
    return mass1
def quicksort(i):
    j = i
   # j = int(input(j))
    sortmass = [0] * j
    for m in range(j):
        sortmass[m] = random.randint(1, 99)
        #print(sortmass[m])

    def sort(sortmass):
        if len(sortmass) <= 1:
            return sortmass
        piv = sortmass[0]
        left = list(filter(lambda x: x < piv, sortmass))
        center = [i for i in sortmass if i == piv]
        right = list(filter(lambda x: x > piv, sortmass))
        return sort(left) + center + sort(right)

    print(sort(sortmass))
    return sortmass

root =Tk()
root['bg'] = '#fafafa'
root.title=('basics')
root.geometry('700x450')
root.resizable(width=False, height=False)

frame = Frame(root, bg='grey')
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='text1', bg="white", font="40")
title.place(relx=0.5,rely=0.5)

def show_message():
    label["text"] = quicksort(int(entry.get()))

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)


btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

root.mainloop()

i = 0
while i == 0:
    print (" quit\n massum\n sort")
    k = input ()
    if k == 'massum':
        massum()
    if k == 'sort':
        quicksort(7)
    if k != 'quit':
        pass
    else:
        i = 1
   # print (i)
print ('end with ', i)