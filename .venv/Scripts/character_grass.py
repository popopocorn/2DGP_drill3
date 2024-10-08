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
    for dy in range(90, 390, 2):
        draw_g_b(550, dy)
def run_right(cur_x):
    for dx in range(0, 150, 2):
        draw_g_b(dx + cur_x, 90)
def run_bottom():
    for dy in range(390, 90, -2):
        draw_g_b(250, dy)
def run_left():
    for dx in range(550, 250, -2):
        draw_g_b(dx, 390)



def run_rectangle():

    run_right(400)
    run_top()
    run_left()
    run_bottom()
    run_right(250)
    delay(0.5)
def run_circle():
    r, cx = 300, 800//2
    cy = r + 90
    for i in range(270, 630):

        dx=cos(radians(i))*r
        dy=sin(radians(i))*r
        draw_g_b(cx+dx,cy+dy)
    delay(0.5)

def run_climb1():
    max_y=300*tan(radians(60))
    dx=550
    dy=90
    while dx>=400 and dy<=90+max_y:
        draw_g_b(dx, dy)
        dx-=1
        dy+=tan(radians(60))
    return dy

def run_climb2(dy):
    dx = 400
    while dx >= 250 and dy >= 90:
        draw_g_b(dx, dy)
        dx -= 1
        dy -= tan(radians(60))


def run_triangle():
    run_right(400)
    climb1_y = run_climb1()
    run_climb2(climb1_y)
    run_right(250)
    delay(0.5)



while True:

    run_rectangle()

    run_circle()

    run_triangle()
    break
close_canvas()
