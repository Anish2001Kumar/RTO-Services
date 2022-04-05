from tkinter import *
from tkinter import ttk,messagebox
import sqlite3


class DriClass:
	def __init__(self,root):
		self.root=root
		self.root.title("Driving License Services")
		self.root.geometry("1200x700+50+50")
		self.root.config(bg="white")
		
		# Title
		title = Label(self.root, text="Manage Driving License Details", font= ("goudy old style",30,"bold"),justify="center",bg="#033054",fg="white").place(width=1200,height=35)

		# Label Widgets
		l_dlllnum = Label(self.root, text="DL/LL Number", font= ("goudy old style",20,"bold"),bg="white").place(x=10,y=60)
		l_ownernm = Label(self.root, text="Owner's Name", font= ("goudy old style",20,"bold"),bg="white").place(x=10,y=100)
		l_email = Label(self.root, text="Email ID", font= ("goudy old style",20,"bold"),bg="white").place(x=10,y=140)
		l_gender = Label(self.root, text="Gender", font= ("goudy old style",20,"bold"),bg="white").place(x=10,y=180)
		l_dob = Label(self.root, text="D.O.B(dd-mm-yyyy)", font= ("goudy old style",20,"bold"),bg="white").place(x=600,y=60)
		l_mobile = Label(self.root, text="Contact No", font= ("goudy old style",20,"bold"),bg="white").place(x=600,y=100)
		l_vehicleclass = Label(self.root, text="Class of Vehicle", font= ("goudy old style",20,"bold"),bg="white").place(x=600,y=140)
		l_validupto = Label(self.root, text="Valid Upto", font= ("goudy old style",20,"bold"),bg="white").place(x=600,y=180)
		l_state = Label(self.root, text="State", font= ("goudy old style",20,"bold"),bg="white").place(x=10,y=220)
		l_city = Label(self.root, text="City", font= ("goudy old style",20,"bold"),bg="white").place(x=450,y=220)
		l_pincode = Label(self.root, text="Pincode", font= ("goudy old style",20,"bold"),bg="white").place(x=750,y=220)
		l_address = Label(self.root, text="Address", font= ("goudy old style",20,"bold"),bg="white").place(x=10,y=260)

        
		# Variables
		self.var_dlllnum = StringVar()
		self.var_ownernm = StringVar()
		self.var_gender = StringVar()
		self.var_dob = StringVar()
		self.var_vehicleclass = StringVar()
		self.var_validupto = StringVar()
		self.var_state = StringVar()
		self.var_city = StringVar()
		self.var_pincode = StringVar()
		self.var_address = StringVar()
		self.var_mobile = StringVar()
		self.var_email = StringVar()
		self.var_search = StringVar()

		# Entry Fields
		self.txt_dlllnum = Entry(self.root,textvariable = self.var_dlllnum,font= ("goudy old style",15),bg='lightyellow')
		self.txt_dlllnum.place(x=200,y=60,width=200)

		self.txt_ownernm = Entry(self.root,textvariable = self.var_ownernm, font= ("goudy old style",15),bg='lightyellow')
		self.txt_ownernm.place(x=200,y=100,width=200)

		self.txt_gender = Entry(self.root,textvariable = self.var_gender, font= ("goudy old style",15),bg='lightyellow')
		self.txt_gender.place(x=200,y=180,width=200)

		self.txt_vehicleclass= ttk.Combobox(self.root,textvariable = self.var_vehicleclass, font= ("goudy old style",15),values=("Select Vehicle Type","Two Wheeler", "Four Wheeler"),state = 'readonly')
		self.txt_vehicleclass.place(x=850,y=140,width=200)
		self.txt_vehicleclass.current(0)

		self.txt_dob = Entry(self.root,textvariable = self.var_dob, font= ("goudy old style",15),bg='lightyellow')
		self.txt_dob.place(x=850,y=60,width=200)

		self.txt_mobile = Entry(self.root,textvariable = self.var_mobile, font= ("goudy old style",15),bg='lightyellow')
		self.txt_mobile.place(x=850,y=100,width=200)

		self.txt_email = Entry(self.root,textvariable = self.var_email, font= ("goudy old style",15),bg='lightyellow')
		self.txt_email.place(x=200,y=140,width=200)
        
		self.txt_validupto = Entry(self.root,textvariable = self.var_validupto, font= ("goudy old style",15),bg='lightyellow')
		self.txt_validupto.place(x=850,y=180,width=200)
        
		self.txt_state = Entry(self.root,textvariable = self.var_state, font= ("goudy old style",15),bg='lightyellow')
		self.txt_state.place(x=200,y=220,width=200)
        
		self.txt_city = Entry(self.root,textvariable = self.var_city, font= ("goudy old style",15),bg='lightyellow')
		self.txt_city.place(x=510,y=220,width=200)
        
		self.txt_pincode = Entry(self.root,textvariable = self.var_pincode, font= ("goudy old style",15),bg='lightyellow')
		self.txt_pincode.place(x=900,y=220,width=200)
        
		self.txt_address = Entry(self.root,textvariable = self.var_address, font= ("goudy old style",15),bg='lightyellow')
		self.txt_address.place(x=200,y=260,width=600,height=100)

		# Buttons
		self.btn_add = Button(self.root,text="ADD",font= ("goudy old style",15,"bold"), bg="#2196f3",fg = "white",command= self.add)
		self.btn_add.place(x=60,y=400,width=100)

		self.btn_update = Button(self.root,text="UPDATE",font= ("goudy old style",15,"bold"), bg="#4caf50",fg = "white", command= self.update)
		self.btn_update.place(x=180,y=400,width=100)

		self.btn_delete = Button(self.root,text="DELETE",font= ("goudy old style",15,"bold"), bg="#f44336",fg = "white", command= self.delete)
		self.btn_delete.place(x=300,y=400,width=100)

		self.btn_clear = Button(self.root,text="CLEAR",font= ("goudy old style",15,"bold"), bg="#607d8b",fg = "white",command= self.clear)
		self.btn_clear.place(x=420,y=400,width=100)

		#search panel
		l_search = Label(self.root, text="Search By | DL/LL No  :", font= ("goudy old style",15,"bold"),bg="white").place(x=600,y=400)

		txt_search = Entry(self.root,textvariable = self.var_search,font= ("goudy old style",15),bg='lightyellow').place(x=800,y=400,width=200)

		btn_search = Button(self.root,text="Search",font= ("goudy old style",15,"bold"), bg="#03a9f4",fg = "white", command= self.search).place(x=1030,y=400,width=120)


		# Content
		self.R_Frame = Frame(self.root, bd=2, relief =RIDGE)
		self.R_Frame.place(x=10, y=450, width=1175, height=245)

		scrolly = Scrollbar(self.R_Frame, orient=VERTICAL)
		scrollx = Scrollbar(self.R_Frame, orient=HORIZONTAL)
		self.DrivingLicenseTable = ttk.Treeview(self.R_Frame,columns=("dlllnum","ownernm","email","gender","dob","mobile","vehicleclass","validupto","state","city","pincode","address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
		scrollx.pack(side= BOTTOM, fill=X )
		scrolly.pack(side= RIGHT, fill=Y )
		scrollx.config(command=self.DrivingLicenseTable.xview)
		scrolly.config(command=self.DrivingLicenseTable.yview)

		self.DrivingLicenseTable.heading("dlllnum",text="DL/LL Number")
		self.DrivingLicenseTable.heading("ownernm",text="Name")
		self.DrivingLicenseTable.heading("email",text="Email id")
		self.DrivingLicenseTable.heading("gender",text="Gender")
		self.DrivingLicenseTable.heading("dob",text="D.O.B")
		self.DrivingLicenseTable.heading("mobile",text="Mobile")
		self.DrivingLicenseTable.heading("vehicleclass",text="C.O.V")
		self.DrivingLicenseTable.heading("validupto",text="Valid Upto")
		self.DrivingLicenseTable.heading("state",text="State")
		self.DrivingLicenseTable.heading("city",text="City")
		self.DrivingLicenseTable.heading("pincode",text="Pin Code")
		self.DrivingLicenseTable.heading("address",text="Address")


		self.DrivingLicenseTable["show"]='headings'

		self.DrivingLicenseTable.column("dlllnum",width=50)
		self.DrivingLicenseTable.column("ownernm",width=50)
		self.DrivingLicenseTable.column("email",width=50)
		self.DrivingLicenseTable.column("gender",width=50)
		self.DrivingLicenseTable.column("dob",width=50)
		self.DrivingLicenseTable.column("mobile",width=50)
		self.DrivingLicenseTable.column("vehicleclass",width=50)
		self.DrivingLicenseTable.column("validupto",width=50)
		self.DrivingLicenseTable.column("state",width=50)
		self.DrivingLicenseTable.column("city",width=50)
		self.DrivingLicenseTable.column("pincode",width=50)
		self.DrivingLicenseTable.column("address",width=50)



		self.DrivingLicenseTable.pack(fill=BOTH, expand=1)
		self.DrivingLicenseTable.bind("<ButtonRelease-1>",self.get_data)
		self.show()


	def get_data(self,ev):
		self.txt_dlllnum.config(state='readonly')
		self.txt_vehicleclass.config(state='disabled')

		r=self.DrivingLicenseTable.focus()
		content=self.DrivingLicenseTable.item(r)
		row=content["values"]
		
		self.var_dlllnum.set(row[0])
		self.var_ownernm.set(row[1])
		self.var_email.set(row[2])
		self.var_gender.set(row[3])
		self.var_dob.set(row[4])
		self.var_mobile.set(row[5])
		self.var_vehicleclass.set(row[6])
		self.var_validupto.set(row[7])
		self.var_state.set(row[8])
		self.var_city.set(row[9])
		self.var_pincode.set(row[10])
		self.var_address.set(row[11])


	def add(self):

		con= sqlite3.connect(database ="RTO.db")
		cur=con.cursor()

		try:
			if self.var_dlllnum.get()=="":
				messagebox.showerror("Error !","DL/LL Number is required", parent = self.root)

			elif self.var_ownernm.get()=="":
				messagebox.showerror("Error !","Owner Name is required", parent = self.root)

			elif self.var_email.get()=="":
				messagebox.showerror("Error !","Email id is required", parent = self.root)

			elif self.var_gender.get()=="":
				messagebox.showerror("Error !","Gender not Selected", parent = self.root)

			elif self.var_dob.get()=="":
				messagebox.showerror("Error !","D.O.B is required", parent = self.root)

			elif self.var_mobile.get()=="":
				messagebox.showerror("Error !","Mobile No is required", parent = self.root)

			elif self.var_vehicleclass.get()=="":
				messagebox.showerror("Error !","Vehicle Class is required", parent = self.root)
                
			elif self.var_validupto.get()=="":
				messagebox.showerror("Error !","Validity Date is required", parent = self.root)
                
			elif self.var_state.get()=="":
				messagebox.showerror("Error !","Resident state is required", parent = self.root)
                
			elif self.var_city.get()=="":
				messagebox.showerror("Error !","Resident city is required", parent = self.root)
                
			elif self.var_pincode.get()=="":
				messagebox.showerror("Error !","Resident pincode is required", parent = self.root)
                
			elif self.var_address.get()=="":
				messagebox.showerror("Error !","Resident address is required", parent = self.root) 
            
			else:
				cur.execute("Select * from Dri_Registration where dlllnum=?",(self.var_dlllnum.get(),))
				row=cur.fetchone()

				if row!=None:
					messagebox.showerror("Error !","DL/LL Number already exists", parent = self.root)

				else:
					cur.execute("insert into Dri_Registration(dlllnum,ownernm,gender,dob,vehicleclass,validupto,state,city,pincode,address,mobile,email) values(?,?,?,?,?,?,?,?,?,?,?,?)", (
						self.var_dlllnum.get(),
		                                self.var_ownernm.get(),
		                                self.var_gender.get(),
		                		self.var_dob.get(),
		                		self.var_vehicleclass.get(),
		                		self.var_validupto.get(),
		                		self.var_state.get(),
		                		self.var_city.get(),
		                		self.var_pincode.get(),
		                		self.var_address.get(),
		                		self.var_mobile.get(),
		                		self.var_email.get(),
						))
					con.commit()
					messagebox.showinfo("Success","Record Added Successfully !",parent =self.root)
					self.show()

		except Exception as ex:
			messagebox.showerror("Error !",f"Error due to {str(ex)}")
	
	def show(self):

		con= sqlite3.connect(database ="RTO.db")
		cur=con.cursor()

		try:
			cur.execute("Select * from Dri_Registration")
			rows=cur.fetchall()
			self.DrivingLicenseTable.delete(*self.DrivingLicenseTable.get_children())
			for row in rows:
				self.DrivingLicenseTable.insert('',END,values=row)

			
		except Exception as ex:
			messagebox.showerror("Error !",f"Error due to {str(ex)}")



	def update(self):

		con= sqlite3.connect(database ="RTO.db")
		cur=con.cursor()

		try:
			if self.var_dlllnum.get()=="":
				messagebox.showerror("Error !","DL/LL Number is required", parent = self.root)

			elif self.var_ownernm.get()=="":
				messagebox.showerror("Error !","Owner Name is required", parent = self.root)

			elif self.var_email.get()=="":
				messagebox.showerror("Error !","Email id is required", parent = self.root)

			elif self.var_gender.get()=="":
				messagebox.showerror("Error !","Gender not Selected", parent = self.root)

			elif self.var_dob.get()=="":
				messagebox.showerror("Error !","D.O.B is required", parent = self.root)

			elif self.var_mobile.get()=="":
				messagebox.showerror("Error !","Mobile No is required", parent = self.root)

			elif self.var_vehicleclass.get()=="":
				messagebox.showerror("Error !","Vehicle Class is required", parent = self.root)
                
			elif self.var_validupto.get()=="":
				messagebox.showerror("Error !","Validity Date is required", parent = self.root)
                
			elif self.var_state.get()=="":
				messagebox.showerror("Error !","Resident state is required", parent = self.root)
                
			elif self.var_city.get()=="":
				messagebox.showerror("Error !","Resident city is required", parent = self.root)
                
			elif self.var_pincode.get()=="":
				messagebox.showerror("Error !","Resident pincode is required", parent = self.root)
                
			elif self.var_address.get()=="":
				messagebox.showerror("Error !","Resident address is required", parent = self.root) 
			else:

				cur.execute("Select * from Dri_Registration where dlllnum=?",(self.var_dlllnum.get(),))
				row=cur.fetchone()

				if row==None:
					messagebox.showerror("Error !","Select the data to be updated from the list", parent = self.root)

				else:
					cur.execute("update Dri_Registration set ownernm=?,gender=?,dob=?,vehicleclass=?,validupto=?,state=?,city=?,pincode=?,address=?,mobile=?,email=? where dlllnum=?", (
		                		self.var_ownernm.get(),
		                		self.var_gender.get(),
		                		self.var_dob.get(),
		              			self.var_vehicleclass.get(),
		                		self.var_validupto.get(),
		                		self.var_state.get(),
		                		self.var_city.get(),
		                		self.var_pincode.get(),
		                		self.var_address.get(),
		                		self.var_mobile.get(),
		                		self.var_email.get(),
                        			self.var_dlllnum.get(),
						))
					con.commit()
					messagebox.showinfo("Success","Record Updated Successfully !",parent =self.root)
					self.show()

		except Exception as ex:
			messagebox.showerror("Error !",f"Error due to {str(ex)}")

	def delete(self):
		con= sqlite3.connect(database ="RTO.db")
		cur=con.cursor()

		try:
			if self.var_dlllnum.get()=="":
				messagebox.showerror("Error !","DL/LL Number is required", parent = self.root)

			elif self.var_ownernm.get()=="":
				messagebox.showerror("Error !","Owner Name is required", parent = self.root)

			elif self.var_email.get()=="":
				messagebox.showerror("Error !","Email id is required", parent = self.root)

			elif self.var_gender.get()=="":
				messagebox.showerror("Error !","Gender not Selected", parent = self.root)

			elif self.var_dob.get()=="":
				messagebox.showerror("Error !","D.O.B is required", parent = self.root)

			elif self.var_mobile.get()=="":
				messagebox.showerror("Error !","Mobile No is required", parent = self.root)

			elif self.var_vehicleclass.get()=="":
				messagebox.showerror("Error !","Vehicle Class is required", parent = self.root)
                
			elif self.var_validupto.get()=="":
				messagebox.showerror("Error !","Validity Date is required", parent = self.root)
                
			elif self.var_state.get()=="":
				messagebox.showerror("Error !","Resident state is required", parent = self.root)
                
			elif self.var_city.get()=="":
				messagebox.showerror("Error !","Resident city is required", parent = self.root)
                
			elif self.var_pincode.get()=="":
				messagebox.showerror("Error !","Resident pincode is required", parent = self.root)
                
			elif self.var_address.get()=="":
				messagebox.showerror("Error !","Resident address is required", parent = self.root) 

			else:

				cur.execute("Select * from Dri_Registration where dlllnum=?",(self.var_dlllnum.get(),))
				row=cur.fetchone()

				if row==None:
					messagebox.showerror("Error !","Select the data to be deleted from the list", parent = self.root)

				else:
					op=messagebox.askyesno("Confirm","Do you want to delete the record",parent= self.root)
					if op==True:
						cur.execute("delete from Dri_Registration where dlllnum=?",(self.var_dlllnum.get(),))
						con.commit()	
						messagebox.showinfo("Success","Record Deleted Successfully !",parent=self.root)
						self.clear()

		except Exception as ex:
			messagebox.showerror("Error !",f"Error due to {str(ex)}")

	def search(self):
		con= sqlite3.connect(database ="RTO.db")
		cur=con.cursor()

		try:
			cur.execute(f"Select * from Dri_Registration where dlllnum=?" ,(self.var_dlllnum.get(),))
			rows=cur.fetchone()
			if rows !=None:
				self.DrivingLicenseTable.delete(*self.DrivingLicenseTable.get_children())
				for row in rows:
					self.DrivingLicenseTable.insert('',END,values=row)
				else:
					messagebox.showerror("Error","No Record found",parent=self.root)
			
		except Exception as ex:
			messagebox.showerror("Error !",f"Error due to {str(ex)}")


	def clear(self):
		self.show()
		self.txt_dlllnum.config(state='normal')
		self.txt_vehicleclass.config(state='normal')
		self.var_dob.set("")
		self.var_ownernm.set(""),
		self.var_vehicleclass.set("Select C.O.V"),
		self.var_gender.set(""),
		self.var_mobile.set(""),
		self.var_email.set(""),
		self.var_validupto.set("")
		self.var_state.set("")
		self.var_city.set("")
		self.var_pincode.set("")
		self.var_address.set("")
		self.var_search.set("")

if __name__ == "__main__":

	root=Tk()
	obj = DriClass(root)
	root.mainloop()