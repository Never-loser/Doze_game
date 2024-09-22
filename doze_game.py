from tkinter import *

root = Tk()
COLUMN = 0
ROW = 0
turn = "X"


def game(button):
    global turn

    if turn == "X":
        turn = "Y"
        label.config(text="O turn:")
        button.config(text="X", bg="green")

    else:
        turn = "X"
        label.config(text="X turn:")
        button.config(text="O", bg="red")
    if x1.cget("text") == "X" and x2.cget("text") == "X" and x3.cget("text") == "X":
        label.config(text="X won the game")
    elif x1.cget("text") == "X" and x4.cget("text") == "X" and x7.cget("text") == "X":
        label.config(text="X won the game")
    elif x1.cget("text") == "X" and x5.cget("text") == "X" and x9.cget("text") == "X":
        label.config(text="X won the game")

    elif x2.cget("text") == "X" and x5.cget("text") == "X" and x8.cget("text") == "X":
        label.config(text="X won the game")

    elif x3.cget("text") == "X" and x6.cget("text") == "X" and x9.cget("text") == "X":
        label.config(text="X won the game")

    elif x4.cget("text") == "X" and x5.cget("text") == "X" and x6.cget("text") == "X":
        label.config(text="X won the game")

    elif x7.cget("text") == "X" and x8.cget("text") == "X" and x9.cget("text") == "X":
        label.config(text="X won the game")

    elif x3.cget("text") == "X" and x5.cget("text") == "X" and x7.cget("text") == "X":
        label.config(text="X won the game")
    if x1.cget("text") == "O" and x2.cget("text") == "O" and x3.cget("text") == "O":
        label.config(text="O won the game")
    elif x1.cget("text") == "O" and x4.cget("text") == "O" and x7.cget("text") == "O":
        label.config(text="O won the game")
    elif x1.cget("text") == "O" and x5.cget("text") == "O" and x9.cget("text") == "O":
        label.config(text="O won the game")

    elif x2.cget("text") == "O" and x5.cget("text") == "O" and x8.cget("text") == "O":
        label.config(text="O won the game")

    elif x3.cget("text") == "O" and x6.cget("text") == "O" and x9.cget("text") == "O":
        label.config(text="O won the game")

    elif x4.cget("text") == "O" and x5.cget("text") == "O" and x6.cget("text") == "O":
        label.config(text="O won the game")

    elif x7.cget("text") == "O" and x8.cget("text") == "O" and x9.cget("text") == "O":
        label.config(text="O won the game")

    elif x3.cget("text") == "O" and x5.cget("text") == "O" and x7.cget("text") == "O":
        label.config(text="O won the game")


def reset():
    global turn
    x1.config(text="*", bg="white")
    x2.config(text="*", bg="white")
    x3.config(text="*", bg="white")
    x4.config(text="*", bg="white")
    x5.config(text="*", bg="white")
    x6.config(text="*", bg="white")
    x7.config(text="*", bg="white")
    x8.config(text="*", bg="white")
    x9.config(text="*", bg="white")
    label.config(text="X turn:")
    turn = "X"


x1 = Button(root, text="*", height=5, width=10, command=lambda: game(x1))
x2 = Button(root, text="*", height=5, width=10, command=lambda: game(x2))
x3 = Button(root, text="*", height=5, width=10, command=lambda: game(x3))
x4 = Button(root, text="*", height=5, width=10, command=lambda: game(x4))
x5 = Button(root, text="*", height=5, width=10, command=lambda: game(x5))
x6 = Button(root, text="*", height=5, width=10, command=lambda: game(x6))
x7 = Button(root, text="*", height=5, width=10, command=lambda: game(x7))
x8 = Button(root, text="*", height=5, width=10, command=lambda: game(x8))
x9 = Button(root, text="*", height=5, width=10, command=lambda: game(x9))
x1.grid(row=1, column=0)
x2.grid(row=1, column=1)
x3.grid(row=1, column=2)
x4.grid(row=2, column=0)
x5.grid(row=2, column=1)
x6.grid(row=2, column=2)
x7.grid(row=3, column=0)
x8.grid(row=3, column=1)
x9.grid(row=3, column=2)

label = Label(text=f"{turn} turn: ",font=("arial",18),bg="#FFC000",width=17)
label.grid(row=0, column=0, columnspan=3)

reply_button = Button(text="reply", command=reset,width=33,bg="#FFC401")
reply_button.grid(row=4, column=0, columnspan=3)
root.mainloop()
