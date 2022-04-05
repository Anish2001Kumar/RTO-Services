from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from tkmacosx import Button

class Login:
	def __init__(self,root):
		self.root = root
		self.root.title("Login Window")
		self.root.geometry("1200x700+100+100")
		self.root.config(bg="alice blue")

		self.bg = ImageTk.PhotoImage(file="Images/bg4.png")
		bg = Label(self.root, image= self.bg).place(x=0,y=0,relwidth=1,relheight=1)

		#----Frame-------

		login_frame = Frame(self.root,bg="alice blue")
		login_frame.place(x=200, y=100 ,width= 800, height= 500)

		title = Label(login_frame,text="RTO Management System",font=("times new roman",40,"bold"),justify= CENTER, bg="#033054",fg="alice blue").place(width=800, height=60)

		log = Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),fg="cyan4",bg="alice blue").place(x=80 ,y=80)

		self.bg1 = ImageTk.PhotoImage(file="Images/log1.png")
		bg1 = Label(login_frame, image= self.bg1 ,bg="alice blue").place(x=300,y=130,width=150,height=147)

		email = Label(login_frame,text="Email Id",font=("times new roman",25,"bold"),bg="alice blue").place(x=200 ,y=290)
		self.txt_email = Entry(login_frame,font=("times new roman",20),bg="light grey")
		self.txt_email.place(x=320 ,y=290)

		passw = Label(login_frame,text="Password",font=("times new roman",25,"bold"),bg="alice blue").place(x=200 ,y=340)
		self.txt_passw = Entry(login_frame,font=("times new roman",20),bg="light grey",show="*")
		self.txt_passw.place(x=320 ,y=340)


		btn_reg = Button(login_frame,text="Register New Account",font=("times new roman",14),fg="#B00857",bg="alice blue",bd=0).place(x=200,y=390)

		btn_fgt = Button(login_frame,text="Forgot Password ?",font=("times new roman",14),fg="#B00857",bg="alice blue",bd=0).place(x=390,y=390)

		self.btn_img = ImageTk.PhotoImage(file = "Images/log_btn.png")
		btn_login = Button(login_frame,image =self.btn_img,bd=0,bg="alice blue",command=self.login).place(x=300,y=430,width=150,height=41)

	def login(self):
		if self.txt_email.get()=="" or self.txt_passw=="" :
			messagebox.showerror("Error !","All Fields are required", parent = self.root)

		else:

			try:
				con= sqlite3.connect(database ="RTO.db")
				cur=con.cursor()

				cur.execute("Select * from Employee where email=? and passw=?",(self.txt_email.get(),self.txt_passw.get()))
				row=cur.fetchone()

				if row==None:
					messagebox.showerror("Error !","Invalid Username and Password", parent = self.root)

				else:
					messagebox.showinfo("Success",f"Welcome {row[0]} !",parent =self.root)

			except Exception as ex:
				messagebox.showerror("Error !",f"Error due to {str(ex)}")

root = Tk()
obj = Login(root)
root.mainloop()