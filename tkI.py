import tkinter as tk
from tkinter import *
from tkinter import ttk
from libsarit import TextCypher


root = tk.Tk()

# ---------------------------------------------------Frames---------------------------------------------------#

base_text = ttk.Frame(root, width=40, height=40)
key = ttk.Frame(root, width=40, height=40)
buttons_interface = ttk.Frame(root, width=40, height=40)
result_text = ttk.Frame(root, width=40, height=40)
grid = ttk.Frame(root, width=50, height=50)

# ---------------------------------------------------Widgets---------------------------------------------------#

text_label = ttk.Label(base_text, text="Enter a Text >")
key_entry = ttk.Label(key, text="Enter a text key >")
length = ttk.Label(key, text="Enter a length >")
result = ttk.Label(result_text, text="Result : ")

text_entry = Text(base_text, width=100)
passWord = ttk.Entry(key, width=25)
number = ttk.Entry(key, width=10)
result_entry = Text(result_text, width=100)

# ---------------------------------------------------Create the data to cypher and uncypher----------------------#

uncypherText = ttk.Button(buttons_interface, text="uncypher", command= lambda: result_entry.insert(INSERT, TextCypher(text_entry.get("1.0", "end"), passWord.get(), number.get(), True)))
cypherText = ttk.Button(buttons_interface, text="cypher", command= lambda: result_entry.insert(INSERT, TextCypher(text_entry.get("1.0", "end"), passWord.get(), number.get(), False)))
delete = ttk.Button(buttons_interface, text="delete", command= lambda: result_entry.delete("1.0", "end"))

# ---------------------------------------------------Geometry Managers---------------------------------------------------#

base_text.grid(row=0, column=0)
key.grid(row=1, column=0)
buttons_interface.grid(row=2, column=0)
result_text.grid(row=3, column=0)
grid.grid(row=0, column=2)

text_label.grid(row=0, column=0)
key_entry.grid(row=1, column=0)
length.grid(row=1, column=2)
result.grid(row=3, column=0)

text_entry.grid(row=0, column=1, columnspan=3)
passWord.grid(row=1, column=1)
number.grid(row=1, column=3)
result_entry.grid(row=3, column=1)

cypherText.grid(row=2, column=0)
uncypherText.grid(row=2, column=1)
delete.grid(row=2, column=2)

tk.mainloop()