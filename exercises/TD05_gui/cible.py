import tkinter as tk
root = tk.Tk()
root.title("cible")
a=600
b=600
root.geometry("600x600")
canvas = tk.Canvas(root,width=a,height=b,bg="#000000")

n=120

for i in range(n):
    colors=["blue","green","black","yellow","magenta","red"]

    canvas.create_oval(((a/2)/n)*i,((b/2)/n)*i,a-((a/2)*i/n),b-((b/2)*i/n),fill=colors[i%6])


canvas.grid(row=2,column=2,rowspan=3,columnspan=4)





root.mainloop()