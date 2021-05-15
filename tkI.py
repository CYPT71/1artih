from tkinter import Text, INSERT, Canvas, ttk, Tk
from libsarit import TextCypher, makeSquare
import tkinter.font
import warnings

root = Tk()
root.title("1ARI-project Colon program")
root.resizable(False, False)
root.attributes('-alpha',1)
try:
    root.iconbitmap(r"./dcode.ico")
except:
    warnings.warn("Caution you don't have any title bar icon")
# ---------------------------------------------------Frames---------------------------------------------------#

base_text = ttk.Frame(root)
key = ttk.Frame(root)
buttons_interface = ttk.Frame(root)
result_text = ttk.Frame(root)
grid = ttk.Frame(root)
infos = ttk.Frame(root)

# ---------------------------------------------------Widgets---------------------------------------------------#

text_label = ttk.Label(base_text, text="Clear text >")
key_entry = ttk.Label(key, text="Enter a text key >")
length = ttk.Label(key, text="Enter a length >")
result = ttk.Label(result_text, text="Cypher text > ")
grid_text = ttk.Label(grid, text="Grid of letters")

text_entry = Text(base_text, width=60, height=10)
passWord = ttk.Entry(key, width=25)
number = ttk.Entry(key, width=10)
result_entry = Text(result_text, width=60, height=10)

informations = ttk.Label(infos, text="Use 'Arrow up' to uncypher and 'Arrow down' to\n cypher, you must enter a text key and a length.")

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

passWord.bind("<KeyRelease>", generate_grid)


#-------------------Fonctionnalités de mise en forme------------------#
def deleter():
    result_entry.delete("1.0", "end")
    text_entry.delete("1.0", "end")
    passWord.delete(0, "end")
    number.delete(0, "end")
    generate_grid(None)

def cypher(e = None):
    result_entry.delete("1.0", "end")
    result_entry.insert(INSERT, TextCypher(text_entry.get("1.0", "end"), passWord.get(), number.get(), False))

def uncypher(e = None):
    text_entry.delete("1.0", "end")
    text_entry.insert(INSERT, TextCypher(result_entry.get("1.0", "end"), passWord.get(), number.get(), True))

#-------------------Fonctinalités principales---------------------#

uncypherText = ttk.Button(buttons_interface, text="uncypher", command= uncypher )
cypherText = ttk.Button(buttons_interface, text="cypher", command= cypher)
delete = ttk.Button(buttons_interface, text="delete", command= deleter)

root.bind("<Up>", uncypher)
root.bind("<Down>", cypher)
# ---------------------------------------------------Geometry Managers---------------------------------------------------#

base_text.grid(row=0, column=0)
key.grid(row=1, column=0)
buttons_interface.grid(row=2, column=0)
result_text.grid(row=3, column=0)
grid.grid(row=0, column=1)
infos.grid(row=3, column=1)

text_label.grid(row=0, column=0, sticky='w')
key_entry.grid(row=0, column=0)
length.grid(row=0, column=2)
result.grid(row=0, column=0, sticky='w')
grid_text.grid(row=0, column=0)

text_entry.grid(row=1, column=0, padx=5, pady=5)
passWord.grid(row=0, column=1, padx=(0, 20))
number.grid(row=0, column=3)
result_entry.grid(row=4, column=0, padx=5, pady=5)
informations.grid(row=0, column=1)

cypherText.grid(row=0, column=0)
uncypherText.grid(row=0, column=1)
delete.grid(row=0, column=2)

grille.grid(row=1, column=0, padx=10, pady=5)

generate_grid(None)

root.mainloop()
