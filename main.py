import os

import eel

eel.init('web')

os.system('start msedge.exe --app="http://192.168.43.243:5500/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)