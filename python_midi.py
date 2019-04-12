import mido 
import data_files as df
from pythonosc import udp_client

# midi_device = 'MPKmini2'
# midi_device = 'CASIO USB-MIDI'


def open_midi_stream(filename, midi_device):
    msg = mido.Message('note_on', note=60)
    freq_scale = df.extend_scale(filename)
    client = udp_client.SimpleUDPClient("172.30.98.2", 57120)
    with mido.open_input("MPKmini2") as inport:
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
            print(msg.type)

