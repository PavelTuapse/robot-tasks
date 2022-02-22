#!/usr/bin/python3

from pyrob.api import *

def cross():
	move_right(1)
	for i in range(3):
		move_down()
		fill_cell()
	move_right()
	move_up()
	fill_cell()
	for i in range(2):
		move_left()
		fill_cell()

@task
def task_2_2():
	for i in range(5):
		cross()
		move_up()
		if i != 4:
			move_up()
			move_right(4)



if __name__ == '__main__':
    run_tasks()
