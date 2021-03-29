# AudioBook 
#PyAudio 
PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library. With PyAudio, you can easily use Python to play and record audio on a variety of platforms.      PyAudio is inspired by:

pyPortAudio/fastaudio: Python bindings for PortAudio v18 API.
tkSnack: cross-platform sound toolkit for Tcl/Tk and Python.


"""PyAudio Example: Play a wave file."""

import pyaudio
import wave
import sys

CHUNK = 1024

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# close PyAudio (5)
p.terminate()
To use PyAudio, first instantiate PyAudio using pyaudio.PyAudio() (1), which sets up the portaudio system.

To record or play audio, open a stream on the desired device with the desired audio parameters using pyaudio.PyAudio.open() (2). This sets up a pyaudio.Stream to play or record audio.

Play audio by writing audio data to the stream using pyaudio.Stream.write(), or read audio data from the stream using pyaudio.Stream.read(). (3)

Note that in “blocking mode”, each pyaudio.Stream.write() or pyaudio.Stream.read() blocks until all the given/requested frames have been played/recorded. Alternatively, to generate audio data on the fly or immediately process recorded audio data, use the “callback mode” outlined below.

Use pyaudio.Stream.stop_stream() to pause playing/recording, and pyaudio.Stream.close() to terminate the stream. (4)

Finally, terminate the portaudio session using pyaudio.PyAudio.terminate() (5)









#Speech Recognition

Installing
First, make sure you have all the requirements listed in the “Requirements” section.

The easiest way to install this is using pip install SpeechRecognition.

Otherwise, download the source distribution from PyPI, and extract the archive.

In the folder, run python setup.py install.


Requirements
To use all of the functionality of the library, you should have:

Python 2.6, 2.7, or 3.3+ (required)
PyAudio 0.2.11+ (required only if you need to use microphone input, Microphone)
PocketSphinx (required only if you need to use the Sphinx recognizer, recognizer_instance.recognize_sphinx)
Google API Client Library for Python (required only if you need to use the Google Cloud Speech API, recognizer_instance.recognize_google_cloud)
FLAC encoder (required only if the system is not x86-based Windows/Linux/OS X)

Library Reference
Library for performing speech recognition, with support for several engines and APIs, online and offline.
Speech recognition engine/API support:

CMU Sphinx (works offline)
Google Speech Recognition
Google Cloud Speech API
Wit.ai
Microsoft Bing Voice Recognition
Houndify API
IBM Speech to Text
Snowboy Hotword Detection (works offline)
