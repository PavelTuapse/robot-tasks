#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
	step_to_left = 0
	while not wall_is_beneath():
		move_down()
	while wall_is_beneath():
		move_right()
		step_to_left += 1
	move_down()
	for i in range(step_to_left):
		move_left()


if __name__ == '__main__':
    run_tasks()
