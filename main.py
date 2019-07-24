import pygame as py
from person import Person
from flat import Flat
from level_1 import *
py.init()

width = 1000
height = 600
window = py.display.set_mode([width, height])
rect = window.get_rect()
window.fill((255, 255, 255))

clock = py.time.Clock()

person = Person(width, height)
person.yPos = 530

level = level(window)

objects = []
#objects.append(rect)        
for i in range(len(level.platforms)):
    objects.append(level.platforms[i].rect)

run = True
while run:
    clock.tick(50)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    keys = py.key.get_pressed()

    

    person.move(keys, objects)

    window.fill((255,255,255))
    level.drawLevel(window)
    person.draw(window)  # always last
    py.display.update()
py.quit()
