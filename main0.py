from pybricks.hubs import PrimeHub  
from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction
from pybricks.parameters import Icon  
from pybricks.tools import wait  


# ハブの初期化  
hub = PrimeHub()  
Left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
Right_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE)
hub.display.icon(Icon.HEART) 

#前進
Right_motor.run(500)
Left_motor.run(500)

wait(1000)

Right_motor.brake()
Left_motor.brake()
wait(500)

#後退
Right_motor.run(-500)
Left_motor.run(-500)
wait(1000)

Right_motor.stop()
Left_motor.stop()


