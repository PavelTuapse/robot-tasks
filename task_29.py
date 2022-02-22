#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
	fill = 0
	while fill < 3:
		if not wall_is_on_the_right():
			move_right()
		else:
			break
		if cell_is_filled():
			fill += 1
		else:
			fill = 0

if __name__ == '__main__':
    run_tasks()
