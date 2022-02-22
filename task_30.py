#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
	step = 0
	while not wall_is_on_the_right():
		move_right()
		step += 1
	for i in range(step):
		if not wall_is_beneath():
			for j in range(step):
				if j != i  and j != step-i:
					fill_cell()
				move_down()
		else:
			for j in range(step):
				if j != i and j != step-i:
					fill_cell()
				move_up()

		if not wall_is_on_the_left():
			if not wall_is_on_the_left() and not wall_is_on_the_right():
				fill_cell()
			move_left()
	if wall_is_on_the_left():
		for j in range(step):
			if j != 0:
				fill_cell()
			move_down()



if __name__ == '__main__':
    run_tasks()
