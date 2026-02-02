from pybricks.hubs import PrimeHub  
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.parameters import Icon  
from pybricks.tools import wait  
from pybricks.pupdevices import ForceSensor
from pybricks.tools import multitask, run_task

C1 = 131
C2 = 262
C3 = 523
Ds1 = 139
Ds2 = 277
Ds3 = 554
D1 = 147
D2 = 294
D3 = 587
Es1 = 156
Es2 = 311
Es3 = 622
E1 = 165
E2 = 330
E3 = 659
F1 = 175
F2 =  349
F3 = 698

DO1 = 262
DO2 = 523
RE1 = 147
RE2 = 294
MI1 = 165
MI2 = 330
FA1 = 175
FA2 = 349

RA1 = 110
RA2 = 220
SI1 = 117
SI2 = 233




hub = PrimeHub()  
hub.display.icon(Icon.HEART) 


Left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
Right_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE)

hub.speaker.volume(50)

async def star():
    while True:
        await hub.speaker.beep(F3,140)
        await wait(50)
        await hub.speaker.beep(F3,140)
        await wait(50)
        await hub.speaker.beep(F3,140)
        await wait(50)
        await hub.speaker.beep(D3,70)
        await wait(50)
        await hub.speaker.beep(F3,140)
        await wait(50)
        await hub.speaker.beep(F3,140)
        await wait(50)
        await hub.speaker.beep(D3,70)
        await wait(0)
        await hub.speaker.beep(F3,70)
        await wait(50)
        await hub.speaker.beep(D3,70)
        await wait(0)
        await hub.speaker.beep(F3,140)
        await wait(50)
        await hub.speaker.beep(E3,140)
        await wait(50)
        await hub.speaker.beep(E3,140)
        await wait(50)
        await hub.speaker.beep(E3,140)
        await wait(50)
        await hub.speaker.beep(C3,70)
        await wait(50)
        await hub.speaker.beep(E3,140)
        await wait(50)
        await hub.speaker.beep(E3,140)
        await wait(50)
        await hub.speaker.beep(C3,70)
        await wait(0)
        await hub.speaker.beep(E3,70)
        await wait(50)
        await hub.speaker.beep(C3,70)
        await wait(0)
        await hub.speaker.beep(E3,140)
        await wait(50)
        
async def tika():
    while True:
        await hub.speaker.beep(DO1,150)
        await wait(50)
        await hub.speaker.beep(DO2,150)
        await wait(50)
        await hub.speaker.beep(RA1,150)
        await wait(50)
        await hub.speaker.beep(RA2,150)
        await wait(50)
        await hub.speaker.beep(SI1,150)
        await wait(50)
        await hub.speaker.beep(SI2,150)
        await wait(50)
        await wait(600)
        await hub.speaker.beep(DO1,150)
        await wait(50)
        await hub.speaker.beep(DO2,150)
        await wait(50)
        await hub.speaker.beep(RA1,150)
        await wait(50)
        await hub.speaker.beep(RA2,150)
        await wait(50)
        await hub.speaker.beep(SI1,150)
        await wait(50)
        await hub.speaker.beep(SI2,150)
        await wait(50)
        await wait(600)
        await hub.speaker.beep(FA1,150)
        await wait(50)
        await hub.speaker.beep(FA2,150)
        await wait(50)
        await hub.speaker.beep(RE1,150)
        await wait(50)
        await hub.speaker.beep(RE2,150)
        await wait(50)
        await hub.speaker.beep(MI1,150)
        await wait(50)
        await hub.speaker.beep(MI2,150)
        await wait(50)
        await wait(600)
        await hub.speaker.beep(FA1,150)
        await wait(50)
        await hub.speaker.beep(FA2,150)
        await wait(50)
        await hub.speaker.beep(RE1,150)
        await wait(50)
        await hub.speaker.beep(RE2,150)
        await wait(50)
        await hub.speaker.beep(MI1,150)
        await wait(50)
        await hub.speaker.beep(MI2,150)
        await wait(50)
        await wait(600)
        


async def Right_turn():
    Left_motor.run(500)
    Right_motor.run(-500)
    await wait(8000)

async def Left_turn():
    Left_motor.run(-500)
    Right_motor.run(500)
    await wait(8000)


async def main():
    for i in range(3):
        await multitask(Right_turn(),star(),race=True)
        await multitask(Left_turn(),tika(),race=True)

run_task(main())


hub.speaker.beep(1500,500)
#前進
Right_motor.run(500)
Left_motor.run(500)

wait(1000)

hub.speaker.beep(500,500)
#後退
Right_motor.run(-500)
Left_motor.run(-500)
wait(1000)



Right_motor.stop()
Left_motor.stop()


