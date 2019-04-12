from tkinter import*
import FrequencyFunctions as ff
import data_files as df
import tkinter.messagebox
import python_midi
import mido
from pythonosc import udp_client

# Patrick Tumulty 
# Last Updated: Feb. 28 2019

# ---------- instantiate our window ------------------


root = Tk()
root.title("TemperMental")
root.resizable(width=False, height=False)
root.config()

# ---------- window frames ----------------------------

inputFrame =    Frame(root)
freqList =      Frame(root)
chordButtons =  Frame(root)
sendOptions =   Frame(root)

# ---------- window frame .pack ------------------------

inputFrame.pack(side=TOP, padx=10, pady=10)
freqList.pack(side=TOP, padx=10, pady=10)
chordButtons.pack(side=TOP, padx=10, pady=10)
sendOptions.pack(side=TOP, padx=10, pady=10)

# ---------- gui variables ------------------------------

variable = StringVar()
radio = StringVar()
midiString = StringVar()
# inputDevice = StringVar()

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
    
def assign_midi(*args):
    midi_activate.config(state=NORMAL)
    global inputDevice
    inputDevice = midiString.get()


variable.trace('w', change_state) #checks to see which option has been selected
midiString.trace('w', assign_midi)
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

def set_midi_scale():
    if radio.get() == 'major':
        scale = df.read_data("MajorScale.txt")
        Two_Oct = df.extend_scale(scale)
        python_midi.open_midi_stream(Two_Oct, inputDevice)
    elif radio.get() == "new":
        scale = df.read_data("OtherScale.txt")
        Two_Oct = df.extend_scale(scale)
        python_midi.open_midi_stream(Two_Oct, inputDevice)

def one_chord():
    scale = get_file_data(1)
    triad = scale[1]
    my_client.send_message("/triad", triad[1:])
    print(scale)
def two_chord():
    scale = get_file_data(2)
    triad = scale[1]
    my_client.send_message("/triad", triad[1:])
    print(scale)
def three_chord():
    scale = get_file_data(3)
    triad = scale[1]
    my_client.send_message("/triad", triad[1:])
    print(scale)
def four_chord():
    scale = get_file_data(4)
    triad = scale[1]
    my_client.send_message("/triad", triad[1:])
    print(scale)
def five_chord():
    scale = get_file_data(5)
    triad = scale[1]
    my_client.send_message("/triad", triad[1:])
    print(scale)
def six_chord():
    scale = get_file_data(6)
    triad = scale[1]
    my_client.send_message("/triad", triad[1:])
    print(scale)
def seven_chord():
    scale = get_file_data(7)
    triad = scale[1]
    my_client.send_message("/triad", triad[1:])
    print(scale)
def eight_chord():
    scale = get_file_data(8)
    triad = scale[1]
    my_client.send_message("/triad", triad[1:])
    print(scale)

def midi_input_config():
    midi_setup_window = Tk()
    midi_setup_window.title("Midi Setup")
    midiLabel = Label(midi_setup_window, text="Select MIDI Input:", width=20)
    midiList = ["MIDI"]
    midiList.append(mido.get_input_names())
    midiOptions = OptionMenu(midi_setup_window, midiString, *midiList)
    midiLabel.pack()
    midiOptions.pack()
    midi_setup_window.mainloop()

def open_info_window():
    info = Tk()
    info.title("About")
    prog_file = open("ProgramInfo.txt", "r")
    words = prog_file.read()
    infoLabel = Label(info, text=words)
    infoLabel.pack(padx=10, pady=10)
    info.mainloop()

def client_config():
    global my_client
    my_client = udp_client.SimpleUDPClient("172.30.98.2", 57120)




    

# --------- Tkinter Widgets ---------------------------

ScaleOption =   OptionMenu(inputFrame, variable, "TET", "Just", "Pythagorean")

freqLabel =     Label(inputFrame, text="Frequency:")
scaleLabel =    Label(inputFrame, text="Choose Scale:")
freqColumn =    Label(freqList, text="Major Scale")
newColumn =     Label(freqList, text="New Scale")
centsColumn =   Label(freqList, text="Cents")

numEntry =      Entry(inputFrame, width=10, relief = SUNKEN)
OctaveDivider = Entry(inputFrame, width=10, state=DISABLED)
showButton =    Button(inputFrame, text="Show", command=addToList, state=DISABLED)
status =        Label(root, text="Welcome!", bd=1, relief=SUNKEN, anchor=W)


one =   Button(chordButtons, text="I", state=DISABLED, command = one_chord, width=8, height=3)    
two =   Button(chordButtons, text="II", state=DISABLED, command = two_chord, width=8, height=3)
three = Button(chordButtons, text="III", state=DISABLED, command = three_chord, width=8, height=3)
four =  Button(chordButtons, text="IV", state=DISABLED, command = four_chord, width=8, height=3)
five =  Button(chordButtons, text="V", state=DISABLED, command = five_chord, width=8, height=3)
six =   Button(chordButtons, text="VI", state=DISABLED, command = six_chord, width=8, height=3)
seven = Button(chordButtons, text="VII", state=DISABLED, command = seven_chord, width=8, height=3)
eight = Button(chordButtons, text="VIII", state=DISABLED, command = eight_chord, width=8, height=3)

midi_activate = Button(sendOptions, text="Start MIDI", width = 15, state=DISABLED, command=set_midi_scale)
soloMajor = Radiobutton(sendOptions, text="12 TET", variable=radio, value="major")
soloNew =   Radiobutton(sendOptions, text="New Scale", variable=radio, value="new")
clientConfig = Button(sendOptions, text="Config", width=15, command=client_config)
# Both =      Radiobutton(sendOptions, text="Both", variable=radio, value=)

majScale = Listbox(freqList, width=10)
newScale = Listbox(freqList, width=10)
centsOff = Listbox(freqList, width=10)

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

midi_activate.pack(side=BOTTOM)
clientConfig.pack(side=BOTTOM)
soloMajor.pack(side=LEFT)
soloNew.pack(side=LEFT)

# Both.pack(side=LEFT)

# ---------------------- Menu Bar --------------

# create a pulldown menu, and add it to the menu bar
menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Midi Config", command=midi_input_config)
filemenu.add_command(label="info", command=open_info_window)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)


# display the menu
root.config(menu=menubar)

# ---------------------- Frequency Scales --------------

freqColumn.grid(row=0, column=0, padx = 5)
newColumn.grid(row=0, column=1, padx = 5)
centsColumn.grid(row=0, column=2, padx = 5)

majScale.grid(row=1, column=0, padx = 5)
newScale.grid(row=1, column=1, padx = 5)
centsOff.grid(row=1, column=2, padx = 5)


root.mainloop() 


