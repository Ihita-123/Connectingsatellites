import pgzrun
import random

WIDTH=  600
HEIGHT= 400

no_of_sats=0
sats=[]
for i in range(10):
    satellite=Actor("satellite")
    satellite.x=random.randint(50,WIDTH-50)
    satellite.y=random.randint(50,HEIGHT-50)
    sats.append(satellite)

def draw ():
    screen.blit("spacebg",(0,0))
    for i in sats:
        i.draw()

pgzrun.go()

