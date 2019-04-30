from tkinter import*
import FrequencyFunctions as ff
import data_files as df
import tkinter.messagebox
import python_midi
import mido
from pythonosc import udp_client

# Patrick Tumulty 
# Last Updated: April. 25 2019

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
RatioVariable = StringVar()
radio = StringVar()
midiString = StringVar()
_ipAddress = "127.0.0.1"
inputDevice = StringVar()
homeAddress = IntVar()


# ---------- gui functions ------------------------------

def change_state(*args):
    """Updates the state of the program once a scale has been selected"""
    scale = variable.get()
    if scale == "TET":
        showButton.config(state=NORMAL)
        OctaveDivider.config(state=NORMAL)
        RatioOption.config(state=DISABLED)
        status.config(text="create a new equal tempered scale...")
    elif scale == "Just":
        showButton.config(state=NORMAL)
        OctaveDivider.config(state=DISABLED)
        RatioOption.config(state=DISABLED)
        status.config(text="create a just scale...")
    elif scale == "Pythagorean":
        showButton.config(state=NORMAL)
        OctaveDivider.config(state=DISABLED)
        RatioOption.config(state=DISABLED)
        status.config(text="create a pythagorean scale...")
    elif scale == "Ratio":
        showButton.config(state=NORMAL)
        OctaveDivider.config(state=DISABLED)
        RatioOption.config(state=NORMAL)
        status.config(text="create a scale based on a generator ratio...")


def change_ratio(*args):
    """ "3/2", "4/3", "5/4", "5/3", "9/8", "6/5" """
    ratio = RatioVariable.get()
    global GeneratorRatio
    if ratio == "3/2":
        GeneratorRatio = "3/2" # 1.5
    elif ratio == "4/3":
        GeneratorRatio = "4/3" # 1.333
    elif ratio == "5/4":
        GeneratorRatio = "5/4" # 1.25
    elif ratio == "5/3":
        GeneratorRatio = "5/3" # 1.667
    elif ratio == "9/8":
        GeneratorRatio = "9/8" # 1.125
    elif ratio == "6/5":
        GeneratorRatio = "6/5" # 1.2
     

def change_button_state(*args):
    """ Function waits for user to choose which scale they want to sonify and then activates the buttons  """
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

# ------------- Button State Variables ------------

variable.trace('w', change_state) #checks to see which option has been selected
midiString.trace('w', assign_midi)
radio.trace('w', change_button_state)
RatioVariable.trace('w', change_ratio)


def addToList():
    """ Populates the three GUI lists """
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
    elif variable.get() == "Ratio":
        frequency = float(numEntry.get())
        status.config(text="Major Scale / Ratio Scale / Cents Off...")
        MajScale = ff.StandardMajScale(frequency)
        otherScale = ff.RatioScale(frequency, GeneratorRatio)
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
    """Reads in text file, parses information, starts midi stream"""
    if radio.get() == 'major':
        scale = df.read_data("MajorScale.txt")
        Two_Oct = df.extend_scale(scale)
        open_midi_stream(Two_Oct, inputDevice, _ipAddress)
        # python_midi.open_midi_stream(Two_Oct, inputDevice, _ipAddress)
    elif radio.get() == "new":
        scale = df.read_data("OtherScale.txt")
        Two_Oct = df.extend_scale(scale)
        # python_midi.open_midi_stream(Two_Oct, inputDevice, _ipAddress)
        open_midi_stream(Two_Oct, inputDevice, _ipAddress)


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


def saveSettings():
    print(inputDevice)
    global _ipAddress
    _ipAddress = ipAddressEntry.get()
    status.config(text="Device: " + inputDevice + " IP Address: " + ipAddressEntry.get())
    client_config();
    print(_ipAddress)

