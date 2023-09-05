# ChordsRandomizerApp
Generate chord progressions by randomizing sets of chords and enable users to playback the chord progression using their preferred MIDI instruments.


## Installation

Before running the Chord Generator App, you need to install its dependencies:

1. **Python 3:** If you don't have Python 3 installed, download and install it from the [official Python website](https://www.python.org/downloads/).

2. **PySide6:** Install the PySide6 library using pip:

    ```
    pip install PySide6
    ```

3. **Mido:** Install the Mido library for MIDI communication:

    ```
    pip install mido
    ```

## Usage


1. Clone this repository to your local machine:

    ```
    git clone https://github.com/radio0but/ChordsRandomizerApp.git
    ```

2. Navigate to the project directory:

    ```
    cd ChordsRandomizerApp
    ```

3. Run the Chord Generator App:

    ```
    python chord_generator.py
    ```


4. Use the app to generate chord progressions and play them through your MIDI device.

## Features

- **Generate Chords:** Click the "Generate" button to generate a series of chords based on the selected tonality and number of bars.

- **Play Chords:** Click the "Play" button to play the generated chord progression. Adjust the tempo and repetition settings as needed.

- **Stop Playback:** Click the "Stop" button to stop playback at any time.

- **Select MIDI Device:** Choose your MIDI output device from the dropdown list.

- **Refresh MIDI Devices:** Click the "Refresh MIDI" button to update the list of available MIDI devices.

## Contributing

If you would like to contribute to this project, feel free to open issues or submit pull requests.

---

Happy music composition!
