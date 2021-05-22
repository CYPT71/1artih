from tkinter import Label, Text, INSERT, Canvas, ttk, Tk, Menu, Button, Toplevel, END, filedialog, ACTIVE, NORMAL
import tkinter.font as tkFont
import json
from libsarit import TextCypher, make_square
from voice_to_text import speech_to_text

root = Tk()
root.title("1ARI-project Colon program")
root.resizable(False, False)
root.attributes('-alpha',0.94)
# root.overrideredirect(True)
# root.state("iconic")

lastClickX = 0
lastClickY = 0

def save_last_click_pos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))

# root.bind('<Button-1>', save_last_click_pos)
# root.bind('<B1-Motion>', dragging)
# ---------------------------------------------------Frames---------------------------------------------------#

base_text = ttk.Frame(root)
key = ttk.Frame(root)
buttons_interface = ttk.Frame(root)
result_text = ttk.Frame(root)
grid = ttk.Frame(root)
infos = ttk.Frame(root)

Font = tkFont.Font(family="Comic Sans MS", size=15)

# ---------------------------------------------------Paramètres menu---------------------------------------------------#

menubar = Menu(root, tearoff=0)
root.config(menu = menubar)
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label = u"\u2717", command = root.destroy)
menubar.add_cascade(menu = file, label = u"\U0001F4C1")

policeMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(menu=policeMenu, label = u"\u2699")

fontList = tkFont.families()
fontIndex = 0
size = 10
taille = ttk.Entry(buttons_interface, width=5)

def change_police(index):
    global fontIndex
    fontIndex = index
    informations.configure(font=(fontList[fontIndex], size if size > 16 else 16))
    for elem in [text_entry, passWord, number, result_entry, taille, text_label, \
        key_entry, length, result, uncypherText, cypherText, more, less, delete, grid_text]:
        elem['font'] = tkFont.Font(family=fontList[fontIndex], size=size)

    generate_grid(e=None)

def change_size(plus=True):
    global size
    size = int(t)%15 if (t := taille.get()).isdigit() else ((size + 5 if plus and size < 18 else size - 5) if size > 7 else 16)
    change_police(fontIndex)
    taille.delete(0, END)

for i, font in enumerate(fontList):
    policeMenu.add_command(label=font, command= lambda i=i: change_police(i))


root.bind("<Control-Up>", change_size)
root.bind("<Control-Down>", lambda e: change_size(plus=False))
taille.bind("<Return>", change_size)

# ---------------------------------------------------Widgets---------------------------------------------------#

text_label = ttk.Label(base_text, text=u"Clear text \U0001F513")
key_entry = ttk.Label(key, text=u"Enter a text key \u261E")
length = ttk.Label(key, text=u"Enter a length \u261E")
result = ttk.Label(result_text, text=u"Cypher text \U0001F512")
grid_text = ttk.Label(grid, text=u"Key Grid \u26BF")
informations = ttk.Label(infos, text="Use " + u"\U0001F80B" + " to cypher\n and " + u"\U0001F809" + " to uncypher.")
informations.configure(font=("Consolas", 16))

text_entry = Text(base_text, width=60, height=10, font=Font)
passWord = ttk.Entry(key, width=25, font=Font)
number = ttk.Entry(key, width=10, font=Font)
result_entry = Text(result_text, width=60, height=10, font=Font)

# vocal implementation

def text_reco():
    text_vocal ['state'] = ACTIVE
    
    
    text = speech_to_text()

    text_entry.replace("1.0", "end", text)
    text_vocal['state'] = NORMAL

def key_reco():
    key_vocal['state'] = ACTIVE

    key = speech_to_text()

    passWord.delete(0, "end")
    passWord.insert(0, key)

text_vocal = Button(base_text, text=u"\U0001F399", command=lambda : text_reco())
key_vocal = Button(key, text=u"\U0001F399", command=lambda : key_reco())
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
        var = [a for sub in make_square(passWord.get()) for a in sub]
        for i in range(25, 250, 50):
            for j in range(25, 250, 50):
                grille.create_text(j, i, text=var[index], font=(fontList[fontIndex], size))
                index += 1
        grid_display()

passWord.bind("<KeyRelease>", generate_grid)

#-------------------Fonctionnalités de mise en forme------------------#

def deleter(e = None):
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

uncypherText = Button(buttons_interface, text="uncypher", command= uncypher )
cypherText = Button(buttons_interface, text="cypher", command= cypher)
delete = Button(buttons_interface, text=u"\U0001F5D1", command= deleter)
more = Button(buttons_interface, text=u"\u25B2", command= lambda : change_size())
less = Button(buttons_interface, text=u"\u25BC", command= lambda : change_size(plus=False))

root.bind("<Up>", uncypher)
root.bind("<Down>", cypher)
root.bind("<Control-BackSpace>", deleter)

#-------------------Fonctinalités bonus---------------------#

def set_key(text):
    passWord.delete(0, END)
    passWord.insert(0, text)

def set_spacer(text):
    number.delete(0, END)
    number.insert(0, text)

format = [("json files", "*.json")]
def load_file(e=None):
    file = filedialog.askopenfilename(filetypes=format, defaultextension = format)
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

def save_file(e=None):
    file = filedialog.asksaveasfile(filetypes=format, defaultextension = format)
    if file == None:
        return
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

file.add_command(label = u"\U0001F5C1 Open", command = load_file)
file.add_command(label = u"\U0001F5AB Save", command = save_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-o>", load_file)
root.bind("<Control-q>", lambda e: root.destroy())

"""

def fun(e):
    window = Toplevel(root)
    window.title("New Window")
    window.lift(root)

    Label(window, text=(u"\u262E \u262E \u262E \u262E \n \u262E \u262E \u262E \u262E \n \u262E \u262E \u262E \u262E \n"), font=("Comic Sans MS", 150)).pack()

informations.bind("<1>", fun)

"""
# ---------------------------------------------------Geometry Managers---------------------------------------------------#

base_text.grid(row=0, column=0)
key.grid(row=1, column=0)
buttons_interface.grid(row=2, column=0)
result_text.grid(row=3, column=0)
grid.grid(row=0, column=1)
infos.grid(row=3, column=1)

text_label.grid(row=0, column=0, sticky='w')
text_vocal.grid(row=0, column=1)
key_vocal.grid(row=1, column=0)
key_entry.grid(row=0, column=0, padx=30)
length.grid(row=0, column=2)
result.grid(row=0, column=0, sticky='w')
grid_text.grid(row=0, column=0)

text_entry.grid(row=1, column=0, padx=5, pady=5)

passWord.grid(row=0, column=1, padx=15, pady=15)
number.grid(row=0, column=3, padx=15, pady=15)
taille.grid(row=0, column=4, padx=15, pady=15)

result_entry.grid(row=4, column=0, padx=15, pady=15)
informations.grid(row=0, column=1, padx=15, pady=15)

cypherText.grid(row=0, column=0, padx=5, pady=5)
uncypherText.grid(row=0, column=1, padx=5, pady=5)
delete.grid(row=0, column=2, padx=5, pady=5)
less.grid(row=0, column=3, padx=5, pady=5)
more.grid(row=0, column=5, padx=5, pady=5)

grille.grid(row=1, column=0, padx=15, pady=15)

generate_grid(None)

root.mainloop()
