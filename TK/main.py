import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("Dark")

ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("800x600")
root.title("Shape thing")


def shape(choice):
    sides = []
    if choice == "Triangle":

        l1 = ctk.CTkLabel(master=root, text="Side 1")
        l1.grid(padx=40)
        s1 = ctk.CTkEntry(master=root)
        s1.grid(padx=40,pady=40)

    elif choice == "Rectangle":
        print(4)
    elif choice == "Pentagon":
        print(5)




shapes = ctk.CTkOptionMenu(
    master=root,
    fg_color="#E80",
    values=["Triangle","Rectangle","Pentagon"],
    command=shape
)
shapes.place(
    relx=0.05,
    rely=0.05,
    anchor=ctk.NW
)

root.mainloop()