def midi_input_config():
    midi_setup_window = Tk()
    set_up_screen = Frame(midi_setup_window)
    global ipAddressEntry
    midi_setup_window.title("Midi Setup")
    midiLabel = Label(set_up_screen, text="Select MIDI Input:", width=20)
    ipLabel = Label(set_up_screen, text="IP Address:", width=20)
    localIP = Label(set_up_screen, text="For Local Machine: 127.0.0.1")
    ipAddressEntry = Entry(set_up_screen)
    testButton = Button(set_up_screen, text="Save Settings", width=40, bg='red',command=saveSettings)
    midiList = ["MIDI"]
    devices = detect_midi()
    for item in devices:
        midiList.append(item)
    midiOptions = OptionMenu(set_up_screen, midiString, *midiList)
    set_up_screen.pack(padx=20, pady=20)
    midiLabel.grid(row=0, sticky='W')
    ipLabel.grid(row=1, sticky=W)
    midiOptions.grid(row=0, column=1)
    ipAddressEntry.grid(row=1, column=1)
    localIP.grid(row=2, column=1)
    testButton.grid(row=3, columnspan=2)
    midi_setup_window.mainloop()


def detect_midi():
    devices = []
    for item in mido.get_input_names():
        devices.append(item)
    return devices

def open_info_window():
    info = Tk()
    info.title("About")
    prog_file = open("ProgramInfo.txt", "r")
    words = prog_file.read()
    infoLabel = Label(info, text=words)
    infoLabel.pack(padx=10, pady=10)
    info.mainloop()

def open_help_window():
    info = Tk()
    info.title("Help Window")
    prog_file = open("HelpInfo.txt", "r")
    words = prog_file.read()
    infoLabel = Label(info, text=words)
    infoLabel.pack(padx=10, pady=10)
    info.mainloop()


def client_config():
    global my_client
    my_client = udp_client.SimpleUDPClient(_ipAddress, 57120)
    print("Client Config Successful")

def open_midi_stream(filename, midi_device, ip_Address):
    msg = mido.Message('note_on', note=60)
    freq_scale = df.extend_scale(filename)
    client = udp_client.SimpleUDPClient(ip_Address, 57120)
    with mido.open_input(midi_device) as inport:
        for msg in inport:
            if msg.note == 49: # 49 is C#3 which will end the stream
                break
            elif msg.note == 48:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[0])
                    print(freq_scale[0])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 50:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[1])
                    print(freq_scale[1])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 52:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[2])
                    print(freq_scale[2])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 53:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[3])
                    print(freq_scale[3])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 55:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[4])
                    print(freq_scale[4])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 57:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[5])
                    print(freq_scale[5])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 59:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[6])
                    print(freq_scale[6])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 60:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[7])
                    print(freq_scale[7])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 62:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[8])
                    print(freq_scale[8])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 64:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[9])
                    print(freq_scale[9])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 65:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[10])
                    print(freq_scale[10])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 67:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[11])
                    print(freq_scale[11])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 69:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[12])
                    print(freq_scale[12])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 71:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[13])
                    print(freq_scale[13])
                else:
                    client.send_message("/noteOff", 0)
            elif msg.note == 72:
                if msg.type == "note_on":
                    client.send_message("/noteOn", freq_scale[14])
                    print(freq_scale[14])
                else:
                    client.send_message("/noteOff", 0)
            ###### BLACK KEYS ######
            elif msg.note == 51:
                if msg.type == "note_on":
                    scale = get_file_data(1)
                    triad = scale[1]
                    my_client.send_message("/triad", triad[1:])
                    print("Chord 1")
            elif msg.note == 54:
                if msg.type == "note_on":
                    scale = get_file_data(2)
                    triad = scale[1]
                    my_client.send_message("/triad", triad[1:])
                    print("Chord 2")
            elif msg.note == 56:
                if msg.type == "note_on":
                    scale = get_file_data(3)
                    triad = scale[1]
                    my_client.send_message("/triad", triad[1:])
                    print("Chord 3")
            elif msg.note == 58:
                if msg.type == "note_on":
                    scale = get_file_data(4)
                    triad = scale[1]
                    my_client.send_message("/triad", triad[1:])
                    print("Chord 4")
            elif msg.note == 61:
                if msg.type == "note_on":
                    scale = get_file_data(5)
                    triad = scale[1]
                    my_client.send_message("/triad", triad[1:])
                    print("Chord 5")
            elif msg.note == 63:
                if msg.type == "note_on":
                    scale = get_file_data(6)
                    triad = scale[1]
                    my_client.send_message("/triad", triad[1:])
                    print("Chord 6")
            elif msg.note == 66:
                if msg.type == "note_on":
                    scale = get_file_data(7)
                    triad = scale[1]
                    my_client.send_message("/triad", triad[1:])
                    print("Chord 7")
            elif msg.note == 68:
                if msg.type == "note_on":
                    scale = get_file_data(8)
                    triad = scale[1]
                    my_client.send_message("/triad", triad[1:])
                    print("Chord 8")
            elif msg.note == 70:
                if msg.type == "note_on":
                    my_client.send_message("/triad", [0,0,0])
                    print("Chords OFF")
            print(msg.type)


