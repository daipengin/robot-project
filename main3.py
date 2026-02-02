from pybricks.hubs import PrimeHub  
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.parameters import Icon  
from pybricks.tools import wait  
from pybricks.pupdevices import ForceSensor


hub = PrimeHub()  
hub.display.icon(Icon.HEART) 


Left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
Right_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE)

hub.speaker.volume(50)

hub.speaker.beep(5000,500)
for i in range(5000):
    
    Right_motor.run(1000)
    Left_motor.run(1000)
    wait(1)

hub.speaker.beep(2000,500)
for i in range(5000):
    
    if i % 2 == 0:
        Right_motor.run(1000)
        Left_motor.run(1000)
    else:
        Right_motor.stop()
        Left_motor.stop()    
    
    wait(1)

hub.speaker.beep(1000,500)
for i in range(5000):
    if i % 10 < 3:
        Right_motor.run(1000)
        Left_motor.run(1000)
    else:
        Right_motor.stop()
        Left_motor.stop()    
    
    wait(1)

hub.speaker.beep(500,500)
Right_motor.stop()
Left_motor.stop()

