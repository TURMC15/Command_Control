from math import atan2
from math import sqrt
from math import floor
from math import pow
from math import degrees

def differentialWheels(x, y):
    result = []
    angle = 0
    magnitude = 0
    """
    Format X, Y axis information and account for deadzone
    """
    if y <= 150 and y >= 110:
        y = 0
    elif y < 110:
        y = 110 - y
    elif y > 150:
        y = (y - 150) * -1
    
    if x <= 150 and x >= 110:
        x = 0
    elif x < 110:
        x = (110 - x) * -1
    elif x > 150:
        x = (x - 150) 
                
    """
    Get Angle of joystick and Magnitude of speed
    """
    angle = atan2(y, x)
    angle = degrees(angle)
    angle = angle % 360
    
    magnitude = sqrt(pow(y, 2) + pow(x, 2))
    
    """
    Get wheel speeds
    """

    
    right_dist = 0
    left_dist = 0
    if angle <= 90: 
    
        left_dist= +1 
        if angle<45.0: 
            right_dist= -1*((45.0-angle)/45.0) 
        else:
            right_dist= 1*( (angle-45.0)/45.0)
    
    elif angle <= 180:
        angle = angle - 90
        right_dist= +1
        if angle < 45.0:
            left_dist= 1*((45.0-angle)/45.0)
        
        else:
            left_dist= -1*((angle-45.0)/45.0)
    
    elif angle <= 270:
        angle = angle - 180
        left_dist= -1
        if angle < 45.0:
            right_dist= 1*((45.0-angle)/45.0)
    
        else:
            right_dist= -1*( (angle-45.0)/45.0)
    
    else:
        angle = angle - 270
        right_dist= -1
        if angle < 45.0:
            left_dist= -1 *((45.0-angle)/45.0)
        
        else:
            left_dist= 1*((angle - 45.0)/45.0)
    
    result.append(-1 * int (floor(left_dist*magnitude)))
    result.append(int (floor(right_dist*magnitude)))
    
    return result