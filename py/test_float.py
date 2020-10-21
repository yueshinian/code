#!/usr/bin/env python

import sys, select, termios, tty

msg = """
Control Your model!
---------------------------
input a number with rad:

CTRL-C to quit
"""

def getKey():
	tty.setraw(sys.stdin)
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False


if __name__=="__main__":
	settings = termios.tcgetattr(sys.stdin)

	change_angle=0

	try:
		print msg
		while 1:
			change_angle=0
			key = getKey()
                        if is_number(key) :
                            change_angle=key
                        else:
                            print("ERROR!Please input a number!")
			    if (key == '\x03'):
					break
			print change_angle

	except Exception , e:
		print e,"shit"



