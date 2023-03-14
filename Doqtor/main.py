import matplotlib as mpl
import matplotlib.pyplot as plt
import tkinter as tk

root = tk.Tk()

root.geometry("1250x800")
root.title("Doqtor")

label = tk.Label(root, text="Hello World!", font=("Arial","18"))
label.pack(padx=20,pady=20)

textbox = tk.Text(root, height=3, font=("Arial","16"))
textbox.pack(padx=50,pady=50)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

count = 0
for i in range(2):
    for j in range(3):
        count += 1
        btn1 = tk.Button(buttonframe, text=str(count), font=("Arial","18"))
        btn1.grid(row=i, column=j, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")


anotherbtn = tk.Button(root, text="Test")
anotherbtn.place(x=200,y=200,height=100,width=100)
root.mainloop()