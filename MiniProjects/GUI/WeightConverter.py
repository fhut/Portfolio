import tkinter as tk


window = tk.Tk()


units_to_convert = tk.Entry()
convert = tk.Button(text="Convert",
                    background="grey",
                    foreground="yellow",
                    width=15,
                    height=3
                    )
converted = units_to_convert.get() * 5
convert.text = converted
convert.pack()
units_to_convert.pack()
window.mainloop()

