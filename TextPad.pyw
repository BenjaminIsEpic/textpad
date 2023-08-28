import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *
print("Initializing...")
def change_color():
    color = colorchooser.askcolor(title="Select Text Color")
    text_area.config(fg=color[1])
def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))
def new_file():
    window.title("Untitled.tdf")
    text_area.delete(1.0, END)
def open_file():
    file = askopenfilename(defaultextension=".tdf", file=[("TextPad Document Files", "*.tdf"),
                                                          ("All Files", "*.*")])
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, "r")

        text_area.insert(1.0, file.read())

    except:
        window.title("Untitled.tdf")
        showerror("File Operation Error", "Unable to open file.")

    finally:
        file.close()

def saveas_file():
    file = filedialog.asksaveasfilename(initialfile='Untitled.tdf',
                                        defaultextension=".dedf",
                                        filetypes=[("TextPad Document Files", "*.tdf"),
                                                   ("All Files", "*.*")])
    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except:
            showerror("File Operation Error", "Unable to save file.")

        finally:
          file.close()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def sfs():
    frame.grid()

def about():
    showinfo("About TextPad", "TextPad Version 1.00. TM & © 2023 BenjaminIsEpic.")

def quit():
    window.destroy()
print("Done")
window = Tk()
window.title("Untitled.tdf")
file = None
window_width = 500
window_height = 500
screen_witdh = window.winfo_screenwidth()
screen_witdh = window.winfo_screenheight()

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("10")

text_area = Text(window,font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
menu_bar = Menu(window)
window.config(menu=menu_bar)

frame = Frame(window)
color_button = Button(frame, text="Change Color", command=change_color)
color_button.grid(row=0, column=0)
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)
size_box =Spinbox(frame, from_=1, to=76, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

file_menu = Menu(menu_bar, tearoff=0) 
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As...", command=saveas_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

font_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Font", menu=font_menu)
font_menu.add_command(label="Show Font Strip", command=sfs)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()
