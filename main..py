from tkinter import *
from tkinter import messagebox
import random

def yes():
  messagebox.showinfo(' ', 'I agree')
  quit()
  
def motionMouse(event):
  btnNo.place(x=random.randint(0,500), y=random.randint(0,500))

root = Tk()
root.geometry('600x600')
root.title('Python Survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='Do you like Python?', font='Arial 20 bold', bg='white').pack()
btnNo = Button(root, text='nuh uh', font='Arial 20 bold')
btnNo.place(x=170, y=100)
btnNo.bind('<Enter>', motionMouse)
btnYes = Button(root, text = 'yuh uh', font='Arial 20 bold', command=yes).place(x=350, y=100)

root.mainloop()