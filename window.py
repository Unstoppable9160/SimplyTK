import tkinter as tk


def window(title: str, width: int = 500, height: int = 300, pathToIcon: str = None, icontype: str = None):
    """
        This function creates a simple tkinter window with a specific width height and title
    """
    root = tk.Tk(className=f"{title}")
    root.geometry(f"{width}x{height}")
    if pathToIcon != None:
        if icontype != "ico":
            root.tk.call('wm', 'iconphoto', root._w,
                         tk.PhotoImage(file=f"{pathToIcon}"))
        else:
            root.iconbitmap(f"{pathToIcon}")
    return root
