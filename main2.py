from pybricks.hubs import PrimeHub  
from pybricks.pupdevices import Motor
from pybricks.parameters import Port , Direction
from pybricks.parameters import Icon  
from pybricks.tools import wait  
from pybricks.pupdevices import ForceSensor


hub = PrimeHub()  
hub.display.icon(Icon.HEART) 

Left_button = ForceSensor(Port.A)
Right_button = ForceSensor(Port.B)
Left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
Right_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE)

speed = 300
while True:
    if Left_button.touched():
        Right_motor.run(-speed)
        Left_motor.run(-speed)
        wait(500)
        Right_motor.run(-speed)
        Left_motor.run(speed)
        wait(2000)
    if Right_button.touched():
        Right_motor.run(-speed)
        Left_motor.run(-speed)
        wait(500)
        Right_motor.run(speed)
        Left_motor.run(-speed)
        wait(2000)
    Right_motor.run(speed)
    Left_motor.run(speed)