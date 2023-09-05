# data.py

# Chord to MIDI mapping
chord_to_midi = {
            # Major chords
            'C': [60, 64, 67],
            'C#': [61, 65, 68],
            'Db': [61, 65, 68],
            'D': [62, 66, 69],
            'D#': [63, 67, 70],
            'Eb': [63, 67, 70],
            'E': [64, 68, 71],
            'F': [65, 69, 72],
            'F#': [66, 70, 73],
            'Gb': [66, 70, 73],
            'G': [67, 71, 74],
            'G#': [68, 72, 75],
            'Ab': [68, 72, 75],
            'A': [69, 73, 76],
            'A#': [70, 74, 77],
            'Bb': [70, 74, 77],
            'B': [71, 75, 78],

            # Minor chords
            'Cm': [60, 63, 67],
            'C#m': [61, 64, 68],
            'Dbm': [61, 64, 68],
            'Dm': [62, 65, 69],
            'D#m': [63, 66, 70],
            'Ebm': [63, 66, 70],
            'Em': [64, 67, 71],
            'Fm': [65, 68, 72],
            'F#m': [66, 69, 73],
            'Gbm': [66, 69, 73],
            'Gm': [67, 70, 74],
            'G#m': [68, 71, 75],
            'Abm': [68, 71, 75],
            'Am': [69, 72, 76],
            'A#m': [70, 73, 77],
            'Bbm': [70, 73, 77],
            'Bm': [71, 74, 78],

            # Diminished chords
            'Cdim': [60, 63, 66],
            'C#dim': [61, 64, 67],
            'Dbdim': [61, 64, 67],
            'Ddim': [62, 65, 68],
            'D#dim': [63, 66, 69],
            'Ebdim': [63, 66, 69],
            'Edim': [64, 67, 70],
            'Fdim': [65, 68, 71],
            'F#dim': [66, 69, 72],
            'Gbdim': [66, 69, 72],
            'Gdim': [67, 70, 73],
            'G#dim': [68, 71, 74],
            'Abdim': [68, 71, 74],
            'Adim': [69, 72, 75],
            'A#dim': [70, 73, 76],
            'Bbdim': [70, 73, 76],
            'Bdim': [71, 74, 77],
            # Augmented chords
            'Caug': [60, 64, 68],
            'C#aug': [61, 65, 69],
            'Dbaug': [61, 65, 69],
            'Daug': [62, 66, 70],
            'D#aug': [63, 67, 71],
            'Ebaug': [63, 67, 71],
            'Eaug': [64, 68, 72],
            'Faug': [65, 69, 73],
            'F#aug': [66, 70, 74],
            'Gbaug': [66, 70, 74],
            'Gaug': [67, 71, 75],
            'G#aug': [68, 72, 76],
            'Abaug': [68, 72, 76],
            'Aaug': [69, 73, 77],
            'A#aug': [70, 74, 78],
            'Bbaug': [70, 74, 78],
            'Baug': [71, 75, 79],

            # Additional Diminished Triads
            'C°': [60, 63, 66],
            'D°': [62, 65, 68],
            'E°': [64, 67, 70],
            'F°': [65, 68, 71],
            'G°': [67, 70, 73],
            'A°': [69, 72, 75],
            'B°': [71, 74, 77],


            # Major 7th chords
            'CMaj7': [60, 64, 67, 71],
            'C#Maj7': [61, 65, 68, 72],
            'DbMaj7': [61, 65, 68, 72],  # Same as C#Maj7
            'DMaj7': [62, 66, 69, 73],
            'D#Maj7': [63, 67, 70, 74],
            'EbMaj7': [63, 67, 70, 74],  # Same as D#Maj7
            'EMaj7': [64, 68, 71, 75],
            'FMaj7': [65, 69, 72, 76],
            'F#Maj7': [66, 70, 73, 77],
            'GbMaj7': [66, 70, 73, 77],  # Same as F#Maj7
            'GMaj7': [67, 71, 74, 78],
            'G#Maj7': [68, 72, 75, 79],
            'AbMaj7': [68, 72, 75, 79],  # Same as G#Maj7
            'AMaj7': [69, 73, 76, 80],
            'A#Maj7': [70, 74, 77, 81],
            'BbMaj7': [70, 74, 77, 81],  # Same as A#Maj7
            'BMaj7': [71, 75, 78, 82],

            # Dominant 7th chords
            'C7': [60, 64, 67, 70],
            'C#7': [61, 65, 68, 71],
            'Db7': [61, 65, 68, 71],
            'D7': [62, 66, 69, 72],
            'D#7': [63, 67, 70, 73],
            'Eb7': [63, 67, 70, 73],
            'E7': [64, 68, 71, 74],
            'F7': [65, 69, 72, 75],
            'F#7': [66, 70, 73, 76],
            'Gb7': [66, 70, 73, 76],
            'G7': [67, 71, 74, 77],
            'G#7': [68, 72, 75, 78],
            'Ab7': [68, 72, 75, 78],
            'A7': [69, 73, 76, 79],
            'A#7': [70, 74, 77, 80],
            'Bb7': [70, 74, 77, 80],
            'B7': [71, 75, 78, 81],

            # Minor 7th chords
            'Cm7': [60, 63, 67, 70],
            'C#m7': [61, 64, 68, 71],
            'Dbm7': [61, 64, 68, 71],
            'Dm7': [62, 65, 69, 72],
            'D#m7': [63, 66, 70, 73],
            'Ebm7': [63, 66, 70, 73],
            'Em7': [64, 67, 71, 74],
            'Fm7': [65, 68, 72, 75],
            'F#m7': [66, 69, 73, 76],
            'Gbm7': [66, 69, 73, 76],
            'Gm7': [67, 70, 74, 77],
            'G#m7': [68, 71, 75, 78],
            'Abm7': [68, 71, 75, 78],
            'Am7': [69, 72, 76, 79],
            'A#m7': [70, 73, 77, 80],
            'Bbm7': [70, 73, 77, 80],
            'Bm7': [71, 74, 78, 81],
            # Minor 7th flat five chords (Half-diminished)
            'Cm7b5': [60, 63, 66, 70],
            'C#m7b5': [61, 64, 67, 71],
            'Dbm7b5': [61, 64, 67, 71],  # Same as C#m7b5
            'Dm7b5': [62, 65, 68, 72],
            'D#m7b5': [63, 66, 69, 73],
            'Ebm7b5': [63, 66, 69, 73],  # Same as D#m7b5
            'Em7b5': [64, 67, 70, 74],
            'Fm7b5': [65, 68, 71, 75],
            'F#m7b5': [66, 69, 72, 76],
            'Gbm7b5': [66, 69, 72, 76],  # Same as F#m7b5
            'Gm7b5': [67, 70, 73, 77],
            'G#m7b5': [68, 71, 74, 78],
            'Abm7b5': [68, 71, 74, 78],  # Same as G#m7b5
            'Am7b5': [69, 72, 75, 79],
            'A#m7b5': [70, 73, 76, 80],
            'Bbm7b5': [70, 73, 76, 80],  # Same as A#m7b5
            'Bm7b5': [71, 74, 77, 81],

            # Diminished 7th chords
            'C°7': [60, 63, 66, 69],
            'C#°7': [61, 64, 67, 70],
            'Db°7': [61, 64, 67, 70],  # Same as C#°7
            'D°7': [62, 65, 68, 71],
            'D#°7': [63, 66, 69, 72],
            'Eb°7': [63, 66, 69, 72],  # Same as D#°7
            'E°7': [64, 67, 70, 73],
            'F°7': [65, 68, 71, 74],
            'F#°7': [66, 69, 72, 75],
            'Gb°7': [66, 69, 72, 75],  # Same as F#°7
            'G°7': [67, 70, 73, 76],
            'G#°7': [68, 71, 74, 77],
            'Ab°7': [68, 71, 74, 77],  # Same as G#°7
            'A°7': [69, 72, 75, 78],
            'A#°7': [70, 73, 76, 79],
            'Bb°7': [70, 73, 76, 79],  # Same as A#°7
            'B°7': [71, 74, 77, 80],
            # Additional Chords

            # Dominant 9th chords
            'C9': [60, 64, 67, 70, 74],
            'C#9': [61, 65, 68, 71, 75],
            'Db9': [61, 65, 68, 71, 75],  # Same as C#9
            'D9': [62, 66, 69, 72, 76],
            'D#9': [63, 67, 70, 73, 77],
            'Eb9': [63, 67, 70, 73, 77],  # Same as D#9
            'E9': [64, 68, 71, 74, 78],
            'F9': [65, 69, 72, 75, 79],
            'F#9': [66, 70, 73, 76, 80],
            'Gb9': [66, 70, 73, 76, 80],  # Same as F#9
            'G9': [67, 71, 74, 77, 81],
            'G#9': [68, 72, 75, 78, 82],
            'Ab9': [68, 72, 75, 78, 82],  # Same as G#9
            'A9': [69, 73, 76, 79, 83],
            'A#9': [70, 74, 77, 80, 84],
            'Bb9': [70, 74, 77, 80, 84],  # Same as A#9
            'B9': [71, 75, 78, 81, 85],

            # Major 9th chords
            'CMaj9': [60, 64, 67, 71, 74],
            'C#Maj9': [61, 65, 68, 72, 75],
            'DbMaj9': [61, 65, 68, 72, 75],  # Same as C#Maj9
            'DMaj9': [62, 66, 69, 73, 76],
            'D#Maj9': [63, 67, 70, 74, 77],
            'EbMaj9': [63, 67, 70, 74, 77],  # Same as D#Maj9
            'EMaj9': [64, 68, 71, 75, 78],
            'FMaj9': [65, 69, 72, 76, 79],
            'F#Maj9': [66, 70, 73, 77, 80],
            'GbMaj9': [66, 70, 73, 77, 80],  # Same as F#Maj9
            'GMaj9': [67, 71, 74, 78, 81],
            'G#Maj9': [68, 72, 75, 79, 82],
            'AbMaj9': [68, 72, 75, 79, 82],  # Same as G#Maj9
            'AMaj9': [69, 73, 76, 80, 83],
            'A#Maj9': [70, 74, 77, 81, 84],
            'BbMaj9': [70, 74, 77, 81, 84],  # Same as A#Maj9
            'BMaj9': [71, 75, 78, 82, 85],

            # Minor 9th chords
            'Cm9': [60, 63, 67, 70, 74],
            'C#m9': [61, 64, 68, 71, 75],
            'Dbm9': [61, 64, 68, 71, 75],  # Same as C#m9
            'Dm9': [62, 65, 69, 72, 76],
            'D#m9': [63, 66, 70, 73, 77],
            'Ebm9': [63, 66, 70, 73, 77],  # Same as D#m9
            'Em9': [64, 67, 71, 74, 78],
            'Fm9': [65, 68, 72, 75, 79],
            'F#m9': [66, 69, 73, 76, 80],
            'Gbm9': [66, 69, 73, 76, 80],  # Same as F#m9
            'Gm9': [67, 70, 74, 77, 81],
            'G#m9': [68, 71, 75, 78, 82],
            'Abm9': [68, 71, 75, 78, 82],  # Same as G#m9
            'Am9': [69, 72, 76, 79, 83],
            'A#m9': [70, 73, 77, 80, 84],
            'Bbm9': [70, 73, 77, 80, 84],  # Same as A#m9
            'Bm9': [71, 74, 78, 81, 85],

            # 11th chords are usually extensions of the 9th chords with the added 11th (or 4th). 
            # Since 11th chords can become quite dense, often certain tones (like the 5th) are omitted, 
            # but for simplicity, I'll list the full chord structures.

            # Dominant 11th chords
            'C11': [60, 64, 67, 70, 74, 77],
            'C#11': [61, 65, 68, 71, 75, 78],
            'Db11': [61, 65, 68, 71, 75, 78],  # Same as C#11
            'D11': [62, 66, 69, 72, 76, 79],
            'D#11': [63, 67, 70, 73, 77, 80],
            'Eb11': [63, 67, 70, 73, 77, 80],  # Same as D#11
            'E11': [64, 68, 71, 74, 78, 81],
            'F11': [65, 69, 72, 75, 79, 82],
            'F#11': [66, 70, 73, 76, 80, 83],
            'Gb11': [66, 70, 73, 76, 80, 83],  # Same as F#11
            'G11': [67, 71, 74, 77, 81, 84],
            'G#11': [68, 72, 75, 78, 82, 85],
            'Ab11': [68, 72, 75, 78, 82, 85],  # Same as G#11
            'A11': [69, 73, 76, 79, 83, 86],
            'A#11': [70, 74, 77, 80, 84, 87],
            'Bb11': [70, 74, 77, 80, 84, 87],  # Same as A#11
            'B11': [71, 75, 78, 81, 85, 88],
            # Minor 11th Flat 5 chords
            'Gm11b5': [67, 70, 73, 77, 81, 84],  # G, B♭, D♭, F, A, C
            'G#m11b5': [68, 71, 74, 78, 82, 85], # G#, B, D, F#, A#, C#
            'Abm11b5': [68, 71, 74, 78, 82, 85], # Same as G#m11b5
            'Am11b5': [69, 72, 75, 79, 83, 86],  # A, C, E♭, G, B, D
            'A#m11b5': [70, 73, 76, 80, 84, 87], # A#, C#, E, G#, C, D#
            'Bbm11b5': [70, 73, 76, 80, 84, 87], # Same as A#m11b5
            'Bm11b5': [71, 74, 77, 81, 85, 88],  # B, D, F, A, C#, E
            'Cm11b5': [60, 63, 66, 70, 74, 77],  # C, E♭, G♭, B♭, D, F
            'C#m11b5': [61, 64, 67, 71, 75, 78], # C#, E, G, B, D#, F#
            'Dbm11b5': [61, 64, 67, 71, 75, 78], # Same as C#m11b5
            'Dm11b5': [62, 65, 68, 72, 76, 79],  # D, F, A♭, C, E, G
            'D#m11b5': [63, 66, 69, 73, 77, 80], # D#, F#, A, C#, F, G#
            'Ebm11b5': [63, 66, 69, 73, 77, 80], # Same as D#m11b5
            'Em11b5': [64, 67, 70, 74, 78, 81],  # E, G, B♭, D, F#, A
            'Fm11b5': [65, 68, 71, 75, 79, 82],  # F, A♭, C♭, E♭, G, B♭
            'F#m11b5': [66, 69, 72, 76, 80, 83], # F#, A, C, E, G#, B
            'Gbm11b5': [66, 69, 72, 76, 80, 83], # Same as F#m11b5
            # Minor 11th chords
            'Cm11': [60, 63, 67, 70, 74, 77],  # C, E♭, G, B♭, D, F
            'C#m11': [61, 64, 68, 71, 75, 78],
            'Dbm11': [61, 64, 68, 71, 75, 78],  # Same as C#m11
            'Dm11': [62, 65, 69, 72, 76, 79],
            'D#m11': [63, 66, 70, 73, 77, 80],
            'Ebm11': [63, 66, 70, 73, 77, 80],  # Same as D#m11
            'Em11': [64, 67, 71, 74, 78, 81],
            'Fm11': [65, 68, 72, 75, 79, 82],
            'F#m11': [66, 69, 73, 76, 80, 83],
            'Gbm11': [66, 69, 73, 76, 80, 83],  # Same as F#m11
            'Gm11': [67, 70, 74, 77, 81, 84],
            'G#m11': [68, 71, 75, 78, 82, 85],
            'Abm11': [68, 71, 75, 78, 82, 85],  # Same as G#m11
            'Am11': [69, 72, 76, 79, 83, 86],
            'A#m11': [70, 73, 77, 80, 84, 87],
            'Bbm11': [70, 73, 77, 80, 84, 87],  # Same as A#m11
            'Bm11': [71, 74, 78, 81, 85, 88],

            # Major 11th chords
            'CMaj11': [60, 64, 67, 71, 74, 77],
            'C#Maj11': [61, 65, 68, 72, 75, 78],
            'DbMaj11': [61, 65, 68, 72, 75, 78],  # Same as C#Maj11
            'DMaj11': [62, 66, 69, 73, 76, 79],
            'D#Maj11': [63, 67, 70, 74, 77, 80],
            'EbMaj11': [63, 67, 70, 74, 77, 80],  # Same as D#Maj11
            'EMaj11': [64, 68, 71, 75, 78, 81],
            'FMaj11': [65, 69, 72, 76, 79, 82],
            'F#Maj11': [66, 70, 73, 77, 80, 83],
            'GbMaj11': [66, 70, 73, 77, 80, 83],  # Same as F#Maj11
            'GMaj11': [67, 71, 74, 78, 81, 84],
            'G#Maj11': [68, 72, 75, 79, 82, 85],
            'AbMaj11': [68, 72, 75, 79, 82, 85],  # Same as G#Maj11
            'AMaj11': [69, 73, 76, 80, 83, 86],
            'A#Maj11': [70, 74, 77, 81, 84, 87],
            'BbMaj11': [70, 74, 77, 81, 84, 87],  # Same as A#Maj11
            'BMaj11': [71, 75, 78, 82, 85, 88],
            # Minor 11th Flat 5 chords
            'Cm11b5': [60, 63, 66, 70, 74, 77],  # C, E♭, G♭, B♭, D, F
            'C#m11b5': [61, 64, 67, 71, 75, 78],  # C#, E, G, B, D#, F#
            'Dbm11b5': [61, 64, 67, 71, 75, 78],  # Same as C#m11b5
            'Dm11b5': [62, 65, 68, 72, 76, 79],  # D, F, A♭, C, E, G
            'D#m11b5': [63, 66, 69, 73, 77, 80],  # D#, F#, A, C#, F, G#
            'Ebm11b5': [63, 66, 69, 73, 77, 80],  # Same as D#m11b5
            'Em11b5': [64, 67, 70, 74, 78, 81],  # E, G, B♭, D, F#, A
            'Fm11b5': [65, 68, 71, 75, 79, 82],  # F, A♭, C♭, E♭, G, B♭
            'F#m11b5': [66, 69, 72, 76, 80, 83],  # F#, A, C, E, G#, B
            'Gbm11b5': [66, 69, 72, 76, 80, 83],  # Same as F#m11b5
            'Gm11b5': [67, 70, 73, 77, 81, 84],  # G, B♭, D♭, F, A, C
            'G#m11b5': [68, 71, 74, 78, 82, 85],  # G#, B, D, F#, A#, C#
            'Abm11b5': [68, 71, 74, 78, 82, 85],  # Same as G#m11b5
            'Am11b5': [69, 72, 75, 79, 83, 86],  # A, C, E♭, G, B, D
            'A#m11b5': [70, 73, 76, 80, 84, 87],  # A#, C#, E, G#, C, D#
            'Bbm11b5': [70, 73, 76, 80, 84, 87],  # Same as A#m11b5
            'Bm11b5': [71, 74, 77, 81, 85, 88]   # B, D, F, A, C#, E


        }

