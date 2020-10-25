from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
class call_login:
    def __init__(self, root):
        self.root=root
        self.root.title("Admin system")
        pad = 3
        self._geom = '200x200+0+0'
        root.geometry("{0}x{1}+0+0".format(
            root.winfo_screenwidth()-pad,root.winfo_screenheight()-pad))
        root.bind('<Escape>', self.toggle_geom)
        self.root.resizable(False,False)
#===================BG image================================================================================================================================================
        self.bg=ImageTk.PhotoImage(file="C://Users//Yash Sharma//PycharmProjects//firstprog//allpictures//coffee2.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)



#===========login frame====================================================================================================================================================
        Frame_call_adlogin=Frame(self.root,bg="white")
        Frame_call_adlogin.place(x=500,y=250,height=340,width=500)

        title=Label(Frame_call_adlogin,text="Admin Login Here ",font=("impact",30,"bold"),fg="#633507",bg='white').place(x=90,y=30)
        desc=Label(Frame_call_adlogin,text="Admin Login Area",font=("Goudy old style",15,"bold"),fg="#633507",bg='white').place(x=90,y=100)
        lbl_user= Label(Frame_call_adlogin, text="Username", font=("Goudy old style", 15, "bold"), fg="gray",
                     bg='white').place(x=90, y=140)
        self.txt_user=Entry(Frame_call_adlogin,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)



        lbl_pass = Label(Frame_call_adlogin, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg='white').place(x=90, y=210)
        self.txt_pass = Entry(Frame_call_adlogin, font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=90, y=240, width=350, height=35)





       # forget_btn=Button(Frame_call_login,text="Forget Password ?",bg="white",fg="#d77337",bd=0,font=("time new roman",12)).place(x=90,y=280)
        login_btn= Button(self.root,command=self.login_function, text="Login", fg="white", bg="#633507",
                        font=("time new roman", 20)).place(x=800, y=535,width=180,height=40)
        cancel_btn = Button( text="cancel", fg="#633507",bd=0, bg="white",
                           font=("time new roman", 20)).place(x=560, y=535, width=180, height=40)

 #============================================================================================================================================================================
    def login_function(self):
        if self.txt_pass.get()==""or self.txt_user.get()=="":
            messagebox.showerror("Error","All Keys Are Required",parent=self.root)
        elif self.txt_pass.get() == "1234" and self.txt_user.get() == "rohan"or self.txt_pass.get() == "1234" and self.txt_user.get() == "yash":

            messagebox.showinfo("welcome", f"welcome{self.txt_user.get()}\nYour password:{self.txt_pass.get()}",
                                parent=self.root)
        else:
            messagebox.showerror("Error", "Invalid Username/Password", parent=self.root)



    #=================================================================================================================================================================================
    def toggle_geom(self, event):
        geom = self.root.winfo_geometry()
        print(geom, self._geom)
        self.root.geometry(self._geom)
        self._geom = geom



root=Tk()
obj=call_login(root)
root.mainloop()