from tkinter import *
from PIL import Image, ImageTk
from dbconnection import *
from tkinter import filedialog
import cv2
import random

def open_image():
    cap = cv2.VideoCapture(0)

    # Create a QR code detector
    detector = cv2.QRCodeDetector()

    while True:
        _, frame = cap.read()

        # Detect QR codes
        data, bbox, _ = detector.detectAndDecode(frame)

        # Display the frame
        cv2.imshow('QR Code Scanner', frame)

        # Check if a QR code is detected
        if bbox is not None:
            # Print the data contained in the QR code
            print('Data:', data)
            if data !='':
                break

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()
    id,key=data.split("-")
    mycursor = connection.cursor()
    sql = f"SELECT * FROM `users` WHERE uid='{id}' and passs='{key}'"
    print(sql)
    mycursor.execute(sql)
    data=mycursor.fetchone()
    
    connection.commit()
    mycursor=connection.cursor()
    sql2=f"SELECT * FROM `account` WHERE casid='{id}' and passs='{key}'"
    
    mycursor.execute(sql2)
    print(sql2)
    data2=mycursor.fetchone()
    connection.commit()
    mycursor=connection.cursor()

    if(data is None):
        print("no data is found")
        messagebox.showerror("error","no such account exists")
    else:
        print("data is found")
        showdetails(data,data2[1])
def showdetails(data,data2):
    print("i am callled")
    print(data,data2)
    root1=Toplevel(root)
    root1.iconbitmap("login_icon_176905.ico")
    Label(root1,text="Welcome to SMPK bank",fg="red",bg="light blue",font="stencil 25 bold").grid(row=0,column=0,columnspan=2,sticky=N)
    Label(root1,text="This is the portfolio of the banking system",fg="grey",font="calbri 12 bold").grid(row=1,column=0,columnspan=2,sticky=N)
    Label(root1,text="cas id : ",font="ariel 10 italic").grid(row=2,column=0,padx=10,pady=10)
    Label(root1,text=data[0],font="ariel 10 italic").grid(row=2,column=1,padx=10,pady=10)
    Label(root1,text="name : ",font="ariel 10 italic").grid(row=3,column=0,padx=10,pady=10)
    Label(root1,text=data[1],font="ariel 10 italic").grid(row=3,column=1,padx=10,pady=10)
    print(data[1])
    Label(root1,text="Age : ",font="ariel 10 italic").grid(row=4,column=0,padx=10,pady=10)
    Label(root1,text=data[2],font="ariel 10 italic").grid(row=4,column=1,padx=10,pady=10)
    Label(root1,text="gender : ",font="ariel 10 italic").grid(row=4,column=0,padx=10,pady=10)
    Label(root1,text=data[3],font="ariel 10 italic").grid(row=4,column=1,padx=10,pady=10)
    Label(root1,text="email : ",font="ariel 10 italic").grid(row=5,column=0,padx=10,pady=10)
    Label(root1,text=data[5],font="ariel 10 italic").grid(row=5,column=1,padx=10,pady=10)
    Label(root1,text="contact : ",font="ariel 10 italic").grid(row=6,column=0,padx=10,pady=10)
    Label(root1,text=data[6],font="ariel 10 italic").grid(row=6,column=1,padx=10,pady=10)
    Label(root1,text="amount :",font="ariel 10 italic").grid(row=7,column=0,padx=10,pady=10)
    Label(root1,text=data2,font="ariel 10 italic").grid(row=7,column=1,padx=10,pady=10)
    root1.mainloop()
def signin():
    global casid, password
    print(casid.get())
    print(password.get())
    key=password.get()
    
    mycursor = connection.cursor()
    sql = f"SELECT * FROM `users` WHERE uid='{casid.get()}' and passs='{key}'"
    print(sql)
    mycursor.execute(sql)
    data=mycursor.fetchone()
    
    connection.commit()
    mycursor=connection.cursor()
    sql2=f"SELECT * FROM `account` WHERE casid='{casid.get()}' and passs='{key}'"
    
    mycursor.execute(sql2)
    print(sql2)
    data2=mycursor.fetchone()
    connection.commit()
    mycursor=connection.cursor()

    if(data is None):
        print("no data is found")
        print(data)
    else:
        print("data is found")
        showdetails(data,data2[1])
