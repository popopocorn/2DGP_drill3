from pico2d import *
from math import *
open_canvas(800, 800)
grass = load_image('grass.png')
character = load_image('character.png')

def run_rectangle():
    clear_canvas_now()
    print('rectangle')
    delay(0.5)
def run_circle():
    r, cx = 300, 800//2
    cy = r + 90
    for i in range(270, 630):

        clear_canvas()
        grass.draw_now(400, 30)
        dx=cos(radians(i))*r
        dy=sin(radians(i))*r
        character.draw_now(cx+ dx, cy+dy)
        update_canvas()
        delay(0.01)





    pass




while True:

    run_rectangle()

    run_circle()
    a=input('press enter to continue')
close_canvas()
