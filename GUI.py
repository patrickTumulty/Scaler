from tkinter import*
import FrequencyFunctions as ff
import data_files as df
import tkinter.messagebox

# Patrick Tumulty 
# Last Updated: Feb. 28 2019

# ---------- instantiate our window ------------------
# bg_color = "#F6FAF9"
# button_color = "#FFFFFF"

bg_color = "#D7D7D7"
button_color = "#D7D7D7"

root = Tk()
root.title("TemperMental")
root.resizable(width=False, height=False)
root.config(background = bg_color)

# ---------- window frames ----------------------------

inputFrame =    Frame(root, background = bg_color)
freqList =      Frame(root, background = bg_color)
chordButtons =  Frame(root, background = bg_color)
sendOptions =   Frame(root, background = bg_color)

# ---------- window frame .pack ------------------------

inputFrame.pack(side=TOP, padx=10, pady=10)
freqList.pack(side=TOP, padx=10, pady=10)
chordButtons.pack(side=TOP, padx=10, pady=10)
sendOptions.pack(side=TOP, padx=10, pady=10)

# ---------- gui variables ------------------------------

variable = StringVar()
radio = StringVar()

# ---------- gui functions ------------------------------

def change_state(*args):
    """Updates the state of the program once a scale has been selected"""
    scale = variable.get()
    if scale == "TET":
        showButton.config(state=NORMAL)
        OctaveDivider.config(state=NORMAL)
        status.config(text="create a new equal tempered scale...")
    elif scale == "Just":
        showButton.config(state=NORMAL)
        OctaveDivider.config(state=DISABLED)
        status.config(text="create a just scale...")
    elif scale == "Pythagorean":
        showButton.config(state=NORMAL)
        OctaveDivider.config(state=DISABLED)
        status.config(text="create a pythagorean scale...")


def change_button_state(*args):
    if radio.get() == "major":
        print("12TET")
        one.config(state=NORMAL)
        two.config(state=NORMAL)
        three.config(state=NORMAL)
        four.config(state=NORMAL)
        five.config(state=NORMAL)
        six.config(state=NORMAL)
        seven.config(state=NORMAL)
        eight.config(state=NORMAL)
    elif radio.get() == "new":
        print("New Scale")
        one.config(state=NORMAL)
        two.config(state=NORMAL)
        three.config(state=NORMAL)
        four.config(state=NORMAL)
        five.config(state=NORMAL)
        six.config(state=NORMAL)
        seven.config(state=NORMAL)
        eight.config(state=NORMAL)


variable.trace('w', change_state) #checks to see which option has been selected
radio.trace('w', change_button_state)


def addToList():
    majScale.delete(0, END)
    newScale.delete(0, END)
    centsOff.delete(0, END)
    global otherScale
    global MajScale
    if variable.get() == "TET":
        frequency = float(numEntry.get())
        octDivider = int(OctaveDivider.get())
        status.config(text="Major Scale / New TET Scale / Cents Off...")
        MajScale = ff.StandardMajScale(frequency)
        otherScale = ff.TETMajScale(frequency, octDivider) 
        cents = ff.calculateCents(MajScale, otherScale)
        for i in range(len(MajScale)):
            val = MajScale[i]
            majScale.insert(END, val)
        for i in range(len(otherScale)):
            val = otherScale[i]
            newScale.insert(END, val)
        for i in range(len(cents)):
            val = cents[i]
            centsOff.insert(END, int(val))
        df.write_data("MajorScale.txt", MajScale)
        df.write_data("OtherScale.txt", otherScale)
    elif variable.get() == "Just":
        frequency = float(numEntry.get())
        status.config(text="Major Scale / Just Scale / Cents Off...")
        MajScale = ff.StandardMajScale(frequency)
        otherScale = ff.JustScale(frequency)
        cents = ff.calculateCents(MajScale, otherScale)
        df.write_data("MajorScale.txt", MajScale)
        df.write_data("OtherScale.txt", otherScale)
        for i in range(len(MajScale)):
            val = MajScale[i]
            majScale.insert(END, val)
        for i in range(len(otherScale)):
            val = otherScale[i]
            newScale.insert(END, val)
        for i in range(len(cents)):
            val = cents[i]
            centsOff.insert(END, int(val))    
        df.write_data("MajorScale.txt", MajScale)
        df.write_data("OtherScale.txt", otherScale)
    elif variable.get() == "Pythagorean":
        frequency = float(numEntry.get())
        status.config(text="Major Scale / Pythagorean Scale / Cents Off...")
        MajScale = ff.StandardMajScale(frequency)
        otherScale = ff.PythagoreanScale(frequency)
        cents = ff.calculateCents(MajScale, otherScale)
        for i in range(len(MajScale)):
            val = MajScale[i]
            majScale.insert(END, val)
        for i in range(len(otherScale)):
            val = otherScale[i]
            newScale.insert(END, val)
        for i in range(len(cents)):
            val = cents[i]
            centsOff.insert(END, int(val))
        df.write_data("MajorScale.txt", MajScale)
        df.write_data("OtherScale.txt", otherScale)
            

