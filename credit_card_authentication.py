from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as mbox 

root=Tk()
root.title("Credit Card Authentication")
root.geometry("600x400")

root.configure(background="gold")

input_box = Entry()
input_box.place(relx=0.5, rely=0.3, anchor = CENTER)

img=ImageTk.PhotoImage(Image.open ("credit.jpg"))
label = Label(root, image=img)


def authentication():
    error=0
    try:
        input_value = int(input_box.get())
        
    except(ValueError):
        mbox.showinfo("Alert","Credit card not accepted. Please Put Valid Pincode")
        error=1
    if error==0:
        mbox.showinfo("Alert","Credit card accepted.")

btn = Button(root, text = "check credit card", command = authentication)
btn.place(relx=0.5, rely=0.4, anchor = CENTER)
label.place(relx=0.5, rely=0.7, anchor = CENTER)

root.mainloop()