import sys
import random
import pickle
import time
import os 
onestats = 1
loadingtime = 3 #to insure python is loaded.
load_stats = 0
class game:
    pass
class doggos(game):
    pass
def start():
    print('Doggo City')
    print('made by')
    print('qwertydev1')
    print('loading...')
    if load_stats == 0 and onestats == 1:
        time.sleep(loadingtime)
        print('loaded!')
        print('''
 ________  ________  ________  ________  ________  ________  ___  _________    ___    ___ 
|\   ___ \|\   __  \|\   ____\|\   ____\|\   __  \|\   ____\|\  \|\___   ___\ |\  \  /  /|
\ \  \_|\ \ \  \|\  \ \  \___|\ \  \___|\ \  \|\  \ \  \___|\ \  \|___ \  \_| \ \  \/  / /
 \ \  \ \\ \ \  \\\  \ \  \  __\ \  \  __\ \  \\\  \ \  \    \ \  \   \ \  \   \ \    / / 
  \ \  \_\\ \ \  \\\  \ \  \|\  \ \  \|\  \ \  \\\  \ \  \____\ \  \   \ \  \   \/  /  /  
   \ \_______\ \_______\ \_______\ \_______\ \_______\ \_______\ \__\   \ \__\__/  / /    
    \|_______|\|_______|\|_______|\|_______|\|_______|\|_______|\|__|    \|__|\___/ /     
                                                                             \|___|/      
                                                                                          
                                                                                          
''')
print('welcome to Doggo city! type start() to start.')
