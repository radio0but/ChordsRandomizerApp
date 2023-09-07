import sys
import json
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QMimeData, QTimer, Slot  # Add Slot to the import
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QTextEdit, QLabel, QFileDialog, QListWidget, QMenu, QListWidgetItem, QComboBox
from PySide6.QtGui import QDrag, QPixmap, QAction
from data import chord_to_midi
import mido


class ChordLabel(QLabel):
    def __init__(self, chord, parent=None):
        super().__init__(chord, parent)
        self.chord = chord
        self.parent_editor = parent
        self.setAlignment(Qt.AlignCenter)
        self.setFrameShape(QLabel.Box)
        self.setAcceptDrops(True)
        self.drag_start_position = None

    def mousePressEvent(self, event):
        self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if self.drag_start_position is not None:
            drag = QDrag(self)
            mime_data = QMimeData()
            mime_data.setText(self.chord)
            drag.setMimeData(mime_data)
            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos() - self.rect().topLeft())
            drag.exec_()

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        dropped_chord = event.mimeData().text()
        source_label = event.source()

        if source_label != self:
            source_chord = source_label.chord
            # Update the chord progression data
            self.parent_editor.chordprog_data["chords"].remove(source_chord)
            index = self.parent_editor.gridLayout.indexOf(self)
            self.parent_editor.chordprog_data["chords"].insert(index, source_chord)

            # Rearrange the labels in the grid
            self.parent_editor.update_ui()

            event.acceptProposedAction()


    def contextMenuEvent(self, event):
        menu = QMenu(self)
        action_delete = QAction("Delete", self)
        action_delete.triggered.connect(lambda: self.parent_editor.remove_chord(self.chord))
        menu.addAction(action_delete)
        menu.exec_(event.globalPos())

