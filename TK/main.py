import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("Dark")

ctk.set_default_color_theme("green")


root = ctk.CTk()
root.geometry("800x600")
root.title("Fun Testing")

        
button = ctk.CTkButton(
    master = root,
    text = "Press Me",
    command= lambda: print("Don't Press me"),
    fg_color="#E80",
    hover_color="#E50"
    )

button.place(
    relx=0.5,
    rely=0.5,
    anchor = ctk.CENTER
    )

root.mainloop()