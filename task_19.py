#!/usr/bin/python3

from pyrob.api import *


def move_end():
	while not wall_is_on_the_right():
		move_right()
	if not wall_is_above():
		while not wall_is_above():
			move_up()
		while not wall_is_on_the_left():
			move_left()
@task
def task_8_29():
	if not wall_is_on_the_left():
		while not wall_is_on_the_left():
			move_left()
		if not wall_is_above():
			while not wall_is_above():
				move_up()
			while not wall_is_on_the_left():
				move_left()
		else:
			move_end()
	else:
		move_end()


if __name__ == '__main__':
    run_tasks()
