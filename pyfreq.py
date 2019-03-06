import numpy as np
import math
import random 

# Patrick Tumulty 
# March 6, 2019
# Frequency Functions but all the functions as a class

class pyfreq():
    def Create12TETChromatic(self, frequency):
        """creates a 12 tone even tempered scale with any starting pitch. returns an array"""
        i = 0
        scale = np.array([])
        while i < 12:
            i += 1
            note = round(frequency * (2**(i/12)), 2)      # divides octave into 12 even pitches
            scale = np.append(scale, note)      # adds pitches to an array
        scale = np.insert(scale, 0, frequency)  # adds starting pitch to our scale
        return scale

    def TETChromaticScale(self, frequency, octaveDivider):
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
  
    def StandardMajScale(self, frequency):
        """Takes one arguement, frequency. Returns an array of 8 frequencies from 12 TET chromatic scale"""
        EightSteps = np.array([])
        freqArray = pyfreq().Create12TETChromatic(frequency)
        steps = (0, 2, 4, 5, 7, 9, 11, 12)
        for i in steps:
            scale = freqArray[i]
            EightSteps = np.append(EightSteps, scale)
        return EightSteps

    def JustScale(self, frequency):
        """Takes in a frequency. Returns an array of 8 frequencies in the Just scale"""
        EightSteps = []
        ratios = [1, (9/8), (5/4), (4/3), (3/2), (5/3), (15/8), 2]
        for i in range(len(ratios)):
            note = round(frequency * ratios[i],2)
            EightSteps.append(note)
        return EightSteps

    def PythagoreanScale(self, frequency):
        """Takes in a frequency. Returns an array of 8 frequencies in the Pythagorean scale"""
        EightSteps = []
        ratios = [1, (9/8), (81/64), (4/3), (3/2), (27/16), (243/128), 2]
        for i in range(len(ratios)):
            note = round(frequency * ratios[i],2)
            EightSteps.append(note)
        return EightSteps

    def calculateCents(self, referenceScale, newScale):
        """Takes two arrays of frequencies and calculates the cents difference. Returns 8 values in a list."""
        centsList = []
        for i in range(len(referenceScale)):
            ratio = newScale[i] / referenceScale[i]
            cents = round(((math.log(ratio) / math.log(2)) * 1200), 2)
            centsList.append(cents)
        return centsList

    def SecondLoop(self, frequency, newTET):
        """This function is used only in conjunction with TETMajScale()"""
        absList = []
        minimum = 0
        for i in range(len(newTET)):
            absVal = np.round(abs(newTET[i] - frequency))
            absList.append(absVal)
            minimum = min(absList)
        location = absList.index(minimum)
        return newTET[location]


    def TETMajScale(self, frequency, octaveDivider):
        """Cross references a traditional major scale with a new TET chromatic scale.
        Returns an array of 8 frequencies."""
        standard = pyfreq().StandardMajScale(frequency)
        newTET = pyfreq().TETChromaticScale(frequency, octaveDivider)
        newScale = np.array([])
        for i in range(len(standard)):
            freq = pyfreq().SecondLoop(standard[i], newTET)
            newScale = np.append(newScale, freq)
        return newScale

    def genBlock(self, frequencyArray, chordNum):
        """Takes in an 8 value frequency array and a chord number (1-8)
        return frequencies within key"""
        Melody = ["m"] #4 notes played at random over chords, up one octave
        Chord = ["c"] #3 notes root third fifth, inversions keep chords in one octave
        Bass = ["b"] #2 notes down octave 
        SendValues = [] #empty list to append melody, chord, and bass to
        if chordNum == 1:
            mOne = (0, 2, 4, 6)
            cOne = (0, 2, 4)
            bOne = (0, 4)
            for item in mOne:
                note = frequencyArray[item] * 2
                Melody.append(note)
            for item in cOne:
                note = frequencyArray[item]
                Chord.append(note)
            for item in bOne:
                note = frequencyArray[item] / 2
                Bass.append(note)
        if chordNum == 2:
            mTwo = (1, 3, 5, 7)
            cTwo = (1, 3, 5)
            bTwo = (1, 5)
            for item in mTwo:
                note = frequencyArray[item] * 2
                Melody.append(note)
            for item in cTwo:
                note = frequencyArray[item]
                Chord.append(note)
            for item in bTwo:
                note = frequencyArray[item] / 2
                Bass.append(note)
        if chordNum == 3:
            mThree = (2, 4, 6, 1)
            cThree = (2, 4, 6)
            bthree = (2, 6)
            for item in mThree:
                note = frequencyArray[item] * 2
                Melody.append(note)
            for item in cThree:
                note = frequencyArray[item]
                Chord.append(note)
            for item in bthree:
                note = frequencyArray[item] / 2
                Bass.append(note)
        if chordNum == 4:
            mFour = (3, 5, 7, 2)
            cFour = (3, 5, 7)
            bFour = (3, 7)
            for item in mFour:
                note = frequencyArray[item] * 2
                Melody.append(note)
            for item in cFour:
                note = frequencyArray[item]
                Chord.append(note)
            for item in bFour:
                note = frequencyArray[item] / 2
                Bass.append(note)
        if chordNum == 5:
            mFive = (4, 6, 1, 3)
            cFive = (4, 6, 1)
            bFive = (4, 1)
            for item in mFive:
                note = frequencyArray[item] * 2
                Melody.append(note)
            for item in cFive:
                note = frequencyArray[item]
                Chord.append(note)
            for item in bFive:
                note = frequencyArray[item] / 2
                Bass.append(note)
        if chordNum == 6:
            mSix = (5, 7, 2, 4)
            cSix = (5, 7, 2)
            bSix = (5, 2)
            for item in mSix:
                note = frequencyArray[item] * 2
                Melody.append(note)
            for item in cSix:
                note = frequencyArray[item]
                Chord.append(note)
            for item in bSix:
                note = frequencyArray[item] / 2
                Bass.append(note)
        if chordNum == 7:
            mSev = (6, 1, 3, 5)
            cSev = (6, 1, 3)
            bSev = (6, 3)
            for item in mSev:
                note = frequencyArray[item] * 2
                Melody.append(note)
            for item in cSev:
                note = frequencyArray[item]
                Chord.append(note)
            for item in bSev:
                note = frequencyArray[item] / 2
                Bass.append(note)
        if chordNum == 8:
            mOct = (7, 2, 4, 6)
            cOct = (7, 2, 4)
            bOct = (0, 4)
            for item in mOct:
                note = frequencyArray[item] * 2
                Melody.append(note)
            for item in cOct:
                note = frequencyArray[item]
                Chord.append(note)
            for item in bOct:
                note = frequencyArray[item] / 2
                Bass.append(note)
        SendValues.append(Melody)
        SendValues.append(Chord)
        SendValues.append(Bass)
        return SendValues


    def CompAlgorithm(self, frequencyArray):
        loop = 0
        for i in range(8):
            block = pyfreq().genBlock(frequencyArray, (i + 1))
            if i == 0:
                one = block
            if i == 1:
                two = block
            if i == 2:
                three = block
            if i == 3:
                four = block
            if i == 4:
                five = block
            if i == 5:
                six = block
            if i == 6:
                sev = block
            if i == 7:
                octave = block
        while loop < 10: 
            val = random.randint(1, 8)
            if val == 1:
                print(one, "ONE") 
            elif val == 2:
                print(two, "TWO") 
            elif val == 3:
                print(three) 
            elif val == 4:
                print(four) 
            elif val == 5:
                print(five) 
            elif val == 6:
                print(six) 
            elif val == 7:
                print(sev) 
            elif val == 8:
                print(octave) 
            loop += 1

