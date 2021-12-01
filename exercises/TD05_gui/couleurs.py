import tkinter as tk
root = tk.Tk()
root.title("cible")
root.geometry("400x256")
canvas = tk.Canvas(root,width=256,height=256,bg="#000000")
canvas.grid(row=1,column=3,rowspan=6,columnspan=6)
import random as r

def get_color(R, G, B):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(R, G, B)


color="white"

def draw_pixel(i,j,color):
    canvas.create_rectangle(i,j,i,j,fill=color,outline="")

def couleursaléatoires():
    for i in range(256):
        for j in range(256):
            R=r.randint(0,255)
            G=r.randint(0,255)
            B=r.randint(0,255)
            draw_pixel(i,j,color=get_color(R,G,B))
        
def dégradégris():
    for i in range(256):
        for j in range(256):
            R=j
            G=R
            B=R
            draw_pixel(j,i,color=get_color(R,G,B))


def dégradé2D():
    for i in range(256):
        for j in range(256):
            R=i
            G=0
            B=j
            draw_pixel(i,j,color=get_color(R,G,B))
    



    


bouton_aléatoire=tk.Button(root,text="Aléatoire",command=couleursaléatoires,relief="groove")
bouton_aléatoire.grid(row=1,column=1)

bouton_dégradégris=tk.Button(root,text="dégradé gris",command=dégradégris,relief="groove")
bouton_dégradégris.grid(row=3,column=1)

bouton_dégradé2d=tk.Button(root,text="dégradé 2D",command=dégradé2D,relief="groove")
bouton_dégradé2d.grid(row=5,column=1)










root.mainloop()