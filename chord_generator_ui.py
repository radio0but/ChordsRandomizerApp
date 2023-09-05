# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chord_generator.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_ChordGenerator(object):
    def setupUi(self, ChordGenerator):
        if not ChordGenerator.objectName():
            ChordGenerator.setObjectName(u"ChordGenerator")
        ChordGenerator.resize(1124, 728)
        self.layout = QVBoxLayout(ChordGenerator)
        self.layout.setObjectName(u"layout")
        self.label_4 = QLabel(ChordGenerator)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Noto Sans Black"])
        font.setPointSize(22)
        font.setBold(True)
        self.label_4.setFont(font)

        self.layout.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 0, 10)
        self.label_6 = QLabel(ChordGenerator)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans Black"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_6.setFont(font1)

        self.verticalLayout.addWidget(self.label_6)

        self.label_2 = QLabel(ChordGenerator)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.bar_selector = QComboBox(ChordGenerator)
        self.bar_selector.setObjectName(u"bar_selector")

        self.verticalLayout.addWidget(self.bar_selector)

        self.label_3 = QLabel(ChordGenerator)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.tonality_selector = QComboBox(ChordGenerator)
        self.tonality_selector.setObjectName(u"tonality_selector")

        self.verticalLayout.addWidget(self.tonality_selector)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.chord_input_label = QLabel(ChordGenerator)
        self.chord_input_label.setObjectName(u"chord_input_label")

        self.hboxLayout.addWidget(self.chord_input_label)

        self.chord_input_field = QLineEdit(ChordGenerator)
        self.chord_input_field.setObjectName(u"chord_input_field")

        self.hboxLayout.addWidget(self.chord_input_field)


        self.verticalLayout.addLayout(self.hboxLayout)

        self.generate_btn = QPushButton(ChordGenerator)
        self.generate_btn.setObjectName(u"generate_btn")

        self.verticalLayout.addWidget(self.generate_btn)

        self.label_5 = QLabel(ChordGenerator)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u"boogie.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setMargin(10)

        self.verticalLayout.addWidget(self.label_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label_7 = QLabel(ChordGenerator)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.play_btn = QPushButton(ChordGenerator)
        self.play_btn.setObjectName(u"play_btn")

        self.horizontalLayout.addWidget(self.play_btn)

        self.stop_btn = QPushButton(ChordGenerator)
        self.stop_btn.setObjectName(u"stop_btn")

        self.horizontalLayout.addWidget(self.stop_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(ChordGenerator)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.tempo_selector = QSpinBox(ChordGenerator)
        self.tempo_selector.setObjectName(u"tempo_selector")

        self.verticalLayout_5.addWidget(self.tempo_selector)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.repetition_label = QLabel(ChordGenerator)
        self.repetition_label.setObjectName(u"repetition_label")

        self.verticalLayout_3.addWidget(self.repetition_label)

        self.repetition_selector = QComboBox(ChordGenerator)
        self.repetition_selector.setObjectName(u"repetition_selector")

        self.verticalLayout_3.addWidget(self.repetition_selector)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(ChordGenerator)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.refresh_midi_btn = QPushButton(ChordGenerator)
        self.refresh_midi_btn.setObjectName(u"refresh_midi_btn")

        self.horizontalLayout_4.addWidget(self.refresh_midi_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.midi_device_selector = QComboBox(ChordGenerator)
        self.midi_device_selector.setObjectName(u"midi_device_selector")

        self.verticalLayout_2.addWidget(self.midi_device_selector)

        self.view = QGraphicsView(ChordGenerator)
        self.view.setObjectName(u"view")
        self.view.setMinimumSize(QSize(700, 0))
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        self.view.setBackgroundBrush(brush)

        self.verticalLayout_2.addWidget(self.view)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.layout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(ChordGenerator)

        QMetaObject.connectSlotsByName(ChordGenerator)
    # setupUi

    def retranslateUi(self, ChordGenerator):
        ChordGenerator.setWindowTitle(QCoreApplication.translate("ChordGenerator", u"Chord Generator", None))
        self.label_4.setText(QCoreApplication.translate("ChordGenerator", u" Uldarik's Chord Progression Generator", None))
        self.label_6.setText(QCoreApplication.translate("ChordGenerator", u"Chords Randomizer", None))
        self.label_2.setText(QCoreApplication.translate("ChordGenerator", u"Select Numer of Bar", None))
        self.label_3.setText(QCoreApplication.translate("ChordGenerator", u"Select Tonality or enter chords for Custom Tonality", None))
        self.chord_input_label.setText(QCoreApplication.translate("ChordGenerator", u"Enter Chords (comma separated):", None))
        self.generate_btn.setText(QCoreApplication.translate("ChordGenerator", u"Generate Chords", None))
        self.label_5.setText("")
        self.label_7.setText(QCoreApplication.translate("ChordGenerator", u"Playback", None))
        self.play_btn.setText(QCoreApplication.translate("ChordGenerator", u"Play Chords", None))
        self.stop_btn.setText(QCoreApplication.translate("ChordGenerator", u"Stop Playback", None))
        self.label.setText(QCoreApplication.translate("ChordGenerator", u"Select Tempo", None))
        self.repetition_label.setText(QCoreApplication.translate("ChordGenerator", u"Repetitions per Bar:", None))
        self.label_8.setText(QCoreApplication.translate("ChordGenerator", u"Chose Midi Instrument/Port", None))
        self.refresh_midi_btn.setText(QCoreApplication.translate("ChordGenerator", u"Refresh Devices List", None))
    # retranslateUi

