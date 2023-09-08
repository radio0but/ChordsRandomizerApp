import sys
import json
import mido
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QPushButton, QFileDialog,
                               QGraphicsView, QGraphicsScene, QGraphicsRectItem, QLabel, QSpinBox,
                               QComboBox, QTextEdit, QWidget, QMenu, QGraphicsTextItem)
from PySide6.QtGui import QBrush, QColor, QAction
from PySide6.QtCore import Qt, QTimer
from data import chord_to_midi
import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile


class PlaybackManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.current_chord_index = 0
        self.mid = None
        self.timer = QTimer(main_window)
        self.timer.timeout.connect(self.play_chord)
        self.looping = False  # By default, looping is off

    def test_midi(self):
        if not self.mid:
            self.mid = mido.open_output(self.main_window.combo_device.currentText())
        msg = mido.Message('note_on', note=60)  # Middle C
        self.mid.send(msg)
        QTimer.singleShot(1000, self.stop_test_midi)

    def stop_test_midi(self):
        msg = mido.Message('note_off', note=60)  # Middle C
        self.mid.send(msg)
    def load_midi_devices(self):
        self.main_window.combo_device.clear()
        for name in mido.get_output_names():
            self.main_window.combo_device.addItem(name)

    def play_chord(self):
        self.stop_chord()  # Stop the previous chord
        
        if not self.mid:
            self.mid = mido.open_output(self.main_window.combo_device.currentText())

        bar_length = int(self.main_window.combo_bar_length.currentText())
        rhythms = {
            "Straight": [0.5, 0.5],   # A straight beat for reference
            "OffBeat1": [0.75, 0.25], # First off-beat syncopation
            "OffBeat2": [0.25, 0.75], # Second off-beat syncopation
            "TripleSync": [0.33, 0.66], # Triplet syncopation
            "DottedSync": [0.375, 0.125, 0.5], # Dotted eight syncopation
            "QuickStart": [0.125, 0.375, 0.5], # Quick start syncopation
            "DoubleOff": [0.25, 0.5, 0.25], # Double off-beat syncopation
            "RestStart": [0.25, 0.75],  # Start with a rest (or silence)
            "RestMid": [0.5, 0.25, 0.25], # Rest in the middle
            "SyncCombo": [0.25, 0.375, 0.125, 0.25], # Combination of syncopations

            "QuadrupleSync": [0.2, 0.2, 0.2, 0.4],
            "Staggered": [0.3, 0.1, 0.6],
            "Gallop": [0.125, 0.125, 0.75],
            "DoubleGallop": [0.125, 0.125, 0.125, 0.625],
            "Triplets": [0.333, 0.333, 0.334],
            "Swing": [0.666, 0.334],
            "Shuffle": [0.5, 0.25, 0.25],
            "DottedShuffle": [0.375, 0.125, 0.5],
            "BossaNova": [0.375, 0.125, 0.25, 0.25],
            "AfroCuban": [0.25, 0.25, 0.5]

        }

        rhythm_name = self.main_window.chords_rhythms[self.current_chord_index]
        current_rhythm = rhythms[rhythm_name]
        bar_rhythm = current_rhythm * bar_length  # Repeat the rhythm pattern until it fills the bar length

        if hasattr(self, 'rhythm_counter'):
            self.rhythm_counter += 1
        else:
            self.rhythm_counter = 0

        if self.rhythm_counter >= bar_length:
            self.rhythm_counter = 0
            self.current_chord_index += 1  # Move to the next chord
            if self.current_chord_index >= len(self.main_window.chord_rects):  # All chords played
                if self.looping:
                    self.current_chord_index = 0  # Reset to start for looping
                else:
                    self.stop_playback()
                    return



        rect = self.main_window.chord_rects[self.current_chord_index]
        chord_name = rect.toolTip()
        midi_notes = chord_to_midi.get(chord_name, [])
        
        for note in midi_notes:
            msg = mido.Message('note_on', note=note)
            self.mid.send(msg)

        rect.setBrush(QBrush(QColor("red")))

        # Limit to the total bar length in case of an incomplete bar
        bar_rhythm = bar_rhythm[:bar_length]

        rhythm_index = self.rhythm_counter % len(bar_rhythm)
        delay = bar_rhythm[rhythm_index] * 60.0 / self.main_window.spinbox_tempo.value()
        
        QTimer.singleShot(int(delay * 1000), self.stop_chord)  # Stop the chord after the delay
        QTimer.singleShot(int(delay * 1000), self.play_chord)  # Play next chord after the delay
        self.timer.start(int(delay * 1000))


    def stop_chord(self):
        # Check if there's any previously played chord
        if self.current_chord_index == 0:  # No chord has been played yet
            return
        
        prev_chord_index = self.current_chord_index - 1
        if prev_chord_index < len(self.main_window.chord_rects):
            rect = self.main_window.chord_rects[prev_chord_index]
            chord_name = rect.toolTip()
            midi_notes = chord_to_midi.get(chord_name, [])
            
            for note in midi_notes:
                msg = mido.Message('note_off', note=note)
                self.mid.send(msg)

            rect.setBrush(QBrush(QColor("blue")))
    def start_playback(self):
        self.current_chord_index = 0
        self.play_chord()

    def stop_playback(self):
        self.timer.stop()
        self.current_chord_index = 0
        self.looping = False  # Turn off looping when stopping playback
        for rect in self.main_window.chord_rects:
            rect.setBrush(QBrush(QColor("blue")))


