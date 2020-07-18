import speech_recognition as sr

r = sr.Recognizer()
filename = "C:/Users/p3pra/Desktop/Dproject/Recordings/recorded2.wav"
# #with sr.Microphone() as source:
#     # read the audio data from the default microphone
#     # print("Recognizing...")
#     # audio_data = r.record(source, duration=15)
#     #audio_data = "C:/Users/p3pra/Desktop/Dproject/Recordings/recorded2.wav"
#     # convert speech to text
#     #text = r.recognize_google(audio_data)
# text = r.recognize_google(audio_data,language='en-IN')
# print(text)
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)