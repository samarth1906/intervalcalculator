music_notes = {
    'C': 1,
    'C#': 2,
    'D': 3,
    'D#': 4,
    'E': 5,
    'F': 6,
    'F#': 7,
    'G': 8,
    'G#': 9,
    'A': 10,
    'A#': 11,
    'B': 12,

}
note_1 = input('note 1:')
note_2 = input('note 2:')


if music_notes[note_2]-music_notes[note_1] == 1 or music_notes[note_2]-music_notes[note_1] == -11:
    print('Minor 2nd')
if music_notes[note_2]-music_notes[note_1] == 2 or music_notes[note_2]-music_notes[note_1] == -10:
    print('Major 2nd')
if music_notes[note_2] - music_notes[note_1] == 3 or music_notes[note_2]-music_notes[note_1] == -9:
    print('Minor 3rd')
if music_notes[note_2]-music_notes[note_1] == 4 or music_notes[note_2]-music_notes[note_1] == -8:
    print('Major 3rd')
if music_notes[note_2]-music_notes[note_1] == 5 or music_notes[note_2]-music_notes[note_1] == -7:
    print('Perfect 4th')
if music_notes[note_2]-music_notes[note_1] == 6 or music_notes[note_2]-music_notes[note_1] == -6:
    print('Augmented 4th')
if music_notes[note_2]-music_notes[note_1] == 7 or music_notes[note_2]-music_notes[note_1] == -5:
    print('Perfect 5th')
if music_notes[note_2]-music_notes[note_1] == 8 or music_notes[note_2]-music_notes[note_1] == -4:
    print('Minor 6th')
if music_notes[note_2]-music_notes[note_1] == 9 or music_notes[note_2]-music_notes[note_1] == -3:
    print('Major 6th')
if music_notes[note_2]-music_notes[note_1] == 10 or music_notes[note_2]-music_notes[note_1] == -2:
    print('Minor 7th')
if music_notes[note_2]-music_notes[note_1] == 11 or music_notes[note_2]-music_notes[note_1] == -1:
    print('Major 7th')
if music_notes[note_2]-music_notes[note_1] == 12 or music_notes[note_2]-music_notes[note_1] == 0:
    print('Octave')

input('Press enter to exit:')

