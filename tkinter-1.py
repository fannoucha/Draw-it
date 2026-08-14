import tkinter
print("Pour dessiner, déplace ta souris avec clic gauche")
print("Pour changer de couleur,clique sur une des couleurs")
fenêtre = tkinter.Tk()
titre = tkinter.Label(
    fenêtre,
    text="DRAW IT !",
    font=("Helvetica Neue", 35)
)
canvas = tkinter.Canvas(fenêtre, width=1500, height=1000, bg="white")
canvas.pack()
dernierX,dernierY = 0,0
couleur  = "black"
def enregistrer_position(event):
    global dernierX, dernierY
    dernierX = event.x
    dernierY = event.y
def quand_Cliqué(event):
    enregistrer_position(event)
def quand_Déplacé(event):
    canvas.create_line(dernierX, dernierY, event.x, event.y,fill = couleur, width = largeur.get())
    enregistrer_position(event)
canvas.bind("<Button-1>",quand_Cliqué)
canvas.bind("<B1-Motion>",quand_Déplacé)
red_id = canvas.create_rectangle(10, 10, 30, 30, fill="red")
blue_id = canvas.create_rectangle(10, 35 ,30, 55, fill="blue")
green_id = canvas.create_rectangle(10, 60, 30, 80, fill="green")
yellow_id = canvas.create_rectangle(10, 85, 30, 105, fill="yellow")
black_id = canvas.create_rectangle(10, 110, 30, 130, fill="black")
white_id = canvas.create_rectangle(10, 135, 30, 155, fill="white")
def couleurRed(event):
    global couleur
    couleur="red"
def couleurBlue(event):
    global couleur
    couleur="blue"
def couleurGreen(event):
    global couleur
    couleur="green"
def couleurYellow(event):
    global couleur
    couleur="yellow"
def couleurBlack(event):
    global couleur
    couleur="black"
def couleurWhite(event):
    global couleur
    couleur="white"
canvas.tag_bind(red_id, "<Button-1>", couleurRed)
canvas.tag_bind(blue_id, "<Button-1>", couleurBlue)
canvas.tag_bind(green_id, "<Button-1>",couleurGreen) 
canvas.tag_bind(yellow_id, "<Button-1>",couleurYellow) 
canvas.tag_bind(black_id, "<Button-1>",couleurBlack)
canvas.tag_bind(white_id, "<Button-1>",couleurWhite)
largeur = tkinter.Scale(
    fenêtre,
    from_=1,
    to=30,
    orient="horizontal",
    label="Largeur du crayon"
)
largeur.place(
    relx=1.0,
    x=-10,
    y=10,
    anchor="ne"
)
fenêtre.mainloop()
