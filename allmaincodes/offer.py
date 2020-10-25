from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
class call_offer:
    def __init__(self, root):
        self.root=root
        self.root.title("offer system")
        pad = 3
        self._geom = '200x200+0+0'
        root.geometry("{0}x{1}+0+0".format(
            root.winfo_screenwidth()-pad,root.winfo_screenheight()-pad,))
        root.bind('<Escape>', self.toggle_geom)
        self.root.resizable(False,False)
#===================BG image================================================================================================================================================
        self.bg=ImageTk.PhotoImage(file="E:\\pythonprojects\\djangoprojects\\images\\offer4.jpg")
        self.bg_image=Label(self.root,image=self.bg,).place(x=10,y=0,relwidth=1,relheight=1)
#====================================================================================================================================================================================


    #=================================================================================================================================================================================
    def toggle_geom(self, event):
        geom = self.root.winfo_geometry()
        print(geom, self._geom)
        self.root.geometry(self._geom)
        self._geom = geom



root=Tk()
obj=call_offer(root)
root.mainloop()