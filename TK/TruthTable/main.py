import tkinter as tk
import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,**kwargs)

class Entry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master,**kwargs)

class CombBox(ctk.CTkComboBox):
    def __init__(self, master, **kwargs):
        super().__init__(master,**kwargs)

class OptBox(ctk.CTkOptionMenu):
    def __init__(self, master, **kwargs):
        super().__init__(master,**kwargs)

class Button(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master,**kwargs)

class TxtBox(ctk.CTkTextbox):
    def __init__(self, master, **kwargs):
        super().__init__(master,**kwargs)

class App(ctk.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("800x400")
        self.title("Truth Table")
        self.resizable(width=False,height=False)


        self.grid_rowconfigure((0,1), weight=1)
        self.grid_columnconfigure((0,1), weight=2)

        self.inputs = Frame(
            master=self,
            width=500,
            height=450,
            border_width=3,
            fg_color="#108"
        )
        self.inputs.grid(
            row=0,
            column=0,
            padx=15,
            pady=15,
            sticky="new"
        )
        
        self.expression = Entry(
            master=self.inputs,
            placeholder_text="Enter Boolean Expression",
            width=350,
            height=50,
            border_width=2,
            corner_radius=10
        )

        self.expression.pack(
            padx=10,
            pady=10
        )

        self.truth_table = None

if __name__ == "__main__":
    root = App()
    root.mainloop()