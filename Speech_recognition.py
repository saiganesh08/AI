import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything: ")
    audio = r.listen(source,timeout=5,phrase_time_limit=25)
    print("Done, Please Wait.....")
    try:
        text = r.recognize_google(audio)
        print('You Said: {}'.format(text))
    except:
        print("Sorry! Please Try Again Later...")
