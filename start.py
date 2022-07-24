from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculator Portable")
root.geometry("400x600")

def calculate():
    try:
        result = str(int(textbox_1.get()) + int(textbox_2.get()))
        result_label.configure(root, text="Result : " + result)
    except ValueError as e:
        messagebox.showwarning("Alert", e)

myLabel = Label(root, text="Silakan masukkan angka")
myLabel.pack()

textbox_1 = Entry(root, text="Angka Pertama:", width=50)
textbox_1.pack()

myLabel = Label(root, text="+")
myLabel.pack()

textbox_2 = Entry(root, text="Angka Kedua:", width=50)
textbox_2.pack()

submit = Button(root, text="Submit", command=calculate)
submit.pack()

result_label = Label(root, text="Result : ")
result_label.pack()

root.mainloop()