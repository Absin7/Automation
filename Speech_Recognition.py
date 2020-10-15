import speech_recognition as sr

# Creating an object
audio = sr.Recognizer()

with sr.Microphone() as source:
    print("Please Speak....")
    # Creating an object "real_audio" for listening to the text
    real_audio = audio.listen(source, timeout=10)
    try:
        text = audio.recognize_google(real_audio)
        print("You said:")
        print(text)
    except:
        print('Please try again....')
