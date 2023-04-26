import tkinter as tk
import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt

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
            command= lambda: self.traingle_inequality(self.side1,self.side2,self.side3)
        )
        self.button.pack(
            padx=25,
            pady=25
        )

        self.txt = ctk.CTkTextbox(
            master=self.sides,
            width=200,
            height=50
        )

        self.txt.pack(
            padx=25,
            pady=25
        )
        
    def traingle_inequality(self,side1,side2,side3):
        try:
            sides= sorted([float(side1.get()),float(side2.get()),float(side3.get())])
            a = sides[0]
            b = sides[1]
            c = sides[2]
            self.txt.delete(1.0, ctk.END)
            if a + b > c:
                self.txt.insert(1.0,"Triangle is possible")
                
                angle1 = np.arccos(((a**2)+(c**2)-(b**2))/(2*a*c))
                angle2 = np.arccos(((b**2)+(c**2)-(a**2))/(2*b*c))
                gradient1 = np.tan(angle1)
                gradient2 = -np.tan(angle2)

                x1 = np.arange(0,c,0.01)
                y1 = [0 for i in range(len(x1))]
                x2 = np.arange(0,a,0.01)
                y2 = gradient1*x2
                if b != c:
                    x3 = np.arange(b,c,0.01)
                    y3 = gradient2*x3
                else:
                    y3 = np.arange(0,gradient2,0.01)
                    x3 = [b for i in range(len(y3))]
                
                plt.plot(x1,y1)
                plt.plot(x2,y2)
                plt.plot(x3,y3)
                plt.show()
            else:
                self.txt.insert(1.0,"Triangle is not possible")

        except ValueError:
            print("Please enter 3 valid sides")
    


if __name__ == "__main__":
    root = App()
    root.mainloop()

