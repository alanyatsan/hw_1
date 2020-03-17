#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_on_the_right():
          fill_cell()
          move_up()



    pass


if __name__ == '__main__':
    run_tasks()