# --------- Tkinter Widgets ---------------------------

ScaleOption =   OptionMenu(inputFrame, variable, "TET", "Just", "Pythagorean", "Ratio")
RatioOption =   OptionMenu(inputFrame, RatioVariable, "3/2", "4/3", "5/4", "5/3", "9/8", "6/5")

freqLabel =     Label(inputFrame, text="Frequency:")
scaleLabel =    Label(inputFrame, text="Choose Scale:")
freqColumn =    Label(freqList, text="Major Scale")
newColumn =     Label(freqList, text="New Scale")
centsColumn =   Label(freqList, text="Cents")

numEntry =      Entry(inputFrame, width=10, relief = SUNKEN)
OctaveDivider = Entry(inputFrame, width=10, state=DISABLED)
showButton =    Button(inputFrame, text="Show", command=addToList, state=DISABLED, fg="red")
status =        Label(root, text="Welcome!", bd=1, relief=SUNKEN, anchor=W)

one =   Button(chordButtons, text="I", state=DISABLED, fg="blue", command = one_chord, width=8, height=3)    
two =   Button(chordButtons, text="II", state=DISABLED, fg="red", command = two_chord, width=8, height=3)
three = Button(chordButtons, text="III", state=DISABLED, fg="#F3E90A", command = three_chord, width=8, height=3)
four =  Button(chordButtons, text="IV", state=DISABLED, fg="green", command = four_chord, width=8, height=3)
five =  Button(chordButtons, text="V", state=DISABLED, fg="purple", command = five_chord, width=8, height=3)
six =   Button(chordButtons, text="VI", state=DISABLED, fg="orange", command = six_chord, width=8, height=3)
seven = Button(chordButtons, text="VII", state=DISABLED, fg="cyan", command = seven_chord, width=8, height=3)
eight = Button(chordButtons, text="VIII", state=DISABLED, fg="blue", command = eight_chord, width=8, height=3)

midi_activate = Button(sendOptions, text="Start MIDI", width = 15, fg="blue", state=DISABLED, command=set_midi_scale)
soloMajor = Radiobutton(sendOptions, text="12 TET", variable=radio, value="major")
soloNew =   Radiobutton(sendOptions, text="New Scale", variable=radio, value="new")

# clientConfig = Button(sendOptions, text="Config", width=15, command=client_config)
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
RatioOption.grid(row=3, column=0)
status.pack(side=BOTTOM, fill=X)

one.grid(row=0, column=0)
two.grid(row=0, column=1)
three.grid(row=0, column=2)
four.grid(row=0, column=3)
five.grid(row=1, column=0)
six.grid(row=1, column=1)
seven.grid(row=1, column=2)
eight.grid(row=1, column=3)

midi_activate.pack(side=BOTTOM, padx=10, pady=10)
# clientConfig.pack(side=BOTTOM, padx=10, pady=10)
soloMajor.pack(side=LEFT)
soloNew.pack(side=LEFT)


# ---------------------- Menu Bar --------------

# create a pulldown menu, and add it to the menu bar
menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Midi Config", command=midi_input_config)
filemenu.add_command(label="About", command=open_info_window)
filemenu.add_command(label="Help", command=open_help_window)
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


