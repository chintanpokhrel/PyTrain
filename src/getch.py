def _find_getch():
	try:
		import termios
	except ImportError:
		import msvcrt
		return msvcrt.getch

	import sys, tty
	def _getch():
		fd = sys.stdin.fileno()
		old = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old)

		return ch
	
	return _getch

getch = _find_getch()
