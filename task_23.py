#!/usr/bin/python3

from pyrob.api import *

def up_down():
	step = 0
	while not wall_is_above():
		move_up()
		fill_cell()
		step += 1
	for i in range(step):
		move_down()

@task(delay=0.01)
def task_6_6():
	move_right()
	while wall_is_beneath() and (not wall_is_on_the_right()):
		if not wall_is_above():
			up_down()
		move_right()
	if not wall_is_above() and wall_is_on_the_right():
			up_down()
	while wall_is_beneath():
		move_left()



if __name__ == '__main__':
    run_tasks()
