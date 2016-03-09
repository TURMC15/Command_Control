from Tkinter import *
import re
from time import sleep
from msvcrt import kbhit
import re
import pywinusb.hid as hid
from _random import Random
from Computer.controller.sendToP import test
from Computer.controller.sendToA import sendToA
from threading import Thread
class GUI(Frame):


    def __init__(self, master=None):
                
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.set_main_variables()
        self.update()

    def createWidgets(self):
        
        self.A = Label(self)
        self.A["bg"] = "red"
        self.A["text"] = "A"
        self.A["width"] = 5
        self.A["height"] = 2
        self.A.grid(row = 0, column = 0)
        
        self.B = Label(self)
        self.B["bg"] = "red"
        self.B["text"] = "B"
        self.B["width"] = 5
        self.B["height"] = 2
        self.B.grid(row = 20, column = 0)
        
        self.X = Label(self)
        self.X["bg"] = "red"
        self.X["text"] = "X"
        self.X["width"] = 5
        self.X["height"] = 2
        self.X.grid(row = 40, column = 0)
        
        self.Y = Label(self)
        self.Y["bg"] = "red"
        self.Y["text"] = "Y"
        self.Y["width"] = 5
        self.Y["height"] = 2
        self.Y.grid(row = 60, column = 0)
        
        self.LAP = Label(self)
        self.LAP["bg"] = "red"
        self.LAP["text"] = "LAP"
        self.LAP["width"] = 5
        self.LAP["height"] = 2
        self.LAP.grid(row = 0, column = 40)
        
        self.RAP = Label(self)
        self.RAP["bg"] = "red"
        self.RAP["text"] = "RAP"
        self.RAP["width"] = 5
        self.RAP["height"] = 2
        self.RAP.grid(row = 20, column = 40)
        
        self.UP = Label(self)
        self.UP["bg"] = "red"
        self.UP["text"] = "UP"
        self.UP["width"] = 5
        self.UP["height"] = 2
        self.UP.grid(row = 0, column = 60)
           
        self.UR = Label(self)
        self.UR["bg"] = "red"
        self.UR["text"] = "UR"
        self.UR["width"] = 5
        self.UR["height"] = 2
        self.UR.grid(row = 20, column = 60)
        
        self.R = Label(self)
        self.R["bg"] = "red"
        self.R["text"] = "R"
        self.R["width"] = 5
        self.R["height"] = 2
        self.R.grid(row = 40, column = 60)
        
        self.RD = Label(self)
        self.RD["bg"] = "red"
        self.RD["text"] = "RD"
        self.RD["width"] = 5
        self.RD["height"] = 2
        self.RD.grid(row = 60, column = 60)
        
        self.D = Label (self)
        self.D["bg"] = "red"
        self.D["text"] = "D"
        self.D["width"] = 5
        self.D["height"] = 2
        self.D.grid(row = 0, column = 80)
        
        self.DL = Label(self)
        self.DL["bg"] = "red"
        self.DL["text"] = "DL"
        self.DL["width"] = 5
        self.DL["height"] = 2
        self.DL.grid(row = 20, column = 80)
            
        self.L = Label(self)
        self.L["bg"] = "red"
        self.L["text"] = "L"
        self.L["width"] = 5
        self.L["height"] = 2
        self.L.grid(row = 40, column = 80)
        
        self.LU = Label(self)
        self.LU["bg"] = "red"
        self.LU["text"] = "LU"
        self.LU["width"] = 5
        self.LU["height"] = 2
        self.LU.grid(row = 60, column = 80)
        
        self.RB = Label(self)
        self.RB["bg"] = "red"
        self.RB["text"] = "RB"
        self.RB["width"] = 5
        self.RB["height"] = 2
        self.RB.grid(row = 0, column = 100)
        
        self.LB = Label(self)
        self.LB["bg"] = "red"
        self.LB["text"] = "LB"
        self.LB["width"] = 5
        self.LB["height"] = 2
        self.LB.grid(row = 20, column = 100)
           
        self.LAY = Label(self)
        self.LAY["bg"] = "red"
        self.LAY["text"] = "0"
        self.LAY["width"] = 5
        self.LAY["height"] = 2
        self.LAY.grid(row = 0, column = 120)
        
        self.LAX = Label(self)
        self.LAX["bg"] = "red"
        self.LAX["text"] = "0"
        self.LAX["width"] = 5
        self.LAX["height"] = 2
        self.LAX.grid(row = 20, column = 120)
        
        self.RAY = Label(self)
        self.RAY["bg"] = "red"
        self.RAY["text"] = "0"
        self.RAY["width"] = 5
        self.RAY["height"] = 2
        self.RAY.grid(row = 0, column = 140)
        
        self.RAX = Label(self)
        self.RAX["bg"] = "red"
        self.RAX["text"] = "0"
        self.RAX["width"] = 5
        self.RAX["height"] = 2
        self.RAX.grid(row = 20, column = 140)
        
        self.LT = Label(self)
        self.LT["bg"] = "red"
        self.LT["text"] = "0"
        self.LT["width"] = 5
        self.LT["height"] = 2
        self.LT.grid(row = 40, column = 20)
        
        self.RT = Label(self)
        self.RT["bg"] = "red"
        self.RT["text"] = "0"
        self.RT["width"] = 5
        self.RT["height"] = 2
        self.RT.grid(row = 60, column = 20)
    
    def set_main_variables(self):
        self.i = 0
        
        self.button_A_Pressed = False
        self.button_B_Pressed = False
        self.button_X_Pressed = False
        self.button_Y_Pressed = False
        self.left_Analog_Pressed = False
        self.right_Analog_Pressed = False
        self.up_Pressed = False
        self.up_Right_Pressed = False
        self.right_Pressed = False
        self.right_Down_Pressed = False
        self.down_Pressed = False
        self.down_Left_Pressed = False
        self.left_Pressed = False
        self.left_Up_Pressed = False
        self.right_Bumper_Pressed = False
        self.left_Bumper_Pressed = False        
        
        self.left_Analog_Y  = 0
        self.left_Analog_X = 0
        self.right_Analog_Y = 0
        self.right_Analog_X = 0
        self.left_Trigger = 0
        self.right_Trigger = 0
       
    def update (self):
            string = ""
            if self.i == 0:
                self.i = self.i + 1
                self.getStart()
                
                
            if self.button_A_Pressed:
                self.A["bg"] = "blue"
                string = "A"
            else:
                self.A["bg"] = "red"
                string = "0"
                
            if self.button_B_Pressed:
                self.B["bg"] = "blue"
                string = string + " B"
            else:
                self.B["bg"] = "red"
                string = string + " 0"
                
            if self.button_X_Pressed:
                self.X["bg"] = "blue"
                string = string + " X"
            else:
                self.X["bg"] = "red"
                string = string + " 0"
                
            if self.button_Y_Pressed:
                self.Y["bg"] = "blue"
                string = string + " Y"
            else:
                self.Y["bg"] = "red"
                string = string + " 0"
            
            if self.left_Analog_Pressed:
                self.LAP["bg"] = "blue"
                string =string + " LAP"
            else:
                self.LAP["bg"] = "red"
                string = string + " 0"
            
            if self.right_Analog_Pressed:
                self.RAP["bg"] = "blue"
                string = string + " RA"
            else:
                self.RAP["bg"] = "red"
                string = string + " 0"
                
            if self.up_Pressed:
                self.UP["bg"] = "blue"
                string = string + " U"
            else:
                self.UP["bg"] = "red"
                string = string + " 0"
                
            if self.up_Right_Pressed:
                self.UR["bg"] = "blue"
                string = string + " UR"
            else:
                self.UR["bg"] = "red"
                string = string + " 0"
                
            if self.right_Pressed:
                self.R["bg"] = "blue"
                string = string + " R"
            else:
                self.R["bg"] = "red"
                string = string + " 0"
                
            if self.right_Down_Pressed:    
                self.RD["bg"] = "blue"
                string = string + " RD"
            else:
                self.RD["bg"] = "red"
                string = string + " 0"
                
            if self.down_Pressed:
                self.D["bg"] = "blue"
                string = string + " D"
            else:
                self.D["bg"] = "red"
                string = string + " 0"
                
            if self.down_Left_Pressed:
                self.DL["bg"] = "blue"
                string = string + " DL"
            else:
                self.DL["bg"] = "red"
                string = string + " 0"
                
            if self.left_Pressed:
                self.L["bg"] = "blue"
                string = string + " L"
            else:
                self.L["bg"] = "red"
                string = string + " 0"
                
            if self.left_Up_Pressed:
                self.LU["bg"] = "blue"
                string = string + " LU"
            else:
                self.LU["bg"] = "red"
                string = string + " 0"
                
            if self.right_Bumper_Pressed:
                self.RB["bg"] = "blue"
                string = string + " RB"
            else:
                self.RB["bg"] = "red"
                string = string + " 0"
                
            if self.left_Bumper_Pressed:
                self.LB["bg"] = "blue"
                string = string + " LB"
            else:
                self.LB["bg"] = "red"
                string = string + " 0"
                
                
            self.LAY["text"] = self.left_Analog_Y
            self.LAX["text"] = self.left_Analog_X
            self.RAY["text"] = self.right_Analog_Y
            self.RAX["text"] = self.right_Analog_X
            
            self.LT["text"] = self.left_Trigger
            self.RT["text"] = self.right_Trigger
            
            string = string + " "
            string = string + str(self.left_Analog_X)

            string = string + " "
            string = string + str(self.left_Analog_Y)

            string = string + " "
            string = string + str(self.right_Analog_X)

            string = string + " "
            string = string + str(self.right_Analog_Y)

            string = string + " "
            string = string + str(self.left_Trigger)

            string = string + " "
            string = string + str(self.right_Trigger)
        
            test(string, "Hello")
            
    def getStart(self):
        all_hids = hid.find_all_hid_devices()
        self.device = all_hids[0]
        self.device.open()
        self.device.set_raw_data_handler(self.interpret)
        
    def interpret (self, data):
        dpadAndAnalog = int(data[12])
        # Dpad and Analog buttons
        if dpadAndAnalog != 0:
            if dpadAndAnalog % 4 != 0:
                if dpadAndAnalog - 1 % 4 == 0:
                    self.left_Analog_Pressed = True
                    dpadAndAnalog -= 1
                else:
                    self.left_Analog_Pressed = False
                    
                if (dpadAndAnalog - 2) % 4 == 0:
                    self.right_Analog_Pressed = True
                    dpadAndAnalog -= 2
                else:
                    self.right_Analog_Pressed = False
            else:
                self.left_Analog_Pressed = False
                self.right_Analog_Pressed = False
        
        if dpadAndAnalog != 0:
            if dpadAndAnalog == 4:
                self.up_Pressed = True
            else:
                self.up_Pressed = False
            
            if dpadAndAnalog == 8:
                self.up_Right_Pressed = True
            else:
                self.up_Right_Pressed = False
            
            if dpadAndAnalog == 12:
                self.right_Pressed = True
            else:
                self.right_Pressed = False
                
            if dpadAndAnalog == 16:
                self.right_Down_Pressed = True
            else:    
                self.right_Down_Pressed = False
                
            if dpadAndAnalog == 20:
                self.down_Pressed = True
            else:        
                self.down_Pressed = False
                
            if dpadAndAnalog == 24:
                self.down_Left_Pressed = True
            else:    
                self.down_Left_Pressed = False
                
            if dpadAndAnalog == 28:
                self.left_Pressed = True
            else:    
                self.left_Pressed = False
                
            if dpadAndAnalog == 32:
                self.left_Up_Pressed = True
            else:
                self.left_Up_Pressed = False
                
        # A, B, X, Y buttons, Bumpers, Select and Start buttons
        bumpersABXYSelectStart = int(data[11])
        if bumpersABXYSelectStart != 0:
            if bumpersABXYSelectStart - 128 >= 0:
                self.start_Pressed = True
                bumpersABXYSelectStart -= 128
            else:
                self.start_Pressed = False
            
            if  bumpersABXYSelectStart - 64 >= 0:
                self.select_Pressed = True
                bumpersABXYSelectStart -= 64
            else:
                self.select_Pressed = False
            
            if bumpersABXYSelectStart - 32 >= 0:
                self.right_Bumper_Pressed = True
                bumpersABXYSelectStart -= 32
            else:
                self.right_Bumper_Pressed = False
            
            if bumpersABXYSelectStart - 16 >= 0:
                self.left_Bumper_Pressed = True
                bumpersABXYSelectStart -= 16
            else:
                self.left_Bumper_Pressed = False
                
            if bumpersABXYSelectStart - 8 >= 0:
                self.button_Y_Pressed = True
                bumpersABXYSelectStart -= 8
            else:
                self.button_Y_Pressed = False
            
            if bumpersABXYSelectStart - 4 >= 0:
                self.button_X_Pressed = True
                bumpersABXYSelectStart -= 4
            else:
                self.button_X_Pressed = False
            
            if bumpersABXYSelectStart - 2 >= 0:
                self.button_B_Pressed = True
                bumpersABXYSelectStart -= 2
            else:
                self.button_B_Pressed = False
                
            if bumpersABXYSelectStart - 1 >= 0:
                self.button_A_Pressed = True
            else:    
                self.button_A_Pressed = False
                
            # Triggers, probably should be used for drill extension retraction. Will probably implement a dead-zone for safety
            trigger = int(data[10])
            if trigger != 128:
                if trigger > 128:
                    self.left_Trigger = trigger - 128
            
                if trigger < 128:
                    self.right_Trigger = 128 - trigger
            else:
                self.left_Trigger = 0
                self.right_Trigger = 0
        
            # Analog Joysticks. As far as I can tell we need to use the average of the values. Will probably implement a dead-zone for safety
            # Left Analog Joystick Y-axis
            temp = (int(data[3]) + int(data[4])) / 2
            self.left_Analog_Y = temp
        
            # Left Analog Joystick X-axis
            temp = (int(data[1]) + int(data[2])) / 2
            self.left_Analog_X = temp
        
            # Right Analog Joystick Y-axis
            temp = (int(data[7]) + int(data[8])) / 2
            self.right_Analog_Y = temp
        
            # Right Analog Joystick X-axis
            temp = (int(data[5]) + int(data[6])) / 2
            self.right_Analog_X = temp
            
            self.update()
     

if __name__ == "__main__":
    root = Tk()
    app = GUI(master=root)
    app.master.title("My Do-Nothing Application")
    app.mainloop()
    root.destroy()
