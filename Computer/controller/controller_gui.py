"""
Simple GUI. Right now to see what buttons do what.
Well... RIGHT now just experimenting to learn Tkinter.
"""

from Tkinter import *
from ttk import *
class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        
        self.parent.title("Example")
        self.style = Style()
        self.style.theme_use("default")
        
        self.pack(fill=BOTH, expand = 1)
        
        canvas = Canvas(self)
        canvas.create_line(15, 25, 200, 25)
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        
        canvas.pack(fill=BOTH, expand=1)

    #def button_Pressed():

    #def change_Bar():
        

def main():
    #Create window
    root = Tk()
    root.title("Controller GUI")
    root.geometry("500x300+300+300")

    app = Example(root)
    

    #Start event loop
    root.mainloop()
    
if __name__ == '__main__':
    main()