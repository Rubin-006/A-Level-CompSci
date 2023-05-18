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
        self.geometry("800x600")
        self.title("Mortgage Calculator")
        self.resizable(width=False,height=False)


        self.grid_rowconfigure((0,1), weight=1)
        self.grid_columnconfigure((0,1), weight=2)

        self.inputs = Frame(
            master=self,
            width=500,
            height=450,
            border_width=3,
            fg_color="#FA0"
        )
        self.inputs.grid(
            row=0,
            column=0,
            padx=15,
            pady=15,
            sticky="new"
        )

        self.aprc = Entry(
            master=self.inputs,
            placeholder_text="Enter Annual Interest Rate",
            width=350,
            height=50,
            border_width=2,
            corner_radius=10
        )
        
        self.aprc.pack(
            padx=10,
            pady=15
        )

        self.start_bal = Entry(
            master=self.inputs,
            placeholder_text="Enter Principle Starting Balance of Loan",
            width=350,
            height=50,
            border_width=2,
            corner_radius=10
        )

        self.start_bal.pack(
            padx=10,
            pady=(0,15)
        )

        self.terms = Entry(
            master=self.inputs,
            placeholder_text="Enter number of terms you want to pay",
            width=350,
            height=50,
            border_width=2,
            corner_radius=10
        )

        self.terms.pack(
            padx=10,
            pady=(0,15)
        )


        self.options = Frame(
            master=self,
            width=500,
            height=450,
            border_width=3,
            fg_color="#F40"
        )

        self.options.grid(
            row=0,
            column=1,
            padx=15,
            pady=15,
            sticky="new"
        )


        self.term_types = OptBox(
            master=self.options,
            width=200,
            height=50,
            corner_radius=10,
            values=["Monthly","Weekly","Daily"],
            fg_color="#CF0",
            button_color="#CF0",
            dropdown_hover_color="#CF0",
            dropdown_fg_color="#CF0",
            dropdown_text_color="#333",
            text_color="#333"
        )

        self.term_types.pack(
            padx=20,
            pady=(20,10),
            anchor="center"
        )

        self.button = Button(
            master=self.options,
            text="Calculate Payment",
            width=200,
            height=50,
            fg_color="#CF0",
            hover_color="#CF0",
            text_color="#333",
            command= lambda: self.calc(self.aprc,self.start_bal,self.terms,self.term_types)
        )

        self.button.pack(
            padx=20,
            pady=(10,20),
            anchor="center",
            side="top"
        )

        self.txt = TxtBox(
            master=self.options,
            width=300,
            height=150
        )
        self.txt.pack(
            padx=20,
            pady=20,
            anchor="center"
        )


    def calc(self,aprc,money,terms,term_type):
        self.txt.delete(1.0, ctk.END)
        aprc = float(aprc.get())/12
        money = float(money.get())
        terms = int(terms.get())
        term_type= term_type.get()

        self.types = {"Monthly":12,"Weekly":52,"Daily":365}
        
        terms = terms * self.types[term_type]
        payment = money*((aprc*((1+aprc)**terms))/(((1+aprc)**terms)-1))

        match term_type:
            case "Monthly":
                self.type = "Month"
            case "Weekly":
                self.type = "Week"
            case "Daily":
                self.type = "Day"

        self.txt.insert(1.0,f"You have to pay £{round(payment,2)} every {self.type}")

if __name__ == "__main__":
    root = App()
    root.mainloop()