class ChordProgEditor(QMainWindow):
    def __init__(self, ui_file):
        super().__init__()

        self.setWindowTitle("ChordProg Editor")
        self.setGeometry(100, 100, 800, 600)

        # Load the UI from the .ui file
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        self.setCentralWidget(self.ui)
        # Connect the MIDI device combo box (Add this line)
        self.ui.midi_device_combo.currentIndexChanged.connect(self.select_midi_device)
        self.playback_active = False
        # Initialize MIDI (Add these lines)
        self.midi_out = None
        self.midi_devices = []
        self.populate_midi_devices()

        # Initialize a variable to keep track of the current chord
        self.current_chord_index = 0

        # Connect signals and slots as needed
        self.ui.load_button.clicked.connect(self.load_chordprog)
        self.ui.save_button.clicked.connect(self.save_chordprog)
        self.ui.newButton.clicked.connect(self.new_chordprog)
        # Initialize data
        self.chordprog_data = {
            "tonality": "C",
            "chords": [],
            "notes": "Here you can Load, Save, Create .chordprog file for the Chord Prog Generator \n\nTo make a new file delete this text\n\nDouble Clic on the desired chords in the chord chooser to add them to the canva\n\nThen You can drag the Chord box to the desired position\n\nSave your file then you ll be able to open it with the Chord Prog Generator to listen to the result"
        }
        # Connect signals and slots for tempo selection
        self.ui.tempo_spinbox.valueChanged.connect(self.update_tempo)
        self.ui.tempo_spinbox.setSuffix(" BPM")
        self.ui.tempo_spinbox.setRange(1, 240)  # Set the tempo range
        self.ui.tempo_spinbox.setValue(88)  # Set the default tempo value to 88 BPM

        #self.load_chordprog()
        # Connect the grid from the .ui file
        self.gridLayout = self.ui.gridLayout  # Update this line
        self.update_ui()
        self.populate_chord_list()

        # Connect signals and slots for playback buttons
        self.ui.start_button.clicked.connect(self.start_playback)
        self.ui.stop_button.clicked.connect(self.stop_playback)

        # Initialize MIDI
        self.midi_out = None
        self.midi_devices = []
        self.populate_midi_devices()
    
    def update_tempo(self, tempo):
        self.tempo = tempo
        # You can update your timer or any other tempo-dependent functionality here


    def populate_midi_devices(self):
        self.ui.midi_device_combo.clear()
        self.midi_devices = mido.get_output_names()
        self.ui.midi_device_combo.addItems(self.midi_devices)

    def start_playback(self):
        if not self.midi_out or self.playback_active:
            return

        # Set the playback active flag
        self.playback_active = True

        # Calculate delay based on the tempo
        tempo = self.ui.tempo_spinbox.value()
        delay = 60000 / tempo  # Calculate delay in milliseconds

        # Construct MIDI messages and send them in a loop
        chords = self.chordprog_data["chords"]
        self.playback_timer = QTimer(self)
        self.playback_timer.timeout.connect(self.send_midi_chords)
        self.playback_timer.start(delay)
        self.current_chord_index = 0



    def send_midi_chords(self):
        if not self.midi_out:
            return

        # Check if there was a previous chord, and send "note_off" messages
        if self.current_chord_index > 0:
            prev_chord = self.chordprog_data["chords"][self.current_chord_index - 1]
            prev_midi_notes = chord_to_midi.get(prev_chord)
            if prev_midi_notes:
                self.midi_out.send(mido.Message('note_off', note=prev_midi_notes[0]))
                self.midi_out.send(mido.Message('note_off', note=prev_midi_notes[1]))
                self.midi_out.send(mido.Message('note_off', note=prev_midi_notes[2]))

        # Send "note_on" messages for the current chord
        chord = self.chordprog_data["chords"][self.current_chord_index]
        midi_notes = chord_to_midi.get(chord)
        if midi_notes:
            self.midi_out.send(mido.Message('note_on', note=midi_notes[0], velocity=64))
            self.midi_out.send(mido.Message('note_on', note=midi_notes[1], velocity=64))
            self.midi_out.send(mido.Message('note_on', note=midi_notes[2], velocity=64))

        # Increment the current chord index
        self.current_chord_index += 1

        # Check if we've reached the end of the chords, and reset to the beginning
        if self.current_chord_index >= len(self.chordprog_data["chords"]):
            self.current_chord_index = 0
    @Slot(int)
    def select_midi_device(self, index):
        # Close and reset the MIDI output if it exists
        if self.midi_out:
            self.stop_playback()
        
        if index < len(self.midi_devices):
            device_name = self.midi_devices[index]
            try:
                self.midi_out = mido.open_output(device_name)
            except Exception as e:
                print(f"Error opening MIDI output: {str(e)}")


    def stop_playback(self):
        if self.midi_out:
            # Reset the playback active flag
            self.playback_active = False

            # Reset the timer and current chord index
            if hasattr(self, 'playback_timer'):
                self.playback_timer.stop()
            self.current_chord_index = 0

            # Send "note_off" messages for all chords
            for chord in self.chordprog_data["chords"]:
                midi_notes = chord_to_midi.get(chord)
                if midi_notes:
                    self.midi_out.send(mido.Message('note_off', note=midi_notes[0]))
                    self.midi_out.send(mido.Message('note_off', note=midi_notes[1]))
                    self.midi_out.send(mido.Message('note_off', note=midi_notes[2]))


    def populate_chord_list(self):
        # Clear the existing items
        self.ui.chord_list.clear()

        # Add chord items to the list
        for chord in chord_to_midi.keys():
            item = QListWidgetItem(chord)
            self.ui.chord_list.addItem(item)

        # Connect double-click event
        self.ui.chord_list.itemDoubleClicked.connect(self.add_chord_to_progression)

    def add_chord_to_progression(self, item=None):
        chord = item.text() if item else self.sender().text()
        self.chordprog_data["chords"].append(chord)
        self.update_ui()

    def new_chordprog(self):
        # Create a new chordprog with default values
        self.chordprog_data = {
            "tonality": "C",
            "chords": [],
            "notes": ""
        }
        self.update_ui()    

    def remove_chord(self, chord):
        self.chordprog_data["chords"].remove(chord)
        self.update_ui()

    def load_chordprog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Open .chordprog file", "", "ChordProg Files (*.chordprog);;All Files (*)", options=options)

        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.chordprog_data = json.load(file)
                self.update_ui()
            except Exception as e:
                print(f"Error loading .chordprog file: {str(e)}")

    def save_chordprog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getSaveFileName(self, "Save .chordprog file", "", "ChordProg Files (*.chordprog);;All Files (*)", options=options)

        if file_path:
            if not file_path.endswith(".chordprog"):
                file_path += ".chordprog"
            try:
                # Update notes data from the text area
                self.chordprog_data["notes"] = self.ui.notes_text.toPlainText()

                with open(file_path, "w") as file:
                    json.dump(self.chordprog_data, file, indent=4)
            except Exception as e:
                print(f"Error saving .chordprog file: {str(e)}")


    def update_ui(self):
        # Clear the existing grid
        for i in reversed(range(self.ui.gridLayout.count())):
            widget = self.ui.gridLayout.itemAt(i).widget()
            self.ui.gridLayout.removeWidget(widget)
            widget.deleteLater()

        # Add chord labels to the grid
        for i, chord in enumerate(self.chordprog_data["chords"]):
            label = ChordLabel(chord, self)
            self.ui.gridLayout.addWidget(label, 0, i)

        # Set the notes text
        self.ui.notes_text.setPlainText(self.chordprog_data["notes"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChordProgEditor("ChordProgEditor.ui")  # Load the UI file here
    window.show()
    sys.exit(app.exec_())