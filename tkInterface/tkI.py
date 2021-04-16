import tkinter as tk


root = tk.Tk()

tk.Label(root, text="Enter a Text >").grid(row=0)
tk.Label(root, text="Enter a text key >").grid(row=1)
tk.Label(root, text="enter a number key >").grid(row=1, column=2)
tk.Label(root, text="Result : ").grid(row=2)

text = tk.Entry(root)
text.grid(row=0, column=1, width=100, height=100)

passWord = tk.Entry(root, width=50)
passWord.grid(row=1, column=1)

number = tk.Entry(root)
number.grid(row=1, column=3)

tk.Button(root, text="cypher").grid(row=2)
tk.Button(root, text="uncypher").grid(row=2, column=1)
# breaker = tk.Button(root, text="cypher").grid(row=2, column=3)



tk.mainloop()