def get_file_data(scaledegree):
    """input scale degree. pulls data from the data file (depending on radio button) and runs the scale through genblock"""
    if radio.get() == "major":
        scale = df.read_data("MajorScale.txt")
        block = ff.genBlock(scale, scaledegree)
        return block
    elif radio.get() == "new":
        scale = df.read_data("OtherScale.txt")
        block = ff.genBlock(scale, scaledegree)
        return block

def one_chord():
    scale = get_file_data(1)
    print(scale)
def two_chord():
    scale = get_file_data(2)
    print(scale)
def three_chord():
    scale = get_file_data(3)
    print(scale)
def four_chord():
    scale = get_file_data(4)
    print(scale)
def five_chord():
    scale = get_file_data(5)
    print(scale)
def six_chord():
    scale = get_file_data(6)
    print(scale)
def seven_chord():
    scale = get_file_data(7)
    print(scale)
def eight_chord():
    scale = get_file_data(8)
    print(scale)


# --------- Tkinter Widgets ---------------------------

ScaleOption =   OptionMenu(inputFrame, variable, "TET", "Just", "Pythagorean")
ScaleOption.config(bg = bg_color)
freqLabel =     Label(inputFrame, text="Frequency:", bg = bg_color)
scaleLabel =    Label(inputFrame, text="Choose Scale:", bg = bg_color)
freqColumn =    Label(freqList, text="Major Scale", bg = bg_color )
newColumn =     Label(freqList, text="New Scale", bg = bg_color)
centsColumn =   Label(freqList, text="Cents", bg = bg_color)

numEntry =      Entry(inputFrame, width=10, relief = SUNKEN, highlightbackground = bg_color, bg = button_color)
OctaveDivider = Entry(inputFrame, width=10, state=DISABLED, highlightbackground = bg_color, bg = button_color)
showButton =    Button(inputFrame, text="Show", command=addToList, state=DISABLED, highlightbackground=bg_color)
status =        Label(root, text="Welcome!", bd=1, relief=SUNKEN, anchor=W, bg = bg_color)


one =   Button(chordButtons, text="I", state=DISABLED, command = one_chord, width=8, height=3, highlightbackground=button_color)    
two =   Button(chordButtons, text="II", state=DISABLED, command = two_chord, width=8, height=3, highlightbackground=button_color)
three = Button(chordButtons, text="III", state=DISABLED, command = three_chord, width=8, height=3, highlightbackground=button_color)
four =  Button(chordButtons, text="IV", state=DISABLED, command = four_chord, width=8, height=3, highlightbackground=button_color)
five =  Button(chordButtons, text="V", state=DISABLED, command = five_chord, width=8, height=3, highlightbackground=button_color)
six =   Button(chordButtons, text="VI", state=DISABLED, command = six_chord, width=8, height=3, highlightbackground=button_color)
seven = Button(chordButtons, text="VII", state=DISABLED, command = seven_chord, width=8, height=3, highlightbackground=button_color)
eight = Button(chordButtons, text="VIII", state=DISABLED, command = eight_chord, width=8, height=3, highlightbackground=button_color)

soloMajor = Radiobutton(sendOptions, text="12 TET", variable=radio, value="major", bg = bg_color)
soloNew =   Radiobutton(sendOptions, text="New Scale", variable=radio, value="new", bg = bg_color)
# Both =      Radiobutton(sendOptions, text="Both", variable=radio, value=)

majScale = Listbox(freqList, width=10, bg = button_color)
newScale = Listbox(freqList, width=10, bg = button_color)
centsOff = Listbox(freqList, width=10, bg = button_color)

# ---------------------- Buttons, Entry, and Label pack ------------

showButton.grid (row=0, columnspan=3)
freqLabel.grid(row=1, column=0)
scaleLabel.grid(row=2, column=0)
numEntry.grid(row=1, column=1)
OctaveDivider.grid(row=3, column=1)
ScaleOption.grid(row=2, column=1)
status.pack(side=BOTTOM, fill=X)

one.grid(row=0, column=0)
two.grid(row=0, column=1)
three.grid(row=0, column=2)
four.grid(row=0, column=3)
five.grid(row=1, column=0)
six.grid(row=1, column=1)
seven.grid(row=1, column=2)
eight.grid(row=1, column=3)

soloMajor.pack(side=LEFT)
soloNew.pack(side=LEFT)
# Both.pack(side=LEFT)

# ---------------------- Frequency Scales --------------

freqColumn.grid(row=0, column=0, padx = 5)
newColumn.grid(row=0, column=1, padx = 5)
centsColumn.grid(row=0, column=2, padx = 5)

majScale.grid(row=1, column=0, padx = 5)
newScale.grid(row=1, column=1, padx = 5)
centsOff.grid(row=1, column=2, padx = 5)


root.mainloop() 



"""
text file for left scale, text for middle scale. 
Writes scale to text file
Whenever we press a button, read from a text file 

step one:
    create scales and send to lists in GUI. Write those scales to a text file
step two:
    bring those scales back into our program and turn them into arrays
step three:
    use buttons and feed the scales into gen block 

csv 
Major scale and other scale separate text files
    read newest line 
    append next scale 


overwrite file 
SQLITE3
Databases 


"""