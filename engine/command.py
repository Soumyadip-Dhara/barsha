import pyttsx3
import speech_recognition as sr
import eel

@eel.expose
def speak_text(text):
    engine = pyttsx3.init('sapi5')  # Use 'sapi5' for Windows, 'espeak' for Linux
    voices = engine.getProperty('voices') # getting details of current voice
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def take_speech():  
    Sr= sr.Recognizer()  
    with sr.Microphone() as source:  
        print("Listening...") 
        eel.displaySpeakMessage("Listening...")  # Display message in the UI
        Sr.pause_threshold = 2 # Adjust the pause threshold as needed
        Sr.adjust_for_ambient_noise(source, duration=0.2)  
        audio = Sr.listen(source, 10)
    try:
        print("Recognizing...")  
        eel.displaySpeakMessage("Recognizing...")  # Display message in the UI
        query = Sr.recognize_google(audio, language='en-in')  
        print(f"User said: {query}\n")  
        eel.displaySpeakMessage(query)  # Display recognized text in the UI
        speak_text(query)
        eel.displayHood()

    except Exception as e:  
        eel.displaySpeakMessage("Sorry, I did not understand that. Please try again.")
        speak_text("Sorry, I did not understand that. Please try again.") 
        return None  
    return query.lower()  




# text = take_speech()

# speak_text(text)    