import re
from playsound import playsound
import eel
import os

from engine.command import *
from engine.config import Assistant_Name

import pywhatkit as kit

# Playing assistant sound function
@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\audio\\soft-startup-sound-269291.mp3"
    playsound(music_dir)


# Open function
@eel.expose
def openCommands(query):
    query = query.replace(Assistant_Name, "")
    query = query.replace("open", "")
    query=query.lower().strip()

    if query != "":
        speak_text(f"Opening {query}")
        os.system(f'start '+ query)
    else:
        speak_text("Please specify a valid command to open.")
    
def play_youtube(query):
    search_term = extract_search_term(query)
    if search_term:
        speak_text("Playing "+ search_term + " on YouTube")
        kit.playonyt(search_term)
        # os.system(f'start https://www.youtube.com/results?search_query={search_term}')
    else:
        speak_text("Please specify a valid search term for YouTube.")


def extract_search_term(command):
    # Remove the assistant name and 'open youtube' from the query
    # query = query.replace(Assistant_Name, "").replace("open youtube", "").strip()
    
    # Define a regular pattern to capture the song name
    pattern= r'play\s+(.*?)\s*on\s+youtube|search\s+(.*?)\s*on\s+youtube|play\s+(.*?)\s*on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        # Extract the search term from the matched groups
        search_term = match.group(1) or match.group(2) or match.group(3)
        return search_term.strip()

    # If the query is empty after cleaning, return None
    command = command.replace(Assistant_Name, "").replace("open youtube", "").strip()
    if not command:
        return None
    
    return command        