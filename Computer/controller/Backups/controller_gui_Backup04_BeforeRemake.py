from Tkinter import *
from Computer.controller.test import test

from Computer.controller.command_get import getStart

class GUI(Frame):


    def __init__(self, master=None):
        self.i = 0
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.set_main_variables()
        self.update()

    def createWidgets(self):
        
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        self.A = Label(self)
        self.A["bg"] = "red"
        self.A["text"] = "A: Unpressed"
        self.A["width"] = 5
        self.A["height"] = 2
        
    def set_main_variables(self):
        self.buttons= []
    
    def update (self):
        if self.i == 0:
            self.i = self.i + 1
            self.master.after(100, self.update)
        else:
            self.master.after(100, self.update)
            getStart()
            
if __name__ == "__main__":
    root = Tk()
    app = GUI(master=root)
    app.master.title("My Do-Nothing Application")
    app.mainloop()

    root.destroy()
