import os
import sys
from tkinter import *

import keyboard
import mouse


def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except AttributeError:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def s(key):
	global stat

	if not stat[key]:
		for key_iter in range(len(stat)):
			if stat[key_iter] and key_iter != key:
				match key_iter:
					case 0:
						mouse.release(button="left")
					case 1:
						mouse.release(button="middle")
					case 2:
						mouse.release(button="right")
				stat[key_iter] = False

		stat[key] = True
		match key:
			case 0:
				mouse.press(button="left")
			case 1:
				mouse.press(button="middle")
			case 2:
				mouse.press(button="right")

def r(key):
	global stat

	match key:
		case 0:
			mouse.release(button="left")
		case 1:
			mouse.release(button="middle")
		case 2:
			mouse.release(button="right")

	stat[key] = False

def main():
	global stat
	stat = [False, False, False]  # left - 0 | middle - 1 | right - 0

	root = Tk()
	root.resizable(False, False)
	root.geometry(f"250x125+{root.winfo_screenwidth() // 2 - 125}+{root.winfo_screenheight() // 2 - 62}")
	root.title("Key-Click")
	root.iconbitmap(resource_path("data/key-click-icon.ico"))
	root.config(background="#ffffff")

	title = Label(root, background="#ffffff", activebackground="#ffffff", foreground="#000000", activeforeground="#000000", text="Key-Click", font=("Helvetica", 23, "italic", "bold"))
	title.place(x=0, y=0, width=250, height=65)

	instructions = Label(root, background="#ffffff", activebackground="#ffffff",
	                     foreground="#000000", activeforeground="#000000",
	                     text="left arrow key = left mouse button\n"
	                          "right arrow key = right mouse button\n"
	                          "down arrow key = middle mouse button",
	                     font=("Helvetica", 9, "italic", "bold"))
	instructions.place(x=0, y=60, width=250, height=65)

	keyboard.on_press_key("Left", lambda event: s(0), suppress=True)
	keyboard.on_release_key("Left", lambda event: r(0), suppress=True)
	keyboard.on_press_key("Down", lambda event: s(1), suppress=True)
	keyboard.on_release_key("Down", lambda event: r(1), suppress=True)
	keyboard.on_press_key("Right", lambda event: s(2), suppress=True)
	keyboard.on_release_key("Right", lambda event: r(2), suppress=True)

	root.mainloop()

	for key in range(len(stat)):
		if stat[key]:
			match key:
				case 0:
					mouse.release(button="left")
				case 1:
					mouse.release(button="middle")
				case 2:
					mouse.release(button="right")


if __name__ == "__main__":
	main()
