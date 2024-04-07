from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from dbconnection import *
import os
import qrcode

def getqr(uid, fname, key):
    folder_name = "users"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    filename = f"{fname}.png"
    file_path = os.path.join(folder_name, filename)
    
    data = f"{uid}-{key}"
    qr = qrcode.QRCode(version=1, box_size=5, border=10)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill='black', back_color='white')
    qr_image.save(file_path)
    
    print(f"QR code saved as {fname}.png")

def gettinguid():
    while True:
        uid = random.randint(1000000000, 9999999999)
        mycursor = connection.cursor()
        sql = 'SELECT * FROM users WHERE uid = %s'
        mycursor.execute(sql, (uid,))
        result = mycursor.fetchone()
        if result is None:
            return uid




def register():
    global name, email, age,gender,password,phone
    fname=name.get()
    Email=email.get()
    sex=gender.get()
    
    key=password.get()
    Age=int(age.get())
    contact=int(phone.get())
    uid=gettinguid()
    
    print(uid)
    print("wait registration will proceed soon")
    mycursor = connection.cursor()
    sql="INSERT INTO `users`(`uid`, `name`, `age`, `gender`, `passs`, `email`, `contact`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val=[uid,fname,Age,sex,key,Email,contact]
    try:
        mycursor.execute(sql,val)
        messagebox.showinfo("info","registration process is completed")
        getqr(uid,fname,key)
        connection.commit()
    except Exception as e:
        messagebox.showerror("error",f"failed to register due to\n {e} ")
    sql = "INSERT INTO `account`(`casid`, `amount`, `passs`,`interest`) VALUES (%s, '0', %s,0)"
    val=[uid,key]
    mycursor = connection.cursor()
    mycursor.execute(sql,val)
    connection.commit()
def validate_otp():
    
    OTP=int(otp.get())
    print(OTP)
    print(actualopt)
    if (OTP==actualopt):
        messagebox.showinfo("info","mail is successfully verified")
        register()
    else:
        messagebox.showerror("error","otp doesnot match")
def validate():
    global name, email, age,gender,password,phone
    fname=name.get()
    Email=email.get()
    sex=gender.get()
    key=password.get()
    Age=int(age.get())
    contact=int(phone.get())
    
    if (fname=='' or Email=='' or sex==''or key=='' or Age=='' or contact==''):
        messagebox.showerror("error","empty fields are detected \nall files are required")
    else:
        
        if (len(key)<10):
            messagebox.showerror("error","password should be of 10 or of more character")
        else:
            try:
                import smtplib as s 
                global server
                server = s.SMTP('smtp.gmail.com', 587)
                server.starttls()
                global actualopt
                actualopt= random.randrange(100000,999999) 
                try:
                    # Use the application-specific password generated from your Google Account
                    server.login('your mail', 'your password')
                except Exception as e:
                    print(e)
                subjecttext='validation of email '
                body=f'''
            Dear {fname},
            it is found that you are trying to open bank account in SMPK bank. your otp is {actualopt}
            please enter this for proceeding further details
            Thank you for your cooperation.

            Sincerely,

            SMPK BANK DETAILS

                '''
                message = f"Subject: {subjecttext}\n\n{body}"

                try:
                    server.sendmail('your mail',Email, message)
                    messagebox.showinfo("info","Successfully mail was sent")
                    foot=Toplevel(root)
                    Label(foot,text="enter otp here").grid(row=0,column=0,padx=10,pady=10)
                    global otp
                    otp=Entry(foot)
                    otp.grid(row=1,column=0,sticky=W,padx=10,pady=10)
                    Button(foot,text="check otp",command=validate_otp).grid(row=2,column=0,sticky=W,padx=10,pady=10)
                    foot.mainloop()
                except Exception as e:
                    messagebox.showerror("error",f"error in sending mail due to {e}")
                    server.quit()
            except Exception as e:
                print(e)
                

root = Tk()
root.title("Registration Window")
root.iconbitmap(r"E:\vscode\python\PYTHON FILES\TKINTER PROJECTS\BANKING SYSTEM\Bank_icon-icons.com_74914.ico")

Label(root, text="Enter valid details", font="stencil 24 bold", fg="grey", bg="light blue").grid(row=0, sticky=N,pady=10,columnspan=2)
Label(root,text="Name : ",font="calibri 17 italic").grid(row=1,column=0)

global name 
name=Entry(root,width=30)
name.grid(row=1,column=1,padx=10,pady=10)
Label(root,text="Age  : ",font="calibri 17 italic").grid(row=2,column=0)

global age 
age=Entry(root,width=30)
age.grid(row=2,column=1,padx=10,pady=10)
Label(root,text="Gender : ",font="calibri 17 italic").grid(row=3,column=0)

global Gender 
gender=Entry(root,width=30)
gender.grid(row=3,column=1,padx=10,pady=10)
Label(root,text="password : ",font="calibri 17 italic").grid(row=4,column=0)

global Password 
password=Entry(root,show="*",width=30)
password.grid(row=4,column=1,padx=10,pady=10)
Label(root,text="email : ",font="calibri 17 italic").grid(row=5,column=0)

global email 
email=Entry(root,width=30)
email.grid(row=5,column=1,padx=10,pady=10)
Label(root,text="phone no.  : ",font="calibri 17 italic").grid(row=6,column=0)

global phone 
phone=Entry(root,width=30)
phone.grid(row=6,column=1,padx=10,pady=10)

Button(root,text="Validate",command=validate,width=30,height=2,border=2,bd=3).grid(row=7,column=0,columnspan=2,padx=10,pady=10)
root.mainloop()
