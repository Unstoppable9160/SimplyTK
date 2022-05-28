import tkinter as tk


def Button(window, text: str, backgroundColour: str = None, foregroundColour: str = None, activeBackgroundColour: str = None, activeForegroundColour: str = None, width: int = 10, height: int = 10):
    butt = tk.Button(window, text=f"{text}", width=width, height=height, bg=backgroundColour,
                     fg=foregroundColour, activebackground=activeBackgroundColour, activeforeground=activeForegroundColour)
    butt.pack()
