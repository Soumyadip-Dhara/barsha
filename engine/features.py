from playsound import playsound
import eel

# Playing assistant sound function
@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\audio\\soft-startup-sound-269291.mp3"
    playsound(music_dir)