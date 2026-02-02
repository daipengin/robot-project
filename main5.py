from pybricks.hubs import PrimeHub  
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.parameters import Icon  
from pybricks.tools import wait  
from pybricks.pupdevices import ForceSensor
from pybricks.tools import multitask, run_task


hub = PrimeHub()  
hub.display.icon(Icon.HEART) 

Left_button = ForceSensor(Port.A)
Right_button = ForceSensor(Port.B)
Left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
Right_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE)

 
flag = 0

async def motion():
    if flag == 1:
        Right_motor.run(-500)
        Left_motor.run(-500)
        await wait(500)
        Right_motor.run(-500)
        Left_motor.run(500)
        await wait(500)
    if flag == 2:
        Right_motor.run(-500)
        Left_motor.run(-500)
        await wait(500)
        Right_motor.run(500)
        Left_motor.run(-500)
        await wait(500)

    
async def sound():
    if flag == 1:
        while True:
            await hub.speaker.beep(1500,100)
    if flag == 2:
        while True:
            await hub.speaker.beep(200,100)
        

async def main():
    if flag == 1:
        hub.display.icon(Icon.ARROW_LEFT) 
        await multitask(motion(),sound(),race=True)
    if flag == 2:
        hub.display.icon(Icon.ARROW_RIGHT) 
        await multitask(motion(),sound(),race=True)
    hub.display.icon(Icon.HEART) 
    Right_motor.run(500)
    Left_motor.run(500)
    


while True:
    flag = 0
    if Left_button.touched():
        flag = 1
    if Right_button.touched():
        flag = 2
    run_task(main())