def get_chords_for_tonality(tonality, user_input_chords=[]):
    if user_input_chords and len(user_input_chords) > 1:
        return [chord.strip() for chord in user_input_chords]

            # Default chords for Major and minor keys
    chord_map = {
        'C': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'],
        'Cm': ['Cm', 'Ddim', 'Eb', 'Fm', 'G', 'Ab', 'Bb'],
        'C7': ['C7', 'Dm7', 'Em7', 'FMaj7', 'G7', 'Am7', 'Bm7b5'],
        'Cm7': ['Cm7', 'Dm7b5', 'EbMaj7', 'Fm7', 'G7', 'AbMaj7', 'Bb7'],
        'C9': ['C9', 'Dm9', 'Em9', 'FMaj9', 'G9', 'Am9', 'Bm11b5'],
        'Cm9': ['Cm9', 'Dm11b5', 'EbMaj9', 'Fm9', 'G9', 'AbMaj9', 'Bb9'],
        'CMaj7': ['CMaj7', 'Dm7', 'Em7', 'FMaj7', 'G7', 'Am7', 'Bm7b5'],
        'Cdorian': ['Cm', 'Dm', 'Eb', 'F', 'Gm', 'A°', 'Bb'],
        'Cphrygian': ['Cm', 'Db', 'Eb', 'Fm', 'Gdim', 'Ab', 'Bb'],

        'D': ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#dim'],
        'Dm': ['Dm', 'Edim', 'F', 'Gm', 'A', 'Bb', 'C'],
        'D7': ['D7', 'Em7', 'F#m7', 'GMaj7', 'A7', 'Bm7', 'C#m7b5'],
        'Dm7': ['Dm7', 'Em7b5', 'FMaj7', 'Gm7', 'A7', 'BbMaj7', 'C7'],
        'D9': ['D9', 'Em9', 'F#m9', 'GMaj9', 'A9', 'Bm9', 'C#m11b5'],
        'Dm9': ['Dm9', 'Em11b5', 'FMaj9', 'Gm9', 'A9', 'BbMaj9', 'C9'],
        'DMaj7': ['DMaj7', 'Em7', 'F#m7', 'GMaj7', 'A7', 'Bm7', 'C#m7b5'],
        'Ddorian': ['Dm', 'Em', 'F', 'G', 'Am', 'B°', 'C'],
        'Dphrygian': ['Dm', 'Eb', 'F', 'Gm', 'Adim', 'Bb', 'C'],

        'E': ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#dim'],
        'Em': ['Em', 'F#dim', 'G', 'Am', 'B', 'C', 'D'],
        'E7': ['E7', 'F#m7', 'G#m7', 'AMaj7', 'B7', 'C#m7', 'D#m7b5'],
        'Em7': ['Em7', 'F#m7b5', 'GMaj7', 'Am7', 'B7', 'CMaj7', 'D7'],
        'E9': ['E9', 'F#m9', 'G#m9', 'AMaj9', 'B9', 'C#m9', 'D#m11b5'],
        'Em9': ['Em9', 'F#m11b5', 'GMaj9', 'Am9', 'B9', 'CMaj9', 'D9'],
        'EMaj7': ['EMaj7', 'F#m7', 'G#m7', 'AMaj7', 'B7', 'C#m7', 'D#m7b5'],
        'Edorian': ['Em', 'F#m', 'G', 'A', 'Bm', 'C#°', 'D'],
        'Ephrygian': ['Em', 'F', 'G', 'Am', 'Bdim', 'C', 'D'], 

        'F': ['F', 'Gm', 'Am', 'Bb', 'C', 'Dm', 'Edim'],
        'Fm': ['Fm', 'Gdim', 'Ab', 'Bbm', 'C', 'Db', 'Eb'],
        'F7': ['F7', 'Gm7', 'Am7', 'BbMaj7', 'C7', 'Dm7', 'E7b5'],
        'Fm7': ['Fm7', 'Gm7b5', 'AbMaj7', 'Bbm7', 'C7', 'DbMaj7', 'Eb7'],
        'F9': ['F9', 'Gm9', 'Am9', 'BbMaj9', 'C9', 'Dm9', 'Em11b5'],
        'Fm9': ['Fm9', 'Gm11b5', 'AbMaj9', 'Bbm9', 'C9', 'DbMaj9', 'Eb9'],
        'FMaj7': ['FMaj7', 'Gm7', 'Am7', 'BbMaj7', 'C7', 'Dm7', 'Em7b5'],
        'Fdorian': ['Fm', 'Gm', 'Ab', 'Bb', 'Cm', 'D°', 'Eb'],
        'Fphrygian': ['Fm', 'Gb', 'Ab', 'Bbm', 'Cdim', 'Db', 'Eb'],

        'G': ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#dim'],
        'Gm': ['Gm', 'Adim', 'Bb', 'Cm', 'D', 'Eb', 'F'],
        'G7': ['G7', 'Am7', 'Bm7', 'CMaj7', 'D7', 'Em7', 'F#m7b5'],
        'Gm7': ['Gm7', 'Am7b5', 'BbMaj7', 'Cm7', 'D7', 'EbMaj7', 'F7'],
        'G9': ['G9', 'Am9', 'Bm9', 'CMaj9', 'D9', 'Em9', 'F#m11b5'],
        'Gm9': ['Gm9', 'Am11b5', 'BbMaj9', 'Cm9', 'D9', 'EbMaj9', 'F9'],
        'GMaj7': ['GMaj7', 'Am7', 'Bm7', 'CMaj7', 'D7', 'Em7', 'F#m7b5'],
        'Gdorian': ['Gm', 'Am', 'Bb', 'C', 'Dm', 'E°', 'F'],
        'Gphrygian': ['Gm', 'Ab', 'Bb', 'Cm', 'Ddim', 'Eb', 'F'],

        'A': ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#dim'],
        'Am': ['Am', 'Bdim', 'C', 'Dm', 'E', 'F', 'G'],
        'A7': ['A7', 'Bm7', 'C#m7', 'DMaj7', 'E7', 'F#m7', 'G#m7b5'],
        'Am7': ['Am7', 'Bm7b5', 'CMaj7', 'Dm7', 'E7', 'FMaj7', 'G7'],
        'A9': ['A9', 'Bm9', 'C#m9', 'DMaj9', 'E9', 'F#m9', 'G#m11b5'],
        'Am9': ['Am9', 'Bm11b5', 'CMaj9', 'Dm9', 'E9', 'FMaj9', 'G9'],
        'AMaj7': ['AMaj7', 'Bm7', 'C#m7', 'DMaj7', 'E7', 'F#m7', 'G#m7b5'],
        'Adorian': ['Am', 'Bm', 'C', 'D', 'Em', 'F#°', 'G'],
        'Aphrygian': ['Am', 'Bb', 'C', 'Dm', 'Edim', 'F', 'G'],


        'B': ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#dim'],
        'Bm': ['Bm', 'C#dim', 'D', 'Em', 'F#', 'G', 'A'],
        'B7': ['B7', 'C#m7', 'D#m7', 'EMaj7', 'F#7', 'G#m7', 'A#m7b5'],
        'Bm7': ['Bm7', 'C#m7b5', 'DMaj7', 'Em7', 'F#7', 'GMaj7', 'A7'],
        'B9': ['B9', 'C#m9', 'D#m9', 'EMaj9', 'F#9', 'G#m9', 'A#m11b5'],
        'Bm9': ['Bm9', 'C#m11b5', 'DMaj9', 'Em9', 'F#9', 'GMaj9', 'A9'],
        'BMaj7': ['BMaj7', 'C#m7', 'D#m7', 'EMaj7', 'F#7', 'G#m7', 'A#m7b5'],
        'Bdorian': ['Bm', 'C#m', 'D', 'E', 'F#m', 'G#°', 'A'],
        'Bphrygian': ['Bm', 'C', 'D', 'Em', 'F#dim', 'G', 'A']

}


    return chord_map.get(tonality, [])