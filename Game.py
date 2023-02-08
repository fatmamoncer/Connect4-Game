from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('le jeu puissance 4')
# builing our buttons on the grille
grille = []

def resetboard():
    global grille
    for y in range(6):
        grille.append([])
        for x in range(7):
            grille[y].append(x)
            grille[y][x] = Button(root, text="", font=(
                "helvetica", 20), height=1, width=2, bg="SystemButtonFace")
            grille[y][x].config(command=lambda y=y, x=x: b_click(x, y))
            grille[y][x].grid(column=x, row=y)
    messagebox.showinfo("player "+str(1)+" starts first using chip"+str(1))
    messagebox.showinfo("player "+str(2)+" starts second using chip"+str(2))

resetboard()


# playerone starts white
clicked = True
count = 0

# add chips with a minimal position fonction
def pos_min(x, y):
    global grille
    # get the minimum position in the y axis
    for i in range(5, -1, -1):
        if grille[i][x]["text"] == "":
            return i

# b_click fonction
def b_click(x, y):
    global clicked, count
    global grille

    # clicked = True
    if grille[y][x]["text"] == "" and clicked == True:
        n = pos_min(x, y)
        grille[n][x].config(text='⚪', bg='black', fg='white')
        if checkifwon():
            messagebox.showinfo("player 2 wins!!")
            resetboard()
        clicked = False

    elif grille[y][x]["text"] == "" and clicked == False:
        n = pos_min(x, y)
        grille[n][x].config(text='⚫', bg='white', fg='black')
        if checkifwon():
            messagebox.showinfo("player 1 wins!!")
            resetboard()
        clicked = True

    else:
        messagebox.showerror(
            "hey! this box has been already selected ..try another one")

    if count == 42 and winner == False:
        messagebox.showinfo("no one wins!!")
        resetboard()


# check to see if someone won
def checkifwon():
    global winner
    winner = False
    for y in range(6):
        for x in range(7):
            if checkhorizontal(grille, x, y) or checkvertical(grille, x, y) or checkdiagonal(grille, x, y):
                winner = True

                break
    return winner

# check horizontal
def checkhorizontal(grille, x, y):
    if x < 4:
        if grille[y][x]["text"] == grille[y][x+1]["text"] == grille[y][x+2]["text"] == grille[y][x+3]["text"] and grille[y][x]["text"] != "":
            return True
    return False

# check vertical
def checkvertical(grille, x, y):
    if y < 3:
        if grille[y][x]["text"] == grille[y+1][x]["text"] == grille[y+2][x]["text"] == grille[y+3][x]["text"] and grille[y][x]["text"] != "":
            return True
    return False

# check diagonal
def checkdiagonal(grille, x, y):
    if x < 4 and y < 3:
        if grille[y][x]["text"] == grille[y+1][x+1]["text"] == grille[y+2][x+2]["text"] == grille[y+3][x+3]["text"] and grille[y][x]["text"] != "":
            return True
    if x < 4 and y > 2:
        if grille[y][x]["text"] == grille[y-1][x+1]["text"] == grille[y-2][x+2]["text"] == grille[y-3][x+3]["text"] and grille[y][x]["text"] != "":
            return True
    return False


# add a menu
my_menu = Menu(root)
root.config(menu=my_menu)
# create menu options
reset_menu = Menu(my_menu)
my_menu.add_cascade(label='START THE GAME OVER!', menu=reset_menu)
reset_menu.add_command(label="reset the game", command=resetboard)

root.mainloop()
