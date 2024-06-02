from tkinter import *
from PIL import Image,ImageTk
def newregister():
    import register
def login():
    import forlogging
def depos():
    import deposit
def payment():
    import pay
 
root=Tk()
root.title("banking system")
root.iconbitmap("login_icon_176905.ico")
Label(root,text="Welcome to SMPK bank",fg="red",bg="light blue",font="stencil 25 bold").grid(row=0,sticky=N)
Label(root,text="This is the portfolio of the banking system",fg="grey",font="calbri 12 bold").grid(row=1,sticky=N)
try:
    img=Image.open("baas-banking-as-a-service-.png")
    img=img.resize((250,200))
    img=ImageTk.PhotoImage(img)
    Label(root,image=img).grid(row=2,sticky=N)
except :
    pass
Button(root,text="log in",width=20,command=login).grid(row=3,pady=10,sticky=N)
Button(root,text="New Register",width=20,command=newregister).grid(row=4,pady=10,sticky=N)
Button(root,text="Deposit",width=20,command=depos).grid(row=5,pady=10,sticky=N)
Button(root,text="Payment",width=20,command=payment).grid(row=6,pady=10,sticky=N)
root.mainloop()