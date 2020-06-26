from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
player = {"level": 0, "score": 0, 'NbLine': 0}

cheight = 700
cwidth = 500
root.title("Game Nathan")
root.resizable(False, False)

canvas = Canvas(root, width = cwidth, height = cheight)
canvas.pack()

#1 - 10 => 2
#11 - 15 => 3
#16 - 18 => 4
#19 - 20 => 5
#tous les 10 line level ++

def generateEntity():
    global canvas, cheight
    positionDepartX = randint(0, 9)*35
    positionFinalX = positionDepartX + 35
    positionDepartY = 0
    positionFinalY = 35

    couleur = ["red", "green", "yellow", "blue"]
    color = couleur[randint(0, 3)]
    forme = canvas.create_rectangle(positionDepartX, positionDepartY, positionFinalX, positionFinalY, fill=color, tags='block')

    for x in range(66500):

        myForme = canvas.coords(forme)
        prevForme = canvas.find_overlapping(myForme[0]+1,myForme[1],myForme[2]-1,myForme[3])
        if len(prevForme) > 1:
            break
        
        if myForme[1] > 665:
            break
                            
        canvas.move(forme, 0, 0.01)

        def leftKey(event):
            prevForme = canvas.find_overlapping(myForme[0]-1,myForme[1],myForme[2]-1,myForme[3])
            if myForme[0] > 0 and len(prevForme) == 1:
                canvas.move(forme, -35, 0)

        def rightKey(event):
            prevForme = canvas.find_overlapping(myForme[0]+1,myForme[1],myForme[2]+1,myForme[3])
            if myForme[0] < 315 and len(prevForme) == 1:
                canvas.move(forme, 35, 0)

        def downKey(event):
            if myForme[1] < 665:
                prevForme = canvas.find_overlapping(myForme[0]+1,myForme[1],myForme[2]-1,myForme[3]+25)
                if myForme[1] + 25 > 665 and len(prevForme) == 1:
                    canvas.move(forme,0 ,665-myForme[1])
                elif len(prevForme) == 1:
                    canvas.move(forme,0,25)
            
        root.bind('<Left>', leftKey)
        root.bind('<Right>', rightKey)
        root.bind('<Down>', downKey)
        root.update()

        prevFormes = canvas.find_overlapping(0,canvas.coords(forme[1]-10,315,canvas.coords[3]-10))
        if len(prevForme) > 10:
            for theFormes in prevFormes:
                canvas.delete(theFormes)
            canvas.move('block', 0, 35)
        generateBlock()

        

    generateEntity()
        
def createWindows():
    global canvas
    
    canvas.create_rectangle(350, 0, 500, 700, fill= 'black')
    scoreText = canvas.create_text(401, 25, text= "Score User:", fill= 'white')
    scoreValeurText = canvas.create_text(465, 25, text= "0pts", fill= 'white')
    levelText = canvas.create_text(401, 50, text= "level User:", fill= 'white')
    levelValeurText = canvas.create_text(465, 50, text= "0", fill= 'white')
    generateEntity()

#cancas.itemconfig(levelValeurText, text = str(player['level']))


createWindows()
root.mainloop()



