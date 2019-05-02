# TheSonicExperience

About:
--------------------------------------------

This program is designed to allow a user to quickly calculate and sonify different types of scales. 

The left column will always calculate a 12 Tone Equal Temperment (12TET) scale. The cents calculation on the far
left will always be comparing the novel scale to that of a 12TET scale. The center column is where the novel 
scale will be displayed.

The Scales:
--------------------------------------------

TET:

Choosing "TET" will calculate a new scale in the same way that a 12TET scale is created. 

f(n) = f * 2^n/12

The difference is that it allows the user to input any number of octave subdivision that they would like.
The program will compare the newly created TET scale with that of a 12TET major scale and will select eight 
tones that best fit that of a 12TET. This is why regardless of how many subdivision are chosen, 
the program will only display 8 tones. 
Note: Choosing an octave divider that is a whole number multiple of 12 will yield a standard 12TET scale. 

Just:

The "Just" scale (Sometimes referred to as the Pure Tone Scale) is a scale that is based off of the 
small whole number ratios of the harmonic series. Those ratios are [1, (9/8), (5/4), (4/3), (3/2), (5/3), (15/8), 2].

Pythagorean:

The "Pythagorean" scale is created with the idea of using the most harmonious interval 3/2 (second 
most harmonious, the first being the octave) to generate a scale. The eight tones are realized by starting at a 
pitch and going up a fifth(3/2) or doing down a fourth (4/3). Using the fourth doesn't break the rules of only using
3/2 because a fourth is simply an inverted fifth. 

Ratio:

The "Ratio" option is less musical and more proof of concept. Just like how the Pythagorean scale is
created from a generator interval of 3/2. The ratio option allows you to compose a scale that is generated from 
other small whole number ratios of the harmonic series. 


Sound Setup:
--------------------------------------------
Step One:

Download SuperCollider at the following link. 

https://supercollider.github.io/download

Now you will be able to open up the following file. 

OSCRecieve.sc

Once opened, follow the instructions to set up the synth def. 

Step Two:

In the top hand corner select

File > Midi Config

Once in this window select your midi device form the drop down menu
and enter in your IP Address. Once completed click and save and then exit the window. 
You should notice now in the bottom bar your midi device and IP Address. 

Step Three:

Click on the CONFIG button to step up your OSC Client. 

At this point you should already have a scale selected. 

Next select either 12 TET or New Scale (This will change which scale is being sonified)

You should notice now that the 8 roman numeral buttons are no longer greyed out. Assuming 
that your SuperCollider server has been instantiated you can now select the 8 roman numeral 
buttons to begin hearing the chords 1 - 8 of your scale. You can change between 12TET or 
New Scale at anytime to compare the difference. 
(Note: Changing from 12TET to New Scale wont take effect until you select a new chord or the same chord again)

Start Midi
--------------------------------------------

The START MIDI button works after the steps listed above have already been completed.

Once selected, you can now start to play your midi keyboard in the scale that you have
designated (Note: This will be monophonic). Regardless of the scale, the 8 frequencies 
displayed in your list will map to all the white keys from C3 to C5. 
C3 will be set to the frequency that you entered above to generate your scale.

The black keys are used to control what chords are being played. From D#3 to G#4 you can use 
the black keys to change between the different chords of the scale. (Note: The black keys in this range
performs the same function as the eight chord buttons in the main program. Assigning
them to the black keys has simply made them accessible
during real time midi playback). To silence the chords simply press A#4.  

You will note that after you engage START MIDI, the program will be unresponsive. To end midi playback 
and return to the main program you must hit C#3 on your midi keyboard. To resume midi playback simply press the 
START MIDI button again. Repeat this process to change between scales.  

Dependencies:
--------------------------------------------

pythonosc

SuperCollider

Python 3

Tkinter

Mido

