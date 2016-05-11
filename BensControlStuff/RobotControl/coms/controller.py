from Tkinter import *
from math import atan2
from math import sqrt
from math import floor
from math import pow
from math import degrees
from time import sleep
from msvcrt import kbhit
from wheels import *
import re
import pywinusb.hid as hid
from threading import Thread
import socket
from ctypes import *
import binascii

class GUI(Frame):

    def __init__(self, master=None):
                
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.set_main_variables()
        self.update()


    """
        Creates the GUI elements 
        These display which button on the controller is pressed
    """
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
        
    
        
        self.UP = Label(self)
        self.UP["bg"] = "red"
        self.UP["text"] = "UP"
        self.UP["width"] = 5
        self.UP["height"] = 2
        self.UP.grid(row = 0, column = 60)
    
        self.D = Label (self)
        self.D["bg"] = "red"
        self.D["text"] = "D"
        self.D["width"] = 5
        self.D["height"] = 2
        self.D.grid(row = 0, column = 80)
           
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
    
    
    """
        Initializes the variables used 
    """
    def set_main_variables(self):
        self.i = 0
        self.INVERTX = -1
        self.stringPI = ""
        self.stringAR = ""
        self.tempPI = ""
        self.tempAR = ""
        
        self.button_A_Pressed = False
        self.button_B_Pressed = False
        
        self.up_Pressed = 0
        self.down_Pressed = 0
        
        self.left_Analog_Y  = 0
        self.left_Analog_X = 0
        self.left_Analog_Y_3 = 0
        self.left_Analog_Y_4 = 0
        self.left_Analog_X_1 = 0
        self.left_Analog_X_2 = 0
       
        self.leftTrigger = 0
        self.rightTrigger = 0
        self.rightWheel = 0
        self.leftWheel = 0
       
    
    def getStart(self):
        all_hids = hid.find_all_hid_devices()
        self.device = all_hids[0]
        self.device.open()
        self.device.set_raw_data_handler(self.interpret)
           
       
    """
        Reads the state of the variables and updates both the GUI and the String to be sent to the PI
    """
    def update (self):
            stringPI = ""
            stringAR = ""
            if self.i == 0:
                self.i = self.i + 1
                self.getStart()
                
            
            """
            Actuator, Stepper
            Two button system. Up and down on the dpad 
            and buttons A for stepper and B for actuator
            """
            if self.button_A_Pressed:
                self.A["bg"] = "blue"
                if self.up_Pressed:
                    stringAR = stringAR + "1"
                elif self.down_Pressed:
                    stringAR = stringAR + "2"
                else:
                    stringAR = stringAR + "0"
            else:
                self.A["bg"] = "red"
                stringAR = stringAR + "0"
                
            if self.button_B_Pressed:
                self.B["bg"] = "blue"
                if self.up_Pressed:
                    stringAR = stringAR + "1"
                elif self.down_Pressed:
                    stringAR = stringAR + "2"
                else:
                    stringAR = stringAR + "0"
            else:
                self.B["bg"] = "red"
                stringAR = stringAR + "0"
                
            """
            Conveyer
            """
            if self.leftTrigger:
                stringAR = stringAR + "1"
            else:
                stringAR = stringAR + "0"
            
            """
            Auger
            """
            if self.rightTrigger:
                stringAR = stringAR + "1"
            else:
                stringAR = stringAR + "0"
                    
            if self.up_Pressed:
                self.UP["bg"] = "blue"
            else:
                self.UP["bg"] = "red"
                
            if self.down_Pressed:
                self.D["bg"] = "blue"
            else:
                self.D["bg"] = "red"
                
            self.LAY["text"] = self.left_Analog_Y
            self.LAX["text"] = self.left_Analog_X
            
            
            """
            Steering
            """
            self.setWheels()
            stringPI = self.leftWheel + self.rightWheel
            self.send (stringAR, stringPI)
            
            
    def interpret (self, data):
        
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
        else:
            self.right_Bumper_Pressed = False
            self.left_Bumper_Pressed = False
            self.start_Pressed = False
            self.select_Pressed = False
            self.button_A_Pressed = False
            self.button_B_Pressed = False
            self.button_X_Pressed = False
            self.button_Y_Pressed = False



        # Dpad and Analog buttons
        dpadAndAnalog = int(data[12])
        
        #Clear the Dpad and Analog Buttons
        if dpadAndAnalog == 0:
            self.right_Analog_Pressed = False
            self.left_Analog_Pressed = False
            self.up_Pressed = False
            self.up_Right_Pressed = False
            self.right_Pressed = False
            self.right_Down_Pressed = False
            self.down_Pressed = False
            self.down_Left_Pressed = False
            self.left_Pressed = False
            self.left_Up_Pressed = False
        
        
        """
            The controller sends the information for the DPAD and Analog Buttons
            as a single integer
            
            The Left analog is added as a 1
            The Right analog is added as a 2
            Each of the directions for the DPAD is added as a power of two
            beginning with up as 4 and rotating clockwise until it reaches the
            upper-left as 32
            
            Most of these buttons will not be used
                
        """
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
        """
    Using the right analog for driving
        """
        
        #Left Analog Joystick Y-axis
        temp = int (data[3])
        self.left_Analog_Y_3
        temp = int (data[4])
        self.left_Analog_Y_4 = temp
        
        #Left Analog Joystick X-axis
        temp = int(data[1])
        self.left_Analog_X_1 = temp
        temp = int(data[2])
        self.left_Analog_X_2 = temp
        
        # Right Analog Joystick Y-axis
        temp = int(data[7])
        self.right_Analog_Y_7 = temp
        temp = int(data[8])
        self.right_Analog_Y_8 = temp
    
    
    
        # Right Analog Joystick X-axis
        temp = int(data[5])
        self.right_Analog_X_5 = temp
        temp = int(data[6])
        self.right_Analog_X_6 = temp

        """
            The Triggers are held in a single variable and added together
            
            The Right Trigger ranges from 
            The Left Trigger ranges from
            
            
        """
        trigger = int(data[10])
        
        if trigger > 205:
            self.leftTrigger = True
        
        elif trigger < 50:
            self.rightTrigger = True
        
        else:
            self.leftTrigger = False
            self.rightTrigger = False        
        
        
        
        self.update()
        

    
    def setWheels(self):
        
        result = differentialWheels(self.left_Analog_Y_4, self.left_Analog_X_2)
        
        self.leftWheel = bytearray()
        if result[0] < 0:
            if (-1 * result[0]) > 127:
                self.leftWheel.append(255)
            else:
                self.leftWheel.append((-1 * result[0]) + 128)
        elif result[0] > 127:
            self.leftWheel.append(127)
        else:
            self.leftWheel.append(result[0])
            
            
        self.rightWheel = bytearray()
        if result[1] < 0:
            if (-1 * result[1]) > 127:
                self.rightWheel.append(255)
            else:
                self.rightWheel.append(-1 * result[1] + 128)
        elif result[1] > 127:
            self.rightWheel.append(127)
        else:
            self.rightWheel.append(result[1])

        
    def send (self, stringAR, stringPI):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        UDP_IP_A = "192.168.0.103"
        UDP_PORT_A = 1111
         
        UDP_IP_P = "192.168.0.100"
        UDP_PORT_P = 8888
        
        
        if stringAR != self.tempAR:
            print (stringAR)
            MESSAGE_A = stringAR
            self.tempAR = stringAR
            sock.sendto(MESSAGE_A, (UDP_IP_A, UDP_PORT_A))
        
        if stringPI != self.tempAR:
            print (stringPI)
            MESSAGE_P = stringPI
            self.tempPI = stringPI
            sock.sendto(MESSAGE_P, (UDP_IP_P, UDP_PORT_P))
            
        
if __name__ == "__main__":
    root = Tk()
    app = GUI(master=root)
    app.master.title("GUI FOR CONTROLLER")
    app.mainloop()
    root.destroy()
    
    