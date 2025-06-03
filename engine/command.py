import pyttsx3
import speech_recognition as sr
import eel
import time

@eel.expose
def speak_text(text):
    engine = pyttsx3.init('sapi5')  # Use 'sapi5' for Windows, 'espeak' for Linux
    voices = engine.getProperty('voices') # getting details of current voice
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 120) # Adjust the speech rate as needed
    eel.displaySpeakMessage(text)  # Display message in the UI
    engine.say(text)
    engine.runAndWait()

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
        time.sleep(2)  # Optional: Add a delay for better user experience

    except Exception as e:  
        eel.displaySpeakMessage("Sorry, I did not understand that. Please try again.")
        speak_text("Sorry, I did not understand that. Please try again.") 
        return None  
    return query.lower()  




# text = take_speech()

# speak_text(text)  

@eel.expose
def takeCommands():
      query = take_speech()
      if query:
          if 'open' in query:
              from engine.features import openCommands
              openCommands(query)

          elif 'on youtube' in query:
              from engine.features import play_youtube
              play_youtube(query)
              
        #   elif 'open google' in query:
        #       eel.open_google()
        #   elif 'open stack overflow' in query:
        #       eel.open_stackoverflow()
        #   elif 'open github' in query:
        #       eel.open_github()
        #   elif 'open facebook' in query:
        #       eel.open_facebook()
        #   elif 'open twitter' in query:
        #       eel.open_twitter()
        #   elif 'open instagram' in query:
        #       eel.open_instagram()
        #   elif 'play music' in query:
        #       eel.play_music()
        #   elif 'stop music' in query:
        #       eel.stop_music()
         
          else:
              speak_text("Sorry, I didn't understand that command.")

          eel.displayHood()
