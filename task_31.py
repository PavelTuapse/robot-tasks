#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
<<<<<<< HEAD
	while True:
		if not wall_is_beneath():
			move_down()
		
=======
	if not wall_is_beneath():
		while not wall_is_beneath():
			move_down()
		while not wall_is_on_the_left() and wall_is_beneath():
			move_left()
			if not wall_is_beneath():
				while not wall_is_beneath():
					move_down()


>>>>>>> eefadc023f072a1e1e74e4fc2b4516bf53209d7c


if __name__ == '__main__':
    run_tasks()
