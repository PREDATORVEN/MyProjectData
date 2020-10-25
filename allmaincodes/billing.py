from tkinter import *
class call_bill_online:

    def __init__(self,root):
        self.root=root

        self.root.title("SUPER MARKET SOFTWARE")
        pad = 3
        self._geom ='200x200+0+0'
        root.geometry("{0}x{1}+0+0".format(
        root.winfo_screenwidth() - pad, root.winfo_screenheight() - pad))
        root.bind('<Escape>', self.toggle_geom)
        bg_color="#633507"
        h7 = LabelFrame(self.root,text=('BILL'),font=("family of roman", 30, "bold"),fg="grey", bd=12,relief=GROOVE)
        h7.place(x=5,y=0,width=1520,height=790)
#--------------------------------------------------------------------------------------------------------------------------------------------------
    def toggle_geom(self, event):
        geom = self.root.winfo_geometry()
        print(geom, self._geom)
        self.root.geometry(self._geom)
        self._geom = geom
root = Tk()
x = call_bill_online(root)
root.mainloop()