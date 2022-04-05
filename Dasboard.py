from tkinter import *
import tkinter.messagebox
from tkinter import ttk,messagebox
import random
import time
import datetime
import sqlite3
from tkmacosx import Button
from PIL import Image,ImageTk


class Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.title("RTO Management System")
        self.root.geometry("1200x700+100+100")
        self.root.config(bg="alice blue")

        # BG Image
        self.bg_dash = ImageTk.PhotoImage(file="Images/bg_dash.png")
        bg1 = Label(self.root, image= self.bg_dash).place(x=0,y=0,width=1200,height=630)
        bg2 = Label(self.root,bg="gray29").place(x=0,y=625,width=1200,height=80)

        dashboard_frame = LabelFrame(self.root,text="Services",font=("times new roman",30,"bold"),bg="light blue",)
        dashboard_frame.place(x=20, y=20 ,width= 500, height= 200)

        btn_veh_reg = Button(dashboard_frame,text="Vehicle Registration",font=("times new roman",20),bg="peach puff",bd=0).place(x=150,y=20)
        btn_lic = Button(dashboard_frame,text="Manage License",font=("times new roman",20),bg="peach puff",bd=0).place(x=170,y=80)

root = Tk()
obj = Dashboard(root)
root.mainloop()