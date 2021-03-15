import time
import pyautogui as pygui
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'C:\\Users\\Ogwumike\\Documents\\Joe\\Online Training\\Python\\Py_Programs\\screenshot\\savedscreens\\{}.png'.format(name)
    # time.sleep(3) instant screenshot
    img = pygui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text='Take Screenshot',
    command=screenshot
)
button.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text='CLOSE',
    command=quit
)
close.pack(side=tk.LEFT)

root.mainloop()

