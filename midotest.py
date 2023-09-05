import mido
from time import sleep

# Initialize the default MIDI output port
port = mido.open_output('FLUID Synth (16157):Synth input port (16157:0) 128:0')

print(mido.get_output_names())
# Define a few notes to test
notes = [60, 62, 64, 65, 67]  # These are MIDI note numbers for C4, D4, E4, F4, G4

for note in notes:
    # Send note_on message for the current note
    port.send(mido.Message('note_on', note=note, velocity=64))

    sleep(0.5)  # Wait for half a second

    # Send note_off message for the current note
    port.send(mido.Message('note_off', note=note, velocity=64))

    sleep(0.5)  # Wait for half a second between notes

# Close the MIDI port
port.close()
