import tkinter as tk
import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

ctk.set_appearance_mode("Dark")

ctk.set_default_color_theme("green")


class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,**kwargs)



class App(ctk.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("800x600")
        self.title("Shape Thing")
        self.resizable(width=False,height=False)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(5, weight=1)

        self.sides = Frame(
            master=self,
            width=200,
            height=550,
            border_width=3,
            fg_color="#85F"
        )

        self.sides.grid(
            row=0,
            column=0,
            padx=20,
            pady=20,
            sticky="nsew"
        )


        self.side1 = ctk.CTkEntry(
            master=self.sides,
            placeholder_text="First Side",
            width=200,
            height=50,
            border_width=2,
            corner_radius=10
        )
        self.side1.pack(
            padx=25,
            pady=25
        )

        self.side2 = ctk.CTkEntry(
            master=self.sides,
            placeholder_text="Second Side",
            width=200,
            height=50,
            border_width=2,
            corner_radius=10
        )
        self.side2.pack(
            padx=25,
            pady=25
        )

        self.side3 = ctk.CTkEntry(
            master=self.sides,
            placeholder_text="Third Side",
            width=200,
            height=50,
            border_width=2,
            corner_radius=10
        )
        self.side3.pack(
            padx=25,
            pady=25
        )

        

        self.button = ctk.CTkButton(
            master=self.sides,
            text="Calculate if Triangle is Possible",
            width=200,
            height=50,
            border_width=3,
            fg_color="#85F",
            border_color="black",
            hover_color="#80D",
            command= lambda: self.traingle_inequality(self.side1,self.side2,self.side3)
        )
        self.button.pack(
            padx=25,
            pady=25
        )

        self.txt = ctk.CTkTextbox(
            master=self.sides,
            width=200,
            height=100
        )

        self.txt.pack(
            padx=25,
            pady=25
        )

        self.images = Frame(
                    master = self,
                    height = 500,
                    width = 500,
                    border_width=3,
                    fg_color = "#85F"
                )

        self.images.grid(
            row=0,
            column=2       
                )
        
    def traingle_inequality(self,side1,side2,side3):
        try:
            sides= sorted([float(side1.get()),float(side2.get()),float(side3.get())])
            a = sides[0]
            b = sides[1]
            c = sides[2]
            self.txt.delete(1.0, ctk.END)
            if a + b > c:
                self.txt.insert(1.0,"Triangle is Possible\n")
                if (a == b) and (a == c):
                    self.txt.insert(2.0,"Triangle is Equilateral\nTriangle is Isosceles\n")
                elif ((a == b) and (a != c)) or ((a == c) and (a != b)) or ((b == c) and (b != a)):
                    self.txt.insert(2.0,"Triangle is Isosceles\n")
                else:
                    self.txt.insert(3.0, "Triangle is Scalene\n")

                if a**2 + b**2 == c**2: self.txt.insert(2.0, "Triangle is Right-Angled\n")
 
                x = [0,a,((a**2)+(c**2)-(b**2))/(2*a),0]
                y = [0,0,np.sqrt((c**2)-(((a**2)+(c**2)-(b**2))/(2*a))**2),0]

                plt.clf()
                plt.plot(x,y)
                plt.grid(False)
                plt.axis("off")
                plt.savefig(r"TK\triangle.png")

                self.img = ctk.CTkImage(
                    light_image= Image.open(r"TK\Triangle\triangle.png"),
                    size=(500,500)
                )
                self.triangle = ctk.CTkButton(
                    master = self.images,
                    image=self.img,
                    width = 500,
                    height = 500,
                    anchor=ctk.CENTER,
                    fg_color="#FFF",
                    hover_color="#FFF"
                )

                self.triangle.place(
                    relx=0.5,
                    rely=0.5,
                    anchor=ctk.CENTER
                )

            else:
                self.txt.insert(1.0,"Triangle is not possible")

        except ValueError:
            self.txt.delete(1.0, ctk.END)
            self.txt.insert(1.0,"Please enter 3 valid sides\n")
    


if __name__ == "__main__":
    root = App()
    root.mainloop()

