from tkinter import Text, INSERT, Canvas, ttk, Tk, Menu
from tkinter.constants import END
import tkinter.font as tkFont
from tkinter.filedialog import asksaveasfile, askopenfilename
import json

from libsarit import TextCypher, makeSquare
import tkinter.font
import warnings

root = Tk()
root.title("1ARI-project Colon program")
root.resizable(False, False)
root.attributes('-alpha',1)
try:
    root.iconbitmap(r"./assets/dcode.ico")
except:
    warnings.warn("Caution you don't have any title bar icon")


# ---------------------------------------------------Frames---------------------------------------------------#

base_text = ttk.Frame(root)
key = ttk.Frame(root)
buttons_interface = ttk.Frame(root)
result_text = ttk.Frame(root)
grid = ttk.Frame(root)
infos = ttk.Frame(root)

Font = tkFont.Font(family="Consolas", size=15)

# ---------------------------------------------------Widgets---------------------------------------------------#


root.option_add("+tearOff", False)
menubar = Menu(root)
root.config(menu = menubar)
file = Menu(menubar)
file.add_command(label = "Exit", command = root.destroy)

menubar.add_cascade(menu = file, label = "File")

text_label = ttk.Label(base_text, text="Clear text >")
key_entry = ttk.Label(key, text="Enter a text key >")
length = ttk.Label(key, text="Enter a length >")
result = ttk.Label(result_text, text="Cypher text > ")
grid_text = ttk.Label(grid, text="Grid of letters")
informations = ttk.Label(infos, text="Use 'Arrow up'\n to uncypher\n and\n 'Arrow down'\n to cypher.\n")
informations.configure(font=Font, width=20)

text_entry = Text(base_text, width=60, height=10, font=Font)
passWord = ttk.Entry(key, width=25, font=Font)
number = ttk.Entry(key, width=10, font=Font)
result_entry = Text(result_text, width=60, height=10, font=Font)


# appeler la police 
settings = Menu(menubar)
menubar.add_cascade(menu = settings, label = "Settings")

policeMenu = Menu(settings)
settings.add_cascade(menu=policeMenu, label = "Police")

fontList = tkFont.families()

fontIndex = 0
size = 12

def changePolice(index):
    global fontIndex
    fontIndex = index
    text_entry.configure(font=(fontList[fontIndex], size))
    passWord.configure(font=(fontList[fontIndex], size))
    number.configure(font=(fontList[fontIndex], size))
    result_entry.configure(font=(fontList[fontIndex], size))

def changeSize(plus=True):
    global size
    size = size + 7 if plus else size - 7
    changePolice(fontIndex)

for i, font in enumerate(fontList):
    policeMenu.add_command(label=font, command= lambda i=i: changePolice(i))

settings.add_command(label="More", command= lambda : changeSize())
settings.add_command(label="Less", command= lambda : changeSize(plus=False))

root.bind("<Control-Up>", changeSize)
root.bind("<Control-Down>", lambda e: changeSize(plus=False))

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

#-------------------Fonctinalitées principales---------------------#

uncypherText = ttk.Button(buttons_interface, text="uncypher", command= uncypher )
cypherText = ttk.Button(buttons_interface, text="cypher", command= cypher)
delete = ttk.Button(buttons_interface, text="delete", command= deleter)

root.bind("<Up>", uncypher)
root.bind("<Down>", cypher)

#-------------------Fonctinalitées bonus---------------------#

def set_key(text):
    passWord.delete(0, END)
    passWord.insert(0, text)

def set_spacer(text):
    number.delete(0, END)
    number.insert(0, text)

def loadFile():
    file = askopenfilename(filetypes=[("json files", "*.json")], defaultextension = [("json files", "*.json")])
    data = None
    if file.split("/")[-1].endswith(".json"):
        with open(file, "r+") as jsonFile:
            data = json.load(jsonFile)

    if data is not None:
        set_key(data["key"])
        text_entry.replace("1.0", "end", data["text"])
        result_entry.replace("1.0", "end", data["cypher"])
        set_spacer(data["spacer"])

    generate_grid(e=None)

def saveFile():
    file = asksaveasfile(filetypes=[("json files", "*.json")], defaultextension = [("json files", "*.json")])
    encoding = file.encoding
    file = file.name
    
    if file.split("/")[-1].endswith(".json"):
        data = {
            "key": passWord.get(),
            "text": text_entry.get("1.0", "end"),
            "cypher": result_entry.get("1.0", "end"),
            "spacer": number.get(),
        }

        with open(file, "w+") as jsonFile:
            json.dump(data, jsonFile, indent=4)

file.add_command(label = "Load", command = loadFile)
file.add_command(label = "Save", command = saveFile)

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
