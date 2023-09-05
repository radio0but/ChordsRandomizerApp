import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton,
                               QGraphicsView, QSpinBox, QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem, QLineEdit, QLabel)
from PySide6.QtCore import Qt, QTimer, QFile
from PySide6.QtUiTools import QUiLoader
import random
import mido
from time import sleep
import data


class ChordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        # Load the UI from the XML
        loader = QUiLoader()
        file = QFile("chord_generator.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()
        # Initialize the timer and connect its timeout signal
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.play_next_step)

        self.port = None

        
        # Additional attributes to help manage the play state
        self.current_chord_index = 0
        self.current_step = 0
        self.beat_duration = 0
        
        # Number of bars selector
        self.bar_selector = self.ui.bar_selector
        self.bar_selector.addItems(['2', '3', '4', '6', '8', '12'])
        self.tempo_selector = self.ui.tempo_selector
        self.tempo_selector.setRange(30, 240)  # Adjust the range if needed
        self.tempo_selector.setValue(120)  # Default to 120 BPM
        self.tempo_selector.setSuffix(" BPM")

        self.tonality_selector = self.ui.tonality_selector
        self.tonality_selector.addItems(['C', 'Cm', 'C7', 'Cm7', 'C9', 'Cm9', 'CMaj7', 'Cdorian', 'Cphrygian',
                                        'D', 'Dm', 'D7', 'Dm7', 'D9', 'Dm9', 'DMaj7', 'Ddorian', 'Dphrygian',
                                        'E', 'Em', 'E7', 'Em7', 'E9', 'Em9', 'EMaj7', 'Edorian', 'Ephrygian',
                                        'F', 'Fm', 'F7', 'Fm7', 'F9', 'Fm9', 'FMaj7', 'Fdorian', 'Fphrygian',
                                        'G', 'Gm', 'G7', 'Gm7', 'G9', 'Gm9', 'GMaj7', 'Gdorian', 'Gphrygian',
                                        'A', 'Am', 'A7', 'Am7', 'A9', 'Am9', 'AMaj7', 'Adorian', 'Aphrygian',
                                        'B', 'Bm', 'B7', 'Bm7', 'B9', 'Bm9', 'BMaj7', 'Bdorian', 'Bphrygian'])
        self.generated_chords = []
        #self.port = mido.open_output()

        # Chord map input
        self.chord_input_label = self.ui.chord_input_label
        self.chord_input_field = self.ui.chord_input_field



        # Generate button
        self.generate_btn = self.ui.generate_btn
        self.generate_btn.clicked.connect(self.generate_chords)
 

        # Play button
        self.play_btn = self.ui.play_btn
        self.play_btn.clicked.connect(self.play_chords)

        # Stop Button
        self.stop_btn = self.ui.stop_btn
        self.stop_btn.clicked.connect(self.stop_chords)


        # Graphics view to display bars and chords
        self.view = self.ui.view
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        # Repetition selector
        self.repetition_selector = self.ui.repetition_selector
        self.repetition_selector.addItems(['2', '3', '4', '5', '6', '7', '8'])

        self.refresh_midi_btn = self.ui.refresh_midi_btn
        self.refresh_midi_btn.clicked.connect(self.update_midi_devices)

        # Use the imported data
        self.chord_to_midi = data.chord_to_midi
        # MIDI port setup
        #self.port = mido.open_output('FLUID Synth (16157):Synth input port (16157:0) 128:0')

        # MIDI Device Selection
        self.midi_device_selector = self.ui.midi_device_selector
        self.update_midi_devices()
        self.midi_device_selector.currentIndexChanged.connect(self.set_midi_device)
        self.set_midi_device()
    

    def generate_chords(self):
        self.scene.clear()  # Clear previous bars
        self.generated_chords.clear()
        self.bar_rectangles = []  # List to store the rectangles for each chord

        num_bars = int(self.bar_selector.currentText())
        tonality = self.tonality_selector.currentText()

        # Fetch chords based on the selected tonality
        chords = self.get_chords_for_tonality(tonality)

        bar_width = 80
        bar_height = 40
        spacing = 10

        for i in range(num_bars):
            # Randomly choose chords
            chord = random.choice(chords)
            self.generated_chords.append(chord)

            # Create rectangle representing a bar/chord
            bar = QGraphicsRectItem(i * (bar_width + spacing), 0, bar_width, bar_height)
            self.scene.addItem(bar)
            bar.setBrush(Qt.gray)  # Default color
            self.bar_rectangles.append(bar)

            chord_text = QGraphicsTextItem(chord)
            chord_text.setPos(i * (bar_width + spacing) + 10, 10)
            self.scene.addItem(chord_text)
    def play_chords(self):
        self.beat_duration = 60 / self.tempo_selector.value()
        self.current_chord_index = 0
        self.current_step = 0
        repetitions = int(self.repetition_selector.currentText())
        self.total_steps = repetitions * 2  # times 2 because each chord is played and then stopped
        self.timer.start(self.beat_duration * 1000)  # Adjust the beat duration directly

    def play_next_step(self):
        if self.current_chord_index < len(self.generated_chords):
            chord = self.generated_chords[self.current_chord_index]
            notes = self.chord_to_midi[chord]

            # Play chord on even steps, stop on odd steps
            if self.current_step % 2 == 0:
                for note in notes:
                    self.port.send(mido.Message('note_on', note=note, velocity=64))
                self.bar_rectangles[self.current_chord_index].setBrush(Qt.red)
            else:
                for note in notes:
                    self.port.send(mido.Message('note_off', note=note, velocity=64))
                if self.current_step == self.total_steps - 1:
                    self.bar_rectangles[self.current_chord_index].setBrush(Qt.gray)
                    self.current_chord_index += 1

            self.current_step += 1
            if self.current_step >= self.total_steps:
                self.current_step = 0
        else:
            #self.timer.stop()
            self.current_chord_index = 0
            self.play_next_step()  # Remove the delay by directly calling the method again
    def get_chords_for_tonality(self, tonality):
        user_input_chords = self.chord_input_field.text().split(',')
        return data.get_chords_for_tonality(tonality, user_input_chords)

    def stop_chords(self):
        self.timer.stop()  # Stop the timer
        for bar_rect in self.bar_rectangles:
            bar_rect.setBrush(Qt.gray)  # Reset all bars to gray
        # Turn off any remaining notes that might be playing
        for chord in self.generated_chords:
            for note in self.chord_to_midi[chord]:
                self.port.send(mido.Message('note_off', note=note, velocity=64))
        self.current_chord_index = 0
        self.current_step = 0   
    def update_midi_devices(self):
        current_device = self.midi_device_selector.currentText()
        available_devices = mido.get_output_names()  # Get all available output MIDI devices
        self.midi_device_selector.clear()  # Clear current items
        self.midi_device_selector.addItems(available_devices)  # Populate the dropdown with detected MIDI devices
        # If the previously selected device is still available, set it as the current item.
        index = self.midi_device_selector.findText(current_device)
        if index != -1:
            self.midi_device_selector.setCurrentIndex(index)


    def set_midi_device(self):
        selected_device = self.midi_device_selector.currentText()
        if selected_device in mido.get_output_names():
            self.port = mido.open_output(selected_device)
        else:
            # If the selected device is not available, close the current port and show a warning or error message.
            if self.port:
                self.port.close()
            self.port = None
            # Optionally show an error message to the user.
            print(f"Selected MIDI device '{selected_device}' is not available.")

    

if __name__ == "__main__":
    app = QApplication([])
    window = ChordGenerator()
    window.show()
    sys.exit(app.exec_())
