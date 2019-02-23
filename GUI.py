from tkinter import*
from FrequencyFunctions import*
import tkinter.messagebox

#Patrick Tumulty 
# Feb. 23 2019


root = Tk()
root.title("TemperMental")
a = (12, 13, 45, 65)
b = (15, 56, 76, 98)
c = []
for i in range(len(a)):
    val = a[i] - b[i]
    c.append(val)
    
freqDisplayA = Frame(root)
freqDisplayA.pack(side=LEFT)

scaleValA = Listbox(freqDisplayA)
for i in range(len(a)):
    scaleValA.insert((i+1), a[i])

scaleValB = Listbox(freqDisplayA)
for i in range(len(a)):
    scaleValB.insert((i+1), b[i])

scaleValC = Listbox(freqDisplayA)
for i in range(len(a)):
    scaleValC.insert((i+1), c[i])
    
scaleValA.pack()
scaleValB.pack()
scaleValC.pack()


root.mainloop() 
