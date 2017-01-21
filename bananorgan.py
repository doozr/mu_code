from microbit import *

import music 

while True:
    if pin1.is_touched() and pin2.is_touched():
        music.play("B4:2")
        
    elif pin2.is_touched():
        music.play("A4:2")
    
    elif pin1.is_touched():
        music.play("G4:2")