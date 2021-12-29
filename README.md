# SpeechToText_usingPython_GoogleAPI

There are 4 different files and below are the details.

Note: All the modules used, uses built-in **Google speech API**

1) **Speech to text**: This uses **speech_recognition module** of python to read saved audio files to recognize it and convert into Text data.
2) **Speech to text large_files**: This uses same as above and additionally uses **pydub module** to break large audio files into smaller chunks. Finally converts those and merge into one Text string.
3) **Speech to text using microphone**: Here, instead of saved audio files, it records voice directly from the mirophone. Uses **pyaudio module**
4) **Speech to text using microphone (in different languages)**: Same as 3rd point, additionally it uses language parameter to covert speech of desired language
