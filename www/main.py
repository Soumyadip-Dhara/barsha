import sys
import os

import eel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.features import *

eel.init("www")

playAssistantSound()

os.system('start msedge.exe --app="http://localhost:8000/index.html"')



eel.start('index.html', mode=None, 
        #    size=(800, 600), position=(100, 100), port=8000,
           host='localhost', block=True)

