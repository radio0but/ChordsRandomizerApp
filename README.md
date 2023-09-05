# ChordsRandomizerApp
Generate chord progressions by randomizing sets of chords and enable users to playback the chord progression using their preferred MIDI instruments.


In this examble i use Yoshimi Synth as MIDI instrument

[![Watch the video](https://img.youtube.com/vi/3yXnuPFXqrU/hqdefault.jpg)](https://youtu.be/3yXnuPFXqrU)

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

## Chord Naming Guide

This guide provides a nomenclature for naming chords. You have to use this format if you want to use your own chords collection within the app.

### Basic Format

Chords are named in the format "RootNote" followed by any modifiers.

- **Root Note:** Start with the root note of the chord, which can be one of the following:

  - C, C#, Db, D, D#, Eb, E, F, F#, Gb, G, G#, Ab, A, A#, Bb, B

- **Chord Type:** Use the following modifiers to specify the chord type:

  - If it's a major chord, use just the root note (e.g., C).
  - For minor chords, add 'm' after the root note (e.g., Dm).
  - For diminished chords, add 'dim' after the root note (e.g., F#dim).
  - For augmented chords, add 'aug' after the root note (e.g., Aaug).

### Seventh (7th) Chords

- To indicate a dominant 7th chord, add '7' after the chord type (e.g., G7).
- For major 7th chords, add 'Maj7' after the chord type (e.g., CMaj7).
- For minor 7th chords, add 'm7' after the chord type (e.g., F#m7).
- For minor 7th flat five (half-diminished) chords, add 'm7b5' after the chord type (e.g., Cm7b5).

### Extensions

- For chords with extensions (9th, 11th), add the number after the chord type (e.g., D9, G11).
- For minor 9th chords, add 'm9' after the chord type (e.g., A#m9).
- For minor 11th chords, add 'm11' after the chord type (e.g., Bm11).
- For major 9th chords, add 'Maj9' after the chord type (e.g., EMaj9).

### Flat 5

- For chords with a flat 5, add 'b5' after the chord type (e.g., Cm7b5).

### Diminished 7th Chords

- To indicate a diminished 7th chord, add '°7' after the chord type (e.g., B°7).
- You can also write the diminished triads with just '°' (e.g., C°).

### Additional Chords

- There are additional chords like 'CMaj9', 'Dm11b5', 'Gm11b5', etc., which follow similar patterns as described above.



## Contributing

If you would like to contribute to this project, feel free to open issues or submit pull requests.

---

Happy music composition!
