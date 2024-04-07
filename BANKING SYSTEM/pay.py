from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from dbconnection import *

def give():
    sid=casid.get()
    rid=recieverid.get()
    rs=int(amount.get())
    spassword=senderpassword.get()
    mycursor=connection.cursor()
    sql = f"SELECT * FROM `users`"
    mycursor.execute(sql)
    data=mycursor.fetchall()
    uids=set()
    for i in data:
        uids.add(i[0])
    if ((sid in uids) and (rid in uids)):
        try:
            sql1 = f"SELECT amount FROM account where casid={sid} and passs={spassword}"
            mycursor.execute(sql1)
            sender=int(mycursor.fetchone()[0])
            sender=sender-rs
            if (sender>=0):
                sql1 = f"update  account set amount = {sender} where casid={sid} "
                mycursor.execute(sql1)
                sql3 = f"SELECT amount FROM account where casid={rid}"
                mycursor.execute(sql3)
                reciever=int(mycursor.fetchone()[0])
                reciever=reciever+rs
                sql4 = f"update  account set amount = {reciever} where casid={rid} "
                mycursor.execute(sql4)
                connection.commit()
                messagebox.showinfo("success",f"{rs} has been paid ")
            else:
                messagebox.showerror("error","you don't have enough balane to proceed the transaction")
        except Exception as e:
            messagebox.showerror("error","invalid password")
    else:
        messagebox.showerror("error","either sender or reciever doesnot have SMPK bank account")
        
root=Tk()
root.title("banking system")
root.iconbitmap("E:\\vscode\\python\\PYTHON FILES\\TKINTER PROJECTS\\BANKING SYSTEM\\Bank_icon-icons.com_74914.ico")
Label(root,text="Welcome to SMPK bank   ",fg="red",bg="light blue",font="stencil 25 bold").grid(row=0,column=0,columnspan=2,sticky=N,padx=10,pady=10)
Label(root,text="This is the portfolio of the deposit section of banking system",fg="grey",font="calbri 12 bold").grid(row=1,column=0,columnspan=2,sticky=N,padx=10,pady=10)
try:
    img=Image.open("E:\\vscode\python\\PYTHON FILES\\TKINTER PROJECTS\\BANKING SYSTEM\\baas-banking-as-a-service-.png")
    img=img.resize((350,300))
    img=ImageTk.PhotoImage(img)
    Label(root,image=img).grid(row=2,column=0,columnspan=2,sticky=N,padx=10,pady=10)
except Exception as e:
    print(e)
Label(root,text='user cas id : ').grid(row=3,column=0,sticky=N,padx=10,pady=10)
casid=Entry(root,width=40)
casid.grid(row=3,column=1,padx=10,pady=10)
Label(root,text='reciever-id : ').grid(row=4,column=0,sticky=N,padx=10,pady=10)
recieverid=Entry(root,width=40)
recieverid.grid(row=4,column=1,padx=10,pady=10)
Label(root,text='amount : ').grid(row=5,column=0,sticky=N,padx=10,pady=10)
amount=Entry(root,width=40)
amount.grid(row=5,column=1,padx=10,pady=10)
Label(root,text='sender-password : ').grid(row=6,column=0,sticky=N,padx=10,pady=10)
senderpassword=Entry(root,width=20,show='.',font="stencil 15 bold")
senderpassword.grid(row=6,column=1,padx=10,pady=10)
Button(root,text="pay",command=give,width=40,height=1,border=3,bd=3).grid(row=7,columnspan=2,padx=10,pady=10,sticky=N)
root.mainloop()