from pico2d import *
from math import *
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

def run_rectangle():
    clear_canvas_now()
    print('rectangle')
    delay(0.5)
def run_circle():
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400, 90)





    print('circle')
    delay(0.5)
    pass




while True:

    run_rectangle()

    run_circle()
    break
close_canvas()
