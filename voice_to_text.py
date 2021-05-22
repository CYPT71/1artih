import speech_recognition as sr


''' recording the sound '''
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Adjusting noise ")
        # recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording for 4 seconds")
        recorded_audio = recognizer.listen(source, timeout=1)
        print("Done recording")

    ''' Recorgnizing the Audio '''
    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(
                recorded_audio, 
                language="fr-Fr"
            )
        print("Decoded Text : {}".format(text))
        return text
    except Exception as ex:
        print(ex)
        return ex
