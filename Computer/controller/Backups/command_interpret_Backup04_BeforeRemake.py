"""
Version 0.0.1
11/30/15
@author: Ben Camp

Interpreting the data from command_get
"""
from _random import Random





def whats_pressed (list_Of_Input):
    button_A_Pressed = False
    button_B_Pressed = False
    button_X_Pressed = False
    button_Y_Pressed = False
    left_Bumper_Pressed = False
    right_Bumper_Pressed = False
    select_Pressed = False
    start_Pressed = False

    left_Analog_Pressed = False
    right_Analog_Pressed = False
    up_Pressed = False
    up_Right_Pressed = False
    right_Pressed = False
    right_Down_Pressed = False
    down_Pressed = False
    down_Left_Pressed = False
    left_Pressed = False
    left_Up_Pressed = False

    left_Analog_X = 0
    left_Analog_Y = 0
    right_Analog_X = 0
    right_Analog_Y = 0

    left_Trigger = 0
    right_Trigger = 0
    
    
    dpadAndAnalog = int(list_Of_Input[12])
    # Dpad and Analog buttons
    if dpadAndAnalog != 0:
        if dpadAndAnalog % 4 != 0:
            if dpadAndAnalog - 1 % 4 == 0:
                left_Analog_Pressed = True
                dpadAndAnalog -= 1
            elif (dpadAndAnalog - 2) % 4 == 0:
                right_Analog_Pressed = True
                dpadAndAnalog -= 2
            elif (dpadAndAnalog -3) % 4 == 0:
                left_Analog_Pressed = True
                right_Analog_Pressed = True
                dpadAndAnalog -= 3
                
        if dpadAndAnalog != 0:
            if dpadAndAnalog == 4:
                up_Pressed = True
            
            if dpadAndAnalog == 8:
                up_Right_Pressed = True
                
            if dpadAndAnalog == 12:
                right_Pressed = True
                
            if dpadAndAnalog == 16:
                right_Down_Pressed = True
                
            if dpadAndAnalog == 20:
                down_Pressed = True
                
            if dpadAndAnalog == 24:
                down_Left_Pressed = True
                
            if dpadAndAnalog == 28:
                left_Pressed = True
                
            if dpadAndAnalog == 32:
                left_Up_Pressed = True
            
    # A, B, X, Y buttons, Bumpers, Select and Start buttons
    bumpersABXYSelectStart = int(list_Of_Input[11])
    if bumpersABXYSelectStart != 0:
        if bumpersABXYSelectStart - 128 >= 0:
            start_Pressed = True
            bumpersABXYSelectStart -= 128
        
        if  bumpersABXYSelectStart - 64 >= 0:
            select_Pressed = True
            bumpersABXYSelectStart -= 64
        
        if bumpersABXYSelectStart - 32 >= 0:
            right_Bumper_Pressed = True
            bumpersABXYSelectStart -= 32
        
        if bumpersABXYSelectStart - 16 >= 0:
            left_Bumper_Pressed = True
            bumpersABXYSelectStart -= 16
        
        if bumpersABXYSelectStart - 8 >= 0:
            button_Y_Pressed = True
            bumpersABXYSelectStart -= 8
        
        if bumpersABXYSelectStart - 4 >= 0:
            button_X_Pressed = True
            bumpersABXYSelectStart -= 4
        
        if bumpersABXYSelectStart - 2 >= 0:
            button_B_Pressed = True
            bumpersABXYSelectStart -= 2
            
        if bumpersABXYSelectStart - 1 >= 0:
            button_A_Pressed = True
            
    
    # Triggers, probably should be used for drill extension retraction. Will probably implement a dead-zone for safety
    trigger = int(list_Of_Input[10])
    if trigger != 128:
        if trigger > 128:
            left_Trigger = trigger - 128
        
        if trigger < 128:
            right_Trigger = trigger
    else:
        left_Trigger = 0
        right_Trigger = 0
    
    # Analog Joysticks. As far as I can tell we need to use the average of the values. Will probably implement a dead-zone for safety
    
    # Left Analog Joystick Y-axis
    temp = (int(list_Of_Input[3]) + int(list_Of_Input[4])) / 2
    left_Analog_Y = temp
    
    # Left Analog Joystick X-axis
    temp = (int(list_Of_Input[1]) + int(list_Of_Input[2])) / 2
    left_Analog_X = temp
    
    # Right Analog Joystick Y-axis
    temp = (int(list_Of_Input[7]) + int(list_Of_Input[8])) / 2
    right_Analog_Y = temp
    
    # Right Analog Joystick X-axis
    temp = (int(list_Of_Input[5]) + int(list_Of_Input[6])) / 2
    right_Analog_X = temp
 

