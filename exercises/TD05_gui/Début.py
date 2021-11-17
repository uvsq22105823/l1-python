import tkinter as tk
root = tk.Tk()
root.title("coucou")
root.geometry("600x600")
canvas = tk.Canvas(root,width=600,height=600,bg="#000000")

bouton_carré=tk.Button(root,text="Carré",command=root.destroy,bg="#22DD51",relief="groove")
bouton_carré.grid(row=2,column=1)

bouton_cercle=tk.Button(root,text="Cercle",command=root.destroy,bg="#22DDC2",relief="groove")
bouton_cercle.grid(row=3,column=1)

bouton_croix=tk.Button(root,text="Croix",command=root.destroy,bg="#2279DD",relief="groove")
bouton_croix.grid(row=4,column=1)

bouton_choix=tk.Button(root,text="Choisis une couleur",command=root.destroy,relief="groove")
bouton_choix.grid(row=1,column=4)

canvas.grid(row=2,column=3,rowspan=3,columnspan=4)
root.mainloop()