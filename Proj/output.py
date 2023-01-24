from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo


def close():
    output.window.destroy()
    
    
def output():
    window = Tk()
    window.title("Output Window")
    window.geometry("500x500")

    heading = Label(window,text="Output Window",bg="grey",fg="white",font="40",width="500",height="3")
    heading.pack()

    button = Button(window, text="Submit" , width="12",  bg="brown" , fg="white" , command=close)
    button.place(x="170",y="450")