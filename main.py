'''
    Code issue: Library is not working properly with pipenv
'''

from pydub import AudioSegment

sound = AudioSegment.from_file("SLANDER - Love Is Gone ft. Dylan Matthew (Acoustic) - Lyrics-jb-i_ARlumQ.m4a")

# len() and slicing are in milliseconds
halfway_point = len(sound) / 2
second_half = sound[halfway_point:]

# Concatenation is just adding
second_half_3_times = second_half + second_half + second_half

# writing mp3 files is a one liner
second_half_3_times.export("SLANDER - Love Is Gone ft. Dylan Matthew (Acoustic) - Lyrics-jb-i_ARlumQ123.mp3", format="mp3")