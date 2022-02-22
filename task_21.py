#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
	move_right()
	move_down()
	step = 12
	for k in range(6):
		for i in range(step):
			fill_cell()
			if k%2 == 0:
				move_down()
				fill_cell()
				move_right()
				fill_cell()
			else:
				move_left()
				fill_cell()
				move_up()
				fill_cell()
		step -= 2
		if k%2 == 0:
			move_left(2)
		else:
			move_down(2)
		fill_cell()	
	move_down()


if __name__ == '__main__':
    run_tasks()
