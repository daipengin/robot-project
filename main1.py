from pybricks.hubs import PrimeHub  
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.parameters import Icon  
from pybricks.tools import wait  


# ハブの初期化  
hub = PrimeHub()  
hub.display.icon(Icon.HEART) 


hub.speaker.volume(50)
sound =[
    (["C6/16", "R/16", "G6/16", "C7/16"],120),
    (["C5/32", "D5/32", "E5/32", "F5/32", "G5/16", "R/16", "G5/16"],160),
]

hub.speaker.play_notes(sound[0][0],sound[0][1])

hub.speaker.play_notes(sound[1][0],sound[1][1])

wait(2000)

while True:
    hub.speaker.beep(500,500)
    hub.speaker.beep(1000,500)
    hub.speaker.beep(1500,500)
    hub.speaker.beep(600,500)
    hub.speaker.beep(400,500)
    wait(1000)

  
