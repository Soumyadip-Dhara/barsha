import os

import eel

eel.init("www")

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, 
        #    size=(800, 600), position=(100, 100), port=8000,
           host='localhost', block=True)