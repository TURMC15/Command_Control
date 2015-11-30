"""
Interpreting the data from command_get
Version 0.0.1

Ben Camp
"""


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
upRight_Pressed = False
right_Pressed = False
rightDown_Pressed = False
down_Pressed = False
downLeft_Pressed = False
left_Pressed = False
leftUP_Pressed = False

left_Analog_X = 0
left_Analog_Y = 0
right_Analog_X = 0
right_Analog_Y = 0

left_Trigger = 0
right_Trigger = 0


def whats_pressed (list_Of_Input = []):
    # Dpad and Analog buttons
    if list_Of_Input[12] != 0:
        if list_Of_Input[12] % 4 != 0:
            if list_Of_Input[12] - 1 % 4 == 0:
                left_Analog_Pressed = True
                list_Of_Input[12] -= 1
            elif (list_Of_Input[12] - 2) % 4 == 0:
                right_Analog_Pressed = True
                list_Of_Input[12] -= 2
            elif (list_Of_Input[12] -3) % 4 == 0:
                left_Analog_Pressed = True
                right_Analog_Pressed = True
                list_Of_Input[12] -= 3
                
        if list_Of_Input[12] != 0:
            if list_Of_Input[12] == 4:
                up_Pressed = True
            
            if list_Of_Input[12] == 8:
                upRight_Pressed = True
                
            if list_Of_Input[12] == 12:
                right_Pressed = True
                
            if list_Of_Input[12] == 16:
                rightDown_Pressed = True
                
            if list_Of_Input[12] == 20:
                down_Pressed = True
                
            if list_Of_Input[12] == 24:
                downLeft_Pressed = True
                
            if list_Of_Input[12] == 28:
                left_Pressed = True
                
            if list_Of_Input[12] == 32:
                leftUP_pressed = True
                
    # A, B, X, Y buttons, Bumpers, Select and Start buttons
    if list_Of_Input[11] != 0:
        if list_Of_Input[11] - 128 >= 0:
            start_Pressed = True
            list_Of_Input[11] -= 128
        
        if  list_Of_Input[11] - 64 >= 0:
            select_Pressed = True
            list_Of_Input[11] -= 64
        
        if list_Of_Input[11] - 32 >= 0:
            right_Bumper_Pressed = True
            list_Of_Input[11] -= 32
        
        if list_Of_Input[11] - 16 >= 0:
            left_Bumper_Pressed = True
            list_Of_Input[11] -= 16
        
        if list_Of_Input[11] - 8 >= 0:
            button_Y_Pressed = True
            list_Of_Input[11] -= 8
        
        if list_Of_Input[11] - 4 >= 0:
            button_X_Pressed = True
            list_Of_Input[11] -= 4
        
        if list_Of_Input[11] - 2 >= 0:
            button_B_Pressed = True
            list_Of_Input[11] -= 2
            
        if list_Of_Input[11] - 1 >= 0:
            button_A_Pressed = True
            
    
    # Triggers, probably should be used for drill extension retraction. Will probably implement a dead-zone for safety
    if list_Of_Input[10] != 128:
        if list_Of_Input[10] > 128:
            left_Trigger = list_Of_Input[10] - 128
        
        if list_Of_Input[10] < 128:
            right_Trigger = list_Of_Input[10]
            
    
    # Analog Joysticks. As far as I can tell we need to use the average of the values. Will probably implement a dead-zone for safety
    
    # Left Analog Joystick Y-axis
    temp = (list_Of_Input[3] + list_Of_Input[4]) / 2
    left_Analog_Y = temp
    
    # Left Analog Joystick X-axis
    temp = (list_Of_Input[1] + list_Of_Input[2]) / 2
    left_Analog_X = temp
    
    # Right Analog Joystick Y-axis
    temp = (list_Of_Input[7] + list_Of_Input[8]) / 2
    right_Analog_Y = temp
    
    # Right Analog Joystick X-axis
    temp = (list_Of_Input[5] + list_Of_Input[6]) / 2
    right_Analog_X = temp
    
"""
At this point we need to determine what the exact commands are to be
"""