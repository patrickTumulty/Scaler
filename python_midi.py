import mido 
import data_files as df

midi_device = 'MPKmini2'
# midi_device = 'CASIO USB-MIDI'


def open_midi_stream(filename, midi_device):
    msg = mido.Message('note_on', note=60)
    freq_scale = df.extend_scale(filename)
    with mido.open_input(midi_device) as inport:
        for msg in inport:
            if msg.note == 49: # 49 is C#3 which will end the stream
                break
            elif msg.note == 48:
                print(freq_scale[0])
            elif msg.note == 50:
                print(freq_scale[1])
            elif msg.note == 52:
                print(freq_scale[2])
            elif msg.note == 53:
                print(freq_scale[3])
            elif msg.note == 55:
                print(freq_scale[4])
            elif msg.note == 57:
                print(freq_scale[5])
            elif msg.note == 59:
                print(freq_scale[6])
            elif msg.note == 60:
                print(freq_scale[7])
            elif msg.note == 62:
                print(freq_scale[8])
            elif msg.note == 64:
                print(freq_scale[9])
            elif msg.note == 65:
                print(freq_scale[10])
            elif msg.note == 67:
                print(freq_scale[11])
            elif msg.note == 69:
                print(freq_scale[12])
            elif msg.note == 71:
                print(freq_scale[13])
            elif msg.note == 72:
                print(freq_scale[14])
            print(msg.note)

