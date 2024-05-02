import customtkinter 
from customtkinter import *


root = customtkinter.CTk()
root.geometry('400x400')
root.title("Merdas")
root.maxsize(400, 400)
root.minsize(400, 400)
fonte = CTkFont("JetBrains", 22)

def ver():
    root2 = CTkToplevel()
    root2.geometry('400x400')
    root2.title("Merdas")
    root2.maxsize(400, 400)
    root2.minsize(400, 400)
    otario = fellas.get()
    nome = CTkLabel(root2, text=otario, font=fonte)
    nome.configure()
    nome.place(relx=0.5, y = 15, anchor="center")
    nome = CTkLabel(root2, image=imagem)
    nome.configure()
    nome.place(relx=0.5, y = 200, anchor="center")
    
    











opcoes = ["Thurflecks", "Arlargado", "DonaDev", "Guebo", "Dreagas", "Kokinaldo", "Gl"]


var = customtkinter.StringVar(root)
var.set(opcoes[0]) 

fellas = CTkOptionMenu(root, variable=var, values=opcoes)
fellas.place(relx=0.5, y= 100, anchor="center")

verfella = CTkButton(root, text = "Ver Fella", command=ver)
verfella.place(relx=0.5, y=300, anchor = "center")

root.mainloop()