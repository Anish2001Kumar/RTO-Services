from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class Register:
	def __init__(self,root):
		self.root = root
		self.root.title("Registration Window")
		self.root.geometry("1200x700+100+100")
		self.root.config(bg="alice blue")

		# BG Image
		self.bg = ImageTk.PhotoImage(file="Images/bg1.jpeg")
		bg = Label(self.root, image= self.bg).place(x=350,y=0,relwidth=1,relheight=1)


		# LEFT Image
		self.left = ImageTk.PhotoImage(file="Images/left.png")
		left = Label(self.root, image= self.left).place(x=20,y=100,width=475,height=488)

		#---Variables------
		self.var_fname = StringVar()
		self.var_lname = StringVar()
		self.var_contact = StringVar()
		self.var_email = StringVar()
		self.var_question = StringVar()
		self.var_ans = StringVar()
		self.var_passw = StringVar()
		self.var_cpassw = StringVar()
		

		# Check Button Functonality (Show password)
		

		# Register Frame
		frame1 = Frame(self.root, bg = "alice blue" )
		frame1.place(x=495,y=100,width = 600, height=488)

		title = Label(frame1, text="REGISTER HERE", font=("times new roman",24,"bold"),bg="alice blue",fg="green").place(x=50,y=30)

		fname = Label(frame1, text="First Name", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=50,y=100)
		txt_fname = Entry(frame1, textvariable = self.var_fname, font=("times new roman",15)).place(x=50,y=130)

		lname = Label(frame1, text="Last Name", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=300,y=100)
		txt_lname = Entry(frame1, textvariable = self.var_lname, font=("times new roman",15)).place(x=300,y=130)

		contact = Label(frame1, text="Contact No.", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=50,y=170)
		txt_contact = Entry(frame1, textvariable = self.var_contact, font=("times new roman",15)).place(x=50,y=200)

		email = Label(frame1, text="Email Id", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=300,y=170)
		txt_email = Entry(frame1, textvariable = self.var_email, font=("times new roman",15)).place(x=300,y=200)


		question = Label(frame1, text="Security Question", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=50,y=240)
		cmb_question = ttk.Combobox(frame1, font=("times new roman",13), state='readonly',textvariable = self.var_question)
		cmb_question["values"]=("Select the Question","What's your pet name ?","What's your favourite place ?","What's your hero name ?")
		cmb_question.current(0)
		cmb_question.place(x=50,y=270,width=180)

		ans = Label(frame1, text="Answer", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=300,y=240)
		txt_ans = Entry(frame1, textvariable = self.var_ans, font=("times new roman",15)).place(x=300,y=270)


		passw = Label(frame1, text="Password", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=50,y=310)
		txt_passw = Entry(frame1, textvariable = self.var_passw, font=("times new roman",15),show='*')
		txt_passw.place(x=50,y=340)

		cpassw = Label(frame1, text="Confirm Password", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=300,y=310)
		txt_cpassw = Entry(frame1, textvariable = self.var_cpassw, font=("times new roman",15),show='*')
		txt_cpassw.place(x=300,y=340)

		#----Check Button------------------

		def mark():

			if var.get()==1:
				txt_passw.configure(show="")
				txt_cpassw.configure(show="")
			if var.get()==0:
				txt_passw.configure(show="*")
				txt_cpassw.configure(show="*")

		var = IntVar()

		bt = Checkbutton(frame1,text="Show Password", font=("times new roman",15), command= mark, offvalue=0 , onvalue = 1, variable = var,bg="alice blue")
		bt.place(x=50,y=375)



		#----Buttons------------------

		self.btn_img = ImageTk.PhotoImage(file = "Images/reg_btn.png")
		btn_register = Button(frame1,image =self.btn_img,bd=0,bg="alice blue",command=self.register_data).place(x=50,y=410,width=300,height=50)

		btn_login = Button(self.root ,text="Sign In",font=("times new roman",20),bg="alice blue",bd=0).place(x=310,y=500,width=150,height=44)

		
	

	#----Backend-------------------

	def register_data(self):

		con= sqlite3.connect(database ="RTO.db")
		cur=con.cursor()

		try:
			if self.var_fname.get()=="":
				messagebox.showerror("Error !","First Name is required", parent = self.root)

			elif self.var_lname.get()=="":
				messagebox.showerror("Error !","Last Name is required", parent = self.root)

			elif self.var_contact.get()=="":
				messagebox.showerror("Error !","Contact No is required", parent = self.root)

			elif self.var_email.get()=="":
				messagebox.showerror("Error !","Email ID is required", parent = self.root)

			elif self.var_question.get()=="Select the Question":
				messagebox.showerror("Error !","Security question is not selected", parent = self.root)

			elif self.var_ans.get()=="":
				messagebox.showerror("Error !","Security Answer is required", parent = self.root)

			elif self.var_passw.get()=="":
				messagebox.showerror("Error !","password is required", parent = self.root)

			elif self.var_cpassw.get()=="":
				messagebox.showerror("Error !","Please confirm your password", parent = self.root)

			elif self.var_cpassw.get()!=self.var_passw.get():
				messagebox.showerror("Error !","Your password doesn't matches with confirm password", parent = self.root)

			else:

				cur.execute("Select * from Employee where email=?",(self.var_email.get(),))
				row=cur.fetchone()

				if row!=None:
					messagebox.showerror("Error !","Email ID already exists", parent = self.root)

				else:
					cur.execute("insert into Employee(fname,lname,contact,email,question,answer,passw,cpassw) values(?,?,?,?,?,?,?,?)", (
						self.var_fname.get(),
						self.var_lname.get(),
						self.var_contact.get(),
						self.var_email.get(),
						self.var_question.get(),
						self.var_ans.get(),
						self.var_passw.get(),
						self.var_cpassw.get()
						))
					con.commit()
					messagebox.showinfo("Success","Registered Successfully !",parent =self.root)

					#---Clearing all values------
					
					self.var_lname.set("")
					self.var_fname.set(""),
					self.var_contact.set(""),
					self.var_email.set(""),
					self.var_question.set("Select the Question"),
					self.var_ans.set(""),
					self.var_passw.set("")
					self.var_cpassw.set("")

		except Exception as ex:
			messagebox.showerror("Error !",f"Error due to {str(ex)}")


		self.var_lname.set("")
		self.var_fname.set(""),
		self.var_contact.set(""),
		self.var_email.set(""),
		self.var_question.set("Select the Question"),
		self.var_ans.set(""),
		self.var_passw.set("")
		self.var_cpassw.set("")

root = Tk()
obj = Register(root)
root.mainloop()