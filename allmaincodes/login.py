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
        self.bg=ImageTk.PhotoImage(file="E:\\pythonprojects\\djangoprojects\\images\\supermarket pic5.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)



#===========login frame====================================================================================================================================================
        Frame_call_login=Frame(self.root,bg="white")
        Frame_call_login.place(x=530,y=100,height=340,width=500)

        title=Label(Frame_call_login,text="LOGIN HERE",font=("impact",30,"bold"),fg="#d77337",bg='white').place(x=90,y=30)
        desc=Label(Frame_call_login,text="Admin Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg='white').place(x=90,y=100)
        lbl_user= Label(Frame_call_login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray",
                     bg='white').place(x=90, y=140)
        self.txt_user=Entry(Frame_call_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)



        lbl_pass = Label(Frame_call_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg='white').place(x=90, y=210)
        self.txt_pass = Entry(Frame_call_login, font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=90, y=240, width=350, height=35)





       # forget_btn=Button(Frame_call_login,text="Forget Password ?",bg="white",fg="#d77337",bd=0,font=("time new roman",12)).place(x=90,y=280)
        login_btn= Button(self.root,command=self.login_function, text="Login", fg="white", bg="#d77337",
                        font=("time new roman", 20)).place(x=825, y=385,width=180,height=40)

 #============================================================================================================================================================================
    def login_function(self):
        if self.txt_pass.get()==""or self.txt_user.get()=="":
            messagebox.showerror("Error","All Keys Are Required",parent=self.root)
        elif self.txt_pass.get() == "1234" and self.txt_user.get() == "rohan"or self.txt_pass.get() == "1234" and self.txt_user.get() == "yash":

            messagebox.showinfo("welcom", f"welcome{self.txt_user.get()}\nYour password:{self.txt_pass.get()}",
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