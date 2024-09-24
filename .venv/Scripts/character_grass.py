from pico2d import *
from math import *
open_canvas(800, 800)
grass = load_image('grass.png')
character = load_image('character.png')


def draw_g_b(x,y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)
def run_top():
    for dy in range(0, 600, 10):
        draw_g_b(0, dy)
def run_right():
    for dx in range(0, 800, 10):
        draw_g_b(dx, 600)
def run_bottom():
    for dy in range(600, 0, -10):
        draw_g_b(800, dy)
def run_left():
    for dx in range(800, 0, -10):
        draw_g_b(dx, 0)



def run_rectangle():

    run_right()
    run_bottom()
    run_left()
    run_top()




    print('rectangle')
    delay(0.5)
def run_circle():
    r, cx = 300, 800//2
    cy = r + 90
    for i in range(270, 630):

        dx=cos(radians(i))*r
        dy=sin(radians(i))*r
        draw_g_b(cx+dx,cy+dy)





    pass




while True:

    run_rectangle()

    run_circle()

close_canvas()
