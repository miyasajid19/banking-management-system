from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from dbconnection import *
root1=Tk()
def depo():
    cas=casid.get()
    rs=amount.get()
    bid=bankerid.get()
    bp=bankerpassword.get()
    id="sajid_miya"#set the banker id
    key="021neb432"#set the default password
    mycursor=connection.cursor()
    sql=f"select amount FROM account WHERE casid={cas}"
    mycursor.execute(sql)
    
    d=mycursor.fetchone()
    trs=int(rs)+int(d[0])
    if (bid==id and bp==key):
        mycursor=connection.cursor()
        sql=f"UPDATE account SET amount={trs} WHERE casid={cas}"
        mycursor.execute(sql)
        connection.commit()
        messagebox.showinfo("info",f"{rs} has been deposited to {cas}")
        messagebox.showinfo("info",f"now {cas} has nrs. {trs}")
        root1.destroy()
    else:
        messagebox.showwarning("error","unknown user is trying to enter the system")
    
root1.title("banking system")
root1.iconbitmap("Bank_icon-icons.com_74914.ico")
Label(root1,text="Welcome to SMPK bank   ",fg="red",bg="light blue",font="stencil 25 bold").grid(row=0,column=0,columnspan=2,sticky=N,padx=10,pady=10)
Label(root1,text="This is the portfolio of the deposit section of banking system",fg="grey",font="calbri 12 bold").grid(row=1,column=0,columnspan=2,sticky=N,padx=10,pady=10)
try:
    img=Image.open("baas-banking-as-a-service-.png")
    img=img.resize((350,300))
    img=ImageTk.PhotoImage(img)
    Label(root1,image=img).grid(row=2,column=0,columnspan=2,sticky=N,padx=10,pady=10)
except Exception as e:
    print(e)
Label(root1,text='user cas id : ').grid(row=3,column=0,sticky=N,padx=10,pady=10)
casid=Entry(root1,width=40)
casid.grid(row=3,column=1,padx=10,pady=10)
Label(root1,text='amount : ').grid(row=4,column=0,sticky=N,padx=10,pady=10)
amount=Entry(root1,width=40)
amount.grid(row=4,column=1,padx=10,pady=10)
Label(root1,text='banker-id : ').grid(row=5,column=0,sticky=N,padx=10,pady=10)
bankerid=Entry(root1,width=40)
bankerid.grid(row=5,column=1,padx=10,pady=10)
Label(root1,text='banker-password : ').grid(row=6,column=0,sticky=N,padx=10,pady=10)
bankerpassword=Entry(root1,width=20,show='.',font="stencil 15 bold")
bankerpassword.grid(row=6,column=1,padx=10,pady=10)
Button(root1,text="deposit",command=depo,width=40,height=1,border=3,bd=3).grid(row=7,columnspan=2,padx=10,pady=10,sticky=N)
root1.mainloop()