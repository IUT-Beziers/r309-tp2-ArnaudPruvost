from tkinter import *
from tkinter import ttk
from PIL import Image

root = Tk()
root.title("ma page")
root.geometry("600x540")

img_cliq = ""
def choix(val):
	global img_cliq
	if val == 1:
		img_cliq = img1
	elif val == 2:
		img_cliq = img2
	elif val == 3:
		img_cliq = img3
	elif val == 0 :
		img_cliq = ""

	

def clique(pos):
	if img_cliq != "" and pos.x > 25 and pos.y>30:
		image = dessin.create_image(pos.x,pos.y,image=img_cliq)
		dessin.tag_bind(image, "<Button-3>", lambda event: dessin.delete(image))
		placer = True

but1=ttk.Button(root, width = 10, text="Ordinateur",command=lambda: choix(1))
but1.place(x=10,y=10)
but2=ttk.Button(root, width = 10, text="Switch",command=lambda: choix(2))
but2.place(x=100,y=10)
but3=ttk.Button(root, width = 10, text="Routeur",command=lambda: choix(3))
but3.place(x=190,y=10)
but4=ttk.Button(root, width = 10, text="Sélectionner",command=lambda: choix(0))
but4.place(x=280,y=10)

lg, ht = 600,540
dessin=Canvas(root,bg="ivory",width=lg,height=ht)
dessin.pack(side='bottom', padx=20, pady=40)

img1 = PhotoImage(file = 'ordinateur.png')
img2 = PhotoImage(file = 'switch.png')
img3 = PhotoImage(file = 'router.png')


root.bind('<Button 1>',clique)

root.mainloop()
