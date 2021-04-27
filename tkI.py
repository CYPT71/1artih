from tkinter import Text, INSERT, Canvas, ttk, Tk
from libsarit import TextCypher, makeSquare
import tkinter.font

root = Tk()

# ---------------------------------------------------Frames---------------------------------------------------#

base_text = ttk.Frame(root)
key = ttk.Frame(root)
buttons_interface = ttk.Frame(root)
result_text = ttk.Frame(root)
grid = ttk.Frame(root)

# ---------------------------------------------------Widgets---------------------------------------------------#

text_label = ttk.Label(base_text, text="Message à chiffrer ou à déchiffrer :")
key_entry = ttk.Label(key, text="Entrer la clé : ")
length = ttk.Label(key, text="Entrer la chaîne : ")
result = ttk.Label(result_text, text="Message obtenu :")
grid_text = ttk.Label(grid, text="La grille obtenue :")

text_entry = Text(base_text, width=60, height=10)
passWord = ttk.Entry(key, width=25)
number = ttk.Entry(key, width=10)
result_entry = Text(result_text, width=60, height=10)

# ---------------------------------------------------Functions----------------------------------------------------------#

#-------------------Grille de lettres------------------#
grille = Canvas(grid, height=250, width=250, bg="white")


def grid_display():
    for i in range(0, 250, 50):
        grille.create_line(i, 0, i, 250)
    for j in range(0, 250, 50):
        grille.create_line(0, j, 250, j)

def generate_grid(e):
    for _ in range(2):
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

uncypherText = ttk.Button(buttons_interface, text="Déchiffrer", command= lambda: text_entry.insert(INSERT, TextCypher(result_entry.get("1.0", "end"), passWord.get(), number.get(), True)))
cypherText = ttk.Button(buttons_interface, text="Chiffrer", command= lambda: result_entry.insert(INSERT, TextCypher(text_entry.get("1.0", "end"), passWord.get(), number.get(), False)))
delete = ttk.Button(buttons_interface, text="Effacer", command= lambda: result_entry.delete("1.0", "end"))

# ---------------------------------------------------Geometry Managers---------------------------------------------------#

base_text.grid(row=0, column=0)
key.grid(row=1, column=0)
buttons_interface.grid(row=2, column=0)
result_text.grid(row=3, column=0)
grid.grid(row=0, column=2, rowspan=3)

text_label.grid(row=0, column=0, sticky='w')
key_entry.grid(row=0, column=0)
length.grid(row=0, column=2)
result.grid(row=0, column=0, sticky='w')
grid_text.grid(row=0, column=0)

text_entry.grid(row=1, column=0, padx=5, pady=5)
passWord.grid(row=0, column=1, padx=(0, 20))
number.grid(row=0, column=3)
result_entry.grid(row=4, column=0, padx=5, pady=5)

cypherText.grid(row=0, column=0)
uncypherText.grid(row=0, column=1)
delete.grid(row=0, column=2)

grille.grid(row=1, column=0, padx=10, pady=5)

generate_grid(None)

root.mainloop()