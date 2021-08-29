from tkinter import *
import cmath
m = Tk()
m.title("Quadratic Equation Solver")
m.geometry("650x300")
global A
A = Entry(m,relief = RAISED,width = 30)
A.place(x=10,y=30)
global B
B = Entry(m,relief = RAISED,width = 30)
B.place(x=200,y=30)
global C
C = Entry(m,relief = RAISED,width = 30)
C.place(x=390,y=30)
A.insert(0, 'Your 1st number')
B.insert(0, 'Your 2nd number')
C.insert(0, 'Your 3rd number')
def findSol():
        a = float(A.get())
        b = float(B.get())
        c = float(C.get())
        d = (b**2)-(4*a*c)
        sol1 = (-b-cmath.sqrt(d))/(2*a)
        sol2 = (-b+cmath.sqrt(d))/(2*a)
        R1 = Label(m,bg = 'grey',text = "The first solution"+str(sol1)).place(x = 0, y = 150)
        R2 = Label(m,bg = 'grey',text = "The second solution"+str(sol2)).place(x = 310, y = 150)
def click(*arg):
        A.delete(0,"end")
        B.delete(0,"end")
        C.delete(0,"end")
A.bind("<Button-1>", click)
B.bind("<Button-2>", click)
C.bind("<Button-3>", click)
b1 = Button(m,text = "calculate",bg = 'blue',activebackground = 'blue',activeforeground = 'white',fg = 'white',command = findSol)
b1.place(x = 310,y = 100)
m.mainloop()
