#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
	while not wall_is_on_the_right():
		if (not wall_is_beneath()) and (not wall_is_above()):
			move_up()
			fill_cell()
			move_down(2)
			fill_cell()
			move_up()
		elif not wall_is_beneath():
			move_down()
			fill_cell()
			move_up()
		elif not wall_is_above():
			move_up()
			fill_cell()
			move_down()
		else:
			fill_cell()
		move_right()

	if (not wall_is_beneath()) and (not wall_is_above()):
		move_up()
		fill_cell()
		move_down(2)
		fill_cell()
		move_up()
	elif not wall_is_beneath():
		move_down()
		fill_cell()
		move_up()
	elif not wall_is_above():
		move_up()
		fill_cell()
		move_down()
	else:
		fill_cell()


if __name__ == '__main__':
    run_tasks()
