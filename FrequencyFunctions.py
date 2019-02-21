import numpy as np
import math
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from random import*


def Create12TETChromatic(frequency):
    """creates a 12 tone even tempered scale with any starting pitch. returns an array"""
    i = 0
    scale = np.array([])
    while i < 12:
        i += 1
        note = round(frequency * (2**(i/12)), 2)      # divides octave into 12 even pitches
        scale = np.append(scale, note)      # adds pitches to an array
    scale = np.insert(scale, 0, frequency)  # adds starting pitch to our scale
    return scale


def TETChromaticScale(frequency, octaveDivider):
    """creates an even tempered scale with a given starting frequency and a number for how many divisions you want the
    octave to be diveded into. Returns an Array"""
    i = 0
    scale = np.array([])
    while i < octaveDivider:
        i += 1
        note = round(frequency * (2**(i/octaveDivider)), 2)
        scale = np.append(scale, note)
    scale = np.insert(scale, 0, frequency)
    return scale


def sinWavGen(frequency, duration):
    """ Creates a sin wave with a given frequency and a duration (in seconds). returns an array"""
    sampleRate = 44100
    twoPi = 2 * math.pi
    sampleRate *= duration    # is in seconds
    timeArray = np.arange(sampleRate)
    digiPeriod = 1 / sampleRate
    sinArray = np.array([])
    for i in range(len(timeArray)):
        t = i * digiPeriod              # t effects how long our pitch is. Changing the sampleRate will change dur.
        wav = np.sin(twoPi * (frequency * t))
        sinArray = np.append(sinArray, wav)
    return sinArray


def WriteScale(pitchArray, noteDur):
    """Takes an array of pitches, as well as a note duration (in seconds) and arranges them into a
    chromatic scale using a sin tone. Returns an array"""
    i = 0
    sound = np.array([])
    print(len(pitchArray))
    while i < len(pitchArray):
        pitch = sinWavGen(pitchArray[i], noteDur)
        sound = np.append(sound, pitch)
        i += 1
    return sound


def RandMelody(pitchArray, noteDur):
    """Takes an array of pitches, as well as a note duration (in seconds) and arranges them into a
    random melody using a sin tone. Returns an array"""
    i = 0
    sound = np.array([])
    print(len(pitchArray))
    while i < (len(pitchArray)-1):
        rand = randint(0, len(pitchArray)-1)
        pitch = sinWavGen(pitchArray[rand], noteDur)
        sound = np.append(sound, pitch)
        i += 1
    return sound


def write2wav(sinArray):
    """Scales your array to values between 1 and 0 and converts it to a 16 bit int. Write
    a wav file of that data"""
    sampleRate = 44100
    scaled = np.int16(sinArray / np.max(np.abs(sinArray)) * 32767)
    write("ChromaticScale.wav", sampleRate, scaled)

# Functions used TETMajScale


def StandardMajScale(TETArray):
    """Takes an array of frequencies of a 12 tone chromatic scale and returns a traditional
    major scale"""
    EightSteps = np.array([])
    freqArray = TETArray
    steps = (0, 2, 4, 5, 7, 9, 11, 12)
    for i in steps:
        scale = freqArray[i]
        EightSteps = np.append(EightSteps, scale)
    return EightSteps


def SecondLoop(frequency, newTET):
    """This function is used only in conjunction with DetermineScale()"""
    absList = []
    minimum = 0
    for i in range(len(newTET)):
        absVal = np.round(abs(newTET[i] - frequency))
        absList.append(absVal)
        minimum = min(absList)
    location = absList.index(minimum)
    return newTET[location]


def TETMajScale(frequency, octaveDivider):
    """Cross references a traditional major scale with a new TET chromatic scale.
    Returns an array of 8 frequencies."""
    TTET = Create12TETChromatic(frequency)
    standard = StandardMajScale(TTET)
    newTET = TETChromaticScale(frequency, octaveDivider)
    print(standard)
    print(newTET)
    newScale = np.array([])
    for i in range(len(standard)):
        freq = SecondLoop(standard[i], newTET)
        newScale = np.append(newScale, freq)
    return newScale

# ----------------------------


a = Create12TETChromatic(220)
b = WriteScale(a, 0.2)
write2wav(b)

#a = TETMajScale(440, 13)
#b = WriteScale(a, 0.2)
#write2wav(b)


