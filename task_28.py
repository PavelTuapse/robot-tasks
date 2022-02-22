#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
	fill = 0
	while fill < 5:
		move_right()
		if cell_is_filled():
			fill += 1


if __name__ == '__main__':
    run_tasks()
