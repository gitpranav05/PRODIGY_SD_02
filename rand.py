from tkinter import *
import random
import tkinter.messagebox as tmsg
from windows import set_dpi_awareness

set_dpi_awareness()

count=0
rando = random.randint(1, 100)
print(rando)

def func():
    global count, rando

    try:
        val=gval.get()
        isinstance(val, str)
    except:
        tmsg.showerror("Error","Do not enter string value or leave empty.")
        return

    count+=1

    if rando < gval.get():
        l2.config(text=f"Your guess is more. Attempts:{count}")
        e1.delete(0, END)



    elif rando>gval.get():
        l2.config(text=f"Your guess is less. Attempts:{count}")
        e1.delete(0, END)
        # break
    else:
        tmsg.showinfo(f"Congratulatoins!!!", f"You guessed the correct number with {count} attempts!")
        reset()

def reset():
    global count, rando
    count=0
    rando= random.randint(1, 100)
    print(rando)
    e1.delete(0, END)
    l2.config(text="Enter a number to start", bg = "grey")

root =Tk()
root.geometry("700x325")
root.resizable(False,False)
root.title("Random Integer Guesser")

f1= Frame(root, bg="grey")

gval = IntVar()

l1=Label(f1, text="Guess the random number between 1 and 100", font=("comicsans",18,"bold"), bg="grey")
l1.pack(pady=20)

e1=Entry(f1, textvariable=gval, font="comicsans 15 bold")
e1.delete(0)
e1.pack(pady=30)

Button(f1, text="Check",font="comicsans 15 bold", command=func).pack()

l2=Label(f1, text="Enter a number to start", font=("comicsans",17,"bold"), bg = "grey")
l2.pack(pady=30)

f1.pack(fill= BOTH)

root.mainloop()