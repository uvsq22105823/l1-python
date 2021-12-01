import tkinter as tk
root = tk.Tk()
root.title("début")
root.geometry("600x600")
canvas = tk.Canvas(root,width=600,height=600,bg="#000000")
import random as r

color = "blue"

objects=0



def couleur_random():
    global color
    color=str(input("veuillez choisir un couleur  : blue, yellow, red, orange, green, white, magenta..."))


def fonction_cercle():
    x0=r.randint(1,500)
    x1=x0+100
    y0=r.randint(1,500)
    y1=y0+100
    canvas.create_oval(x0,y0,x1,y1,fill=color)
    

def fonction_carré():
    x0=r.randint(1,500)
    x1=x0+100
    y0=r.randint(1,500)
    y1=y0+100
    canvas.create_rectangle(x0,y0,x1,y1,fill=color)


def fonction_croix():
    x0=r.randint(1,500)
    x1=x0+100
    y0=r.randint(1,500)
    y1=y0+100
    canvas.create_line(x0+50,y0,x1-50,y1,width=10,fill=color)
    canvas.create_line(x0,y0+50,x1,y1-50,width=10,fill=color)


#def revenir en arrière
def undo():
    global objects



#bouton carré
bouton_carré=tk.Button(root,text="Carré",command=fonction_carré,bg="#22DD51",relief="groove")
bouton_carré.grid(row=2,column=1)
objects+=1

#bouton cercle
bouton_cercle=tk.Button(root,text="Cercle",command=fonction_cercle,bg="#22DDC2",relief="groove")
bouton_cercle.grid(row=3,column=1)
objects+=1

#bouton croix
bouton_croix=tk.Button(root,text="Croix",command=fonction_croix,bg="#2279DD",relief="groove")
bouton_croix.grid(row=4,column=1)
objects+=1

#choix de couleur
bouton_choix=tk.Button(root,text="Choisis une couleur",command=couleur_random,relief="groove")
bouton_choix.grid(row=1,column=4)

#revenir en arrière
bouton_undo=tk.Button(root,text="revenir en arrière",command=root.destroy,relief="groove")
bouton_undo.grid(row=1,column=3)




canvas.grid(row=2,column=3,rowspan=3,columnspan=4)





root.mainloop()