import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from libsarit import cypher, functionalPart, uncypher, makeSquare, cutter


root = tk.Tk()


# ---------------------------------------------------Frames---------------------------------------------------#


base_text = ttk.Frame(root, width=40, height=40).grid(row=0, column=0)
key = ttk.Frame(root, width=40, height=40).grid(row=1, column=0)
buttons_interface = ttk.Frame(root, width=40, height=40).grid(row=2, column=0)
result_text = ttk.Frame(root, width=40, height=40).grid(row=3, column=0)
grid = ttk.Frame(root, width=50, height=50).grid(row=0, column=1)


# ---------------------------------------------------Widgets---------------------------------------------------#


text_label = ttk.Label(base_text, text="Enter a Text >")
key_entry = ttk.Label(key, text="Enter a text key >")
length = ttk.Label(key, text="Enter a length >")
result = ttk.Label(result_text, text="Result : ")

text_entry = ttk.Entry(base_text)
text = text_entry.get()
text = cutter(text, 7)
passWord = ttk.Entry(key, width=25)
key = passWord.get()
key = makeSquare(key)
number = ttk.Entry(key, width=5)
n = number.get()
result_entry = ttk.Entry(result_text, width=30)

breaker = ttk.Button(buttons_interface, text="uncypher", command=cypher(text, key, n))
coder = ttk.Button(buttons_interface, text="cypher", command=cypher(text, key, n))


# ---------------------------------------------------Geometry Managers---------------------------------------------------#


text_label.grid(row=0, column=0)
key_entry.grid(row=1, column=0)
length.grid(row=1, column=2)
result.grid(row=3, column=0)

text_entry.grid(row=0, column=1)
passWord.grid(row=1, column=1)
number.grid(row=1, column=3)
result_entry.grid(row=3, column=1)

breaker.grid(row=2, column=1)
coder.grid(row=2, column=0)

tk.mainloop()