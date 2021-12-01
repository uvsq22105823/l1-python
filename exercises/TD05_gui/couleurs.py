import tkinter as tk
root = tk.Tk()
root.title("cible")
root.geometry("400x256")
canvas = tk.Canvas(root,width=256,height=256,bg="#000000")
canvas.grid(row=1,column=3,rowspan=6,columnspan=6)


i=128
j=129
color="white"

def draw_pixel(i,j,color):
    canvas.create_line(i,i,j,j,fill=color)

    


bouton_aléatoire=tk.Button(root,text="Aléatoire",command=draw_pixel,relief="groove")
bouton_aléatoire.grid(row=1,column=1)

bouton_dégradégris=tk.Button(root,text="dégradé gris",command=root.destroy,relief="groove")
bouton_dégradégris.grid(row=3,column=1)

bouton_dégradé2d=tk.Button(root,text="dégradé 2D",command=root.destroy,relief="groove")
bouton_dégradé2d.grid(row=5,column=1)





def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)




root.mainloop()