class CustomRect(QGraphicsRectItem):
    def __init__(self, x, y, width, height, callback, extra_info=None):
        super().__init__(x, y, width, height)
        self.context_callback = callback
        self.extra_info = extra_info if extra_info else {}

    def contextMenuEvent(self, event):
        self.context_callback(event, self)


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        file = QFile("chord_prog_syncopator.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file)
        file.close()
        self.scene = QGraphicsScene(self)
        
        # Assign Widgets to Class Attributes
        self.btn_test = self.ui.findChild(QtWidgets.QPushButton, 'btn_test')
        self.label_tonality = self.ui.findChild(QtWidgets.QLabel, 'label_tonality')
        self.text_area = self.ui.findChild(QtWidgets.QTextEdit, 'text_area')
        self.combo_device = self.ui.findChild(QtWidgets.QComboBox, 'combo_device')
        self.btn_refresh = self.ui.findChild(QtWidgets.QPushButton, 'btn_refresh')
        self.spinbox_tempo = self.ui.findChild(QtWidgets.QSpinBox, 'spinbox_tempo')
        self.combo_bar_length = self.ui.findChild(QtWidgets.QComboBox, 'combo_bar_length')
        self.graphicsView = self.ui.findChild(QtWidgets.QGraphicsView, 'graphicsView')
        self.btn_open = self.ui.findChild(QtWidgets.QPushButton, 'btn_open')
        self.btn_play = self.ui.findChild(QtWidgets.QPushButton, 'btn_play')
        self.btn_stop = self.ui.findChild(QtWidgets.QPushButton, 'btn_stop')
        self.btn_loop = self.ui.findChild(QtWidgets.QPushButton, 'btn_loop')

        # Initialize other variables
        self.current_chord_index = 0
        self.mid = None
        self.timer = QtCore.QTimer(self)
        self.playback_manager = PlaybackManager(self)
        self.chord_rects = []
        self.chords_rhythms = []
        self.rhythm_texts = []

        # Set the UI as central widget
        self.setCentralWidget(self.ui)

        # Connect signals to methods (you'll need to implement or adapt these methods)
        self.btn_test.clicked.connect(self.test_midi)
        self.btn_refresh.clicked.connect(self.load_midi_devices)
        self.btn_open.clicked.connect(self.on_open)
        self.btn_play.clicked.connect(self.start_playback)
        self.btn_stop.clicked.connect(self.stop_playback)
        self.btn_loop.clicked.connect(self.toggle_looping)

        self.initUI()

    def initUI(self):

        self.graphicsView.setScene(self.scene)
        self.load_midi_devices() # Initial load of MIDI devices
        self.spinbox_tempo.setRange(10, 480)
        self.spinbox_tempo.setValue(120)
        self.combo_bar_length.addItems(['2', '3', '4', '5', '6', '7', '8', '9', '12'])
        self.combo_bar_length.setCurrentText('4')

    def on_open(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open .chordprog File", "", "ChordProg Files (*.chordprog);;All Files (*)")
        if file_path:
            self.open_chordprog(file_path)

    def open_chordprog(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)

        self.label_tonality.setText(data['tonality'])
        self.text_area.setText(data['notes'])

        x = 0
        y = 0
        width = 150
        height = 50
        self.chord_rects = []
        for chord in data['chords']:
            rect = CustomRect(x, y, width, height, self.context_menu_event, {"example_key": "example_value"}) # add additional data as needed
            rect.setBrush(QBrush(QColor("blue")))
            rect.setToolTip(chord)
            rect.setFlag(QGraphicsRectItem.ItemIsSelectable)
            rect.setAcceptHoverEvents(True)
            rect.setAcceptedMouseButtons(Qt.RightButton)
            self.scene.addItem(rect)
            self.chord_rects.append(rect)
            # Display the chord name
            chord_text = QGraphicsTextItem(chord)
            chord_text.setPos(x + (width - chord_text.boundingRect().width()) / 2, y)
            self.scene.addItem(chord_text)

            # Display the rhythm name beneath the chord name
            rhythm_text = QGraphicsTextItem("Straight")  # Default rhythm is Straight
            rhythm_text.setPos(x + (width - rhythm_text.boundingRect().width()) / 2, y + height - rhythm_text.boundingRect().height())
            self.scene.addItem(rhythm_text)
            self.rhythm_texts.append(rhythm_text)  # Store rhythm text for updating later

            x += width + 10

        self.chords_rhythms = ["Straight" for _ in data['chords']]

    def set_rhythm(self, rhythm, item):
        index = self.chord_rects.index(item)
        self.chords_rhythms[index] = rhythm

        # Update the displayed rhythm text when rhythm is changed
        rhythm_text_item = self.rhythm_texts[index]
        rhythm_text_item.setPlainText(rhythm)

    def context_menu_event(self, event, item):
        contextMenu = QMenu(self)
        rhythms = [
    "Straight", "OffBeat1", "OffBeat2", "TripleSync", 
    "DottedSync", "QuickStart", "DoubleOff", "RestStart", 
    "RestMid", "SyncCombo", "QuadrupleSync", "Staggered", 
    "Gallop", "DoubleGallop", "Triplets", "Swing", 
    "Shuffle", "DottedShuffle", "BossaNova", "AfroCuban"
]
        for rhythm in rhythms:
            action = QAction(rhythm, self)
            action.triggered.connect(lambda r=rhythm, i=item: self.set_rhythm(r, i))
            contextMenu.addAction(action)
        contextMenu.exec_(event.screenPos())

    def test_midi(self):
        self.playback_manager.test_midi()
    def load_midi_devices(self):
        self.playback_manager.load_midi_devices()
    def start_playback(self):
        self.playback_manager.start_playback()
    def stop_playback(self):
        self.playback_manager.stop_playback()
        self.btn_loop.setText("Toggle Looping")  # Reflect that looping has been turned off
    def set_rhythm_for_chord(self, rhythm, rect):
        index = self.chord_rects.index(rect)
        self.chords_rhythms[index] = rhythm
    def toggle_looping(self):
        self.playback_manager.looping = not self.playback_manager.looping  # Toggle the looping status
        if self.playback_manager.looping:
            self.btn_loop.setText("Looping ON")
        else:
            self.btn_loop.setText("Toggle Looping")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = Main()
    mainWin.show()
    sys.exit(app.exec())