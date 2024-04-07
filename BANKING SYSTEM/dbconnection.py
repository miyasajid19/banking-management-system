import mysql.connector
from tkinter import *
from tkinter import messagebox
try:
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="bankingsystem")
    connection.is_connected()
except Exception as e:
    messagebox.showerror("error",e)