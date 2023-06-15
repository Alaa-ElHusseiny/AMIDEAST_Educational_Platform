import pyaudio
import wave
import speech_recognition as sr

# Set parameters for recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 3

# Initialize PyAudio object and open stream for recording
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Record audio for specified duration
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# Stop recording and close the stream
stream.stop_stream()
stream.close()
p.terminate()

# Save recorded audio to a WAV file
wf = wave.open("recorded_audio.wav", "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()

# Load recorded audio file and initialize recognizer object
r = sr.Recognizer()
with sr.AudioFile("recorded_audio.wav") as source:
    audio_data = r.record(source)

# Convert speech to text using Google Speech Recognition API
try:
    text = r.recognize_google(audio_data)
    print(f"Speech recognized: {text}")
except sr.UnknownValueError:
    print("Speech recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

english_keywords     = ["english", "language"      ,"speaking"   ,"listening","writing"]
programming_keywords = ["code"   , "programming"   , "python"    , "program"]
sdg_keywords         = ["goals"  , "sustainability","development","green"]

for english_key in english_keywords:
    if english_key in text.lower():
        print("I'm happy that you want to learn English")
        break
for programming_key in programming_keywords:
    if programming_key in text.lower():
        print("I'm happy that you want to learn Programming")
        break
for sdg_key in sdg_keywords:
    if sdg_key in text.lower():
        print("I'm happy that you want to learn SDG")
        break


