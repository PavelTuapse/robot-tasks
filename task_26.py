#!/usr/bin/python3

from pyrob.api import *

def cross():
	move_right()
	for i in range(2):
		fill_cell()
		move_down()
	fill_cell()
	move_right()
	move_up()
	fill_cell()
	for i in range(2):
		move_left()
		fill_cell()
	move_up()

@task(delay=0.02)
def task_2_4():
	for j in range(5):
		for i in range(10):
			cross()
			if i != 9:
				move_right(4)
		move_left(36)
		if j != 4:
			move_down(4)


if __name__ == '__main__':
    run_tasks()
