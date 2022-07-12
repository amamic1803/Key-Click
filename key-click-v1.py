import mouse
from tkinter import *
import sys
import os
import keyboard


def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except AttributeError:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def s(event):
	global stat
	if not stat:
		stat = True
		mouse.press(button="left")

def r(event):
	global stat
	stat = False
	mouse.release(button="left")

def main():
	global stat
	stat = False

	root = Tk()
	root.resizable(False, False)
	root.geometry(f"250x100+{root.winfo_screenwidth() // 2 - 125}+{root.winfo_screenheight() // 2 - 50}")
	root.title("Key-Click")
	root.iconbitmap(resource_path("key-click-icon.ico"))
	root.config(background="#ffffff")

	title = Label(root, background="#ffffff", activebackground="#ffffff", foreground="#000000", activeforeground="#000000", text="Key-Click", font=("Helvetica", 23, "italic", "bold"))
	title.place(x=0, y=0, width=250, height=65)

	instructions = Label(root, background="#ffffff", activebackground="#ffffff", foreground="#000000", activeforeground="#000000", text="Right arrow acting as left mouse button", font=("Helvetica", 9, "italic", "bold"))
	instructions.place(x=0, y=65, width=250, height=35)

	keyboard.on_press_key("Right", s, suppress=True)
	keyboard.on_release_key("Right", r, suppress=True)

	root.mainloop()
	if stat:
		mouse.release(button="left")


if __name__ == "__main__":
	main()
