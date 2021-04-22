from tkinter import Text, INSERT, Canvas, ttk, Tk
from libsarit import TextCypher, makeSquare

root = Tk()

# ---------------------------------------------------Frames---------------------------------------------------#

base_text = ttk.Frame(root)
key = ttk.Frame(root)
buttons_interface = ttk.Frame(root)
result_text = ttk.Frame(root)
grid = ttk.Frame(root)

# ---------------------------------------------------Widgets---------------------------------------------------#

text_label = ttk.Label(base_text, text="Enter a Text >")
key_entry = ttk.Label(key, text="Enter a text key >")
length = ttk.Label(key, text="Enter a length >")
result = ttk.Label(result_text, text="Result > ")
grid_text = ttk.Label(grid, text="La grille de lettres")

text_entry = Text(base_text, width=100, height=10)
passWord = ttk.Entry(key, width=25)
number = ttk.Entry(key, width=10)
result_entry = Text(result_text, width=100, height=10)
result_entry.bind("<Key>", lambda a: "break")

# ---------------------------------------------------Functions----------------------------------------------------------#

#-------------------Grille de lettres------------------#
grille = Canvas(grid, height=250, width=250, bg="white")


def grid_display():
    for i in range(0, 250, 50):
        grille.create_line(i, 0, i, 250)
    for j in range(0, 250, 50):
        grille.create_line(0, j, 250, j)

def generate_grid(e):
    index = 0
    grille.delete("all")
    var = [a for sub in makeSquare(passWord.get()) for a in sub]
    for i in range(25, 250, 50):
        for j in range(25, 250, 50):
            grille.create_text(j, i, text=var[index])
            index += 1
    grid_display()

passWord.bind("<Key>", generate_grid)
passWord.bind("<Motion>", generate_grid)

#-------------------Fonctinalités principales---------------------#

uncypherText = ttk.Button(buttons_interface, text="uncypher", command= lambda: result_entry.insert(INSERT, TextCypher(text_entry.get("1.0", "end"), passWord.get(), number.get(), True)))
cypherText = ttk.Button(buttons_interface, text="cypher", command= lambda: result_entry.insert(INSERT, TextCypher(text_entry.get("1.0", "end"), passWord.get(), number.get(), False)))
delete = ttk.Button(buttons_interface, text="delete", command= lambda: result_entry.delete("1.0", "end"))

# ---------------------------------------------------Geometry Managers---------------------------------------------------#

base_text.grid(row=0, column=0)
key.grid(row=1, column=0)
buttons_interface.grid(row=2, column=0)
result_text.grid(row=3, column=0)
grid.grid(row=0, column=2, rowspan=3)

text_label.grid(row=0, column=0)
key_entry.grid(row=0, column=0)
length.grid(row=0, column=2)
result.grid(row=0, column=0)
grid_text.grid(row=0, column=0)

text_entry.grid(row=0, column=1, ipadx=10)
passWord.grid(row=0, column=1)
number.grid(row=0, column=3)
result_entry.grid(row=0, column=1)

cypherText.grid(row=0, column=0)
uncypherText.grid(row=0, column=1)
delete.grid(row=0, column=2)

grille.grid(row=1, column=0)

generate_grid(None)

root.mainloop()