def updatepass():
    global casid,newpassword
    id=casid.get()
    password=newpassword.get()
    if(len(password)>=10):
        try:
            mycursor=connection.cursor()
            sql=f"update  account set passs={password} WHERE casid={id}"
            mycursor.execute(sql)
            connection.commit()
            sql=f"update  users set passs={password} WHERE uid={id}"
            mycursor.execute(sql)
            connection.commit()
            messagebox.showinfo("info","password updated successfully")
        except Exception as e:
            messagebox.showerror("error",f"error in updating password +{e}")
    else:
        messagebox.showerror("error","password length should be greater equal to 10")
        resetpassword()
    
def resetpassword():
    root=Tk()
    global newpassword
    root.title("banking system")
    Label(root,text="new password : ",font="ariel 10 italic").grid(row=0,column=0,sticky=N,padx=10,pady=10)
    newpassword=Entry(root,width=30,show="*")
    newpassword.grid(row=0,column=1,sticky=N,padx=10,pady=10)
    Button(root,text="reset",width=30,height=1,command=updatepass,border=10,bd=5).grid(row=1,column=0,columnspan=2,sticky=N)
    root.mainloop()

def validate_otp():
    
    OTP=int(otp.get())
    print(OTP)
    print(actualopt)
    if (OTP==actualopt):
        messagebox.showinfo("info","mail is successfully verified")
        resetpassword()
    else:
        messagebox.showerror("error","otp doesnot match")
def forgotpassword():
    global casid
    mycursor = connection.cursor()
    sql = f"SELECT email FROM `users` WHERE uid='{casid.get()}'"
    mycursor.execute(sql)
    data=mycursor.fetchone()
    print(f"i have forgotten the password {data}")
    import smtplib as s 
    server = s.SMTP('smtp.gmail.com', 587)
    server.starttls()
    global actualopt
    actualopt= random.randrange(100000,999999) 
    try:
        # Use the application-specific password generated from your Google Account
        server.login('your mail', 'your password')
    except Exception as e:
        print(e)
    subjecttext='resetting of password'
    body=f'''
            Dear customer,
            it is found that you are trying to reset passowrd of  bank account in SMPK bank.
            your otp is {actualopt}.
            please enter this for proceeding further details
            Thank you for your cooperation.

            Sincerely,

            SMPK bank details

                '''
    message = f"Subject: {subjecttext}\n\n{body}"
    try:
        server.sendmail('your mail',data[0], message)
        messagebox.showinfo("info","Successfully mail is sent")
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

root = Tk()
root.title("Log In")
try:
# Assuming you have the icon file in the same directory as your script
    root.iconbitmap("login_icon_176905.ico")
except:
    pass
Label(root, text="Welcome to SMPK bank", fg="red", bg="light blue", font="stencil 25 bold").grid(row=0,columnspan=2, sticky=N,padx=10,pady=10)
Label(root, text="This is the portfolio of the banking system", fg="grey", font="calbri 12 bold").grid(row=1,columnspan=2, sticky=N,padx=10,pady=10)
try:
# Load image using PIL and display it using a label
    img=Image.open(r"baas-banking-as-a-service-.png")
    img = img.resize((250, 250))
    img = ImageTk.PhotoImage(img)
    label = Label(root, image=img)
    label.grid(row=2,columnspan=2,sticky=N,padx=10,pady=10)
except Exception as e:
    print(e)
Label(root,text="Customer identification code: ").grid(row=3,sticky=N,padx=10,pady=10)
casid=Entry(root,width=30)
casid.grid(row=3,column=1,sticky=N,padx=10,pady=10)
Label(root,text="password : ").grid(row=4,sticky=N,padx=10,pady=10)
password=Entry(root,show="*",width=30)
password.grid(row=4,column=1,sticky=N,padx=10,pady=10)
Button(root,text="forgot password???",font="ariel 10 italic",command=forgotpassword,bd=0,border=0,fg="#165546").grid(row=5,column=1,padx=1,pady=1,sticky=N)
Button(root, text="Open Image", command=open_image).grid(row=6,columnspan=2,padx=10,pady=10)
Button(root,text="Log In",command=signin,border=3,bd=10,width=30).grid(row=7,columnspan=2,padx=10,pady=10)
root.mainloop()
