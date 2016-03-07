"""
Version 0.0.1
12/22/15
@author: Ben Camp

This module takes the commands from the given string and formats them into the 
array of bytes for the motor control.

I'm thinking 5-6 bytes are needed.
4 for the commands
"""

direction_Left_Drive_Motor = 0
direction_Right_Drive_Motor = 0
direction_Augur_Motor = 0
direction_Dumping_Motor = 0

speed_Left_Drive_Motor = 0
speed_Right_Drive_Motor = 0
speed_Augur_Motor = 0
speed_Dumping_Motor = 0

checksum = 0

def command_interpret(command_string):
    #Segment the 
        
"""
These are the java commands, they need to be converted
"""
       # first command byte
        if (this.left_Motor_Speed < 0f){
            # travel in reverse
            this.byte_Array_To_Write[1] = (byte)1;
            # write the data byte
            this.byte_Array_To_Write[2] = (byte)Math.round(-127f * this.left_Motor_Speed);
        } else {
            # travel forward
            this.byte_Array_To_Write[1] = (byte)0;
            # write the data byte
            this.byte_Array_To_Write[2] = (byte)Math.round(127f * this.left_Motor_Speed);
        }
        
        # write the checksum
        this.byte_Array_To_Write[3] = 
                (byte) ((byte)(this.byte_Array_To_Write[0] + 
                        this.byte_Array_To_Write[1] + 
                        this.byte_Array_To_Write[2]) & ((byte)127));
        
        this.byte_Array_To_Write[4] = this.mainDriveMotorControllerAddress;
        
        if (this.right_Motor_Speed < 0f){
            # drive in reverse
            this.byte_Array_To_Write[5] = (byte)5;
            # write the data byte
            this.byte_Array_To_Write[6] = (byte)Math.round(-127f * this.right_Motor_Speed);
        } else {
            # drive forward
            this.byte_Array_To_Write[5] = (byte)4;
            # write the data byte
            this.byte_Array_To_Write[6] = (byte)Math.round(127f * this.right_Motor_Speed);
        }
        
        # write the checksum
        this.byte_Array_To_Write[7] = 
                (byte) ((byte)(this.byte_Array_To_Write[4] + 
                        this.byte_Array_To_Write[5] + 
                        this.byte_Array_To_Write[6]) & ((byte)127));
        
        this.byte_Array_To_Write[8] = this.collectionAndDumpMotorControllerAddress;
        
        if (this.collection_System_Speed < 0f){
            # reverse the collection system
            this.byte_Array_To_Write[9] = (byte)1;
            this.byte_Array_To_Write[10] = (byte)Math.round(-127f * this.collection_System_Speed);
        } else {
            # drive collection system forward
            this.byte_Array_To_Write[9] = (byte)0;
            this.byte_Array_To_Write[10] = (byte)Math.round(127f * this.collection_System_Speed);
        }
        
        # write the checksum
        this.byte_Array_To_Write[11] = 
                (byte) ((byte)(this.byte_Array_To_Write[8] + 
                        this.byte_Array_To_Write[9] + 
                        this.byte_Array_To_Write[10]) & ((byte)127));
        
        this.byte_Array_To_Write[12] = this.collectionAndDumpMotorControllerAddress;
        
        if (this.dump_System_Speed < 0f){
            # drive dump system in reverse
            this.byte_Array_To_Write[13] = (byte)5;
            this.byte_Array_To_Write[14] = (byte)Math.round(-127f * this.dump_System_Speed);
        } else {
            # drive dump system forward
            this.byte_Array_To_Write[13] = (byte)4;
            this.byte_Array_To_Write[14] = (byte)Math.round(127f * this.dump_System_Speed);
        }
        
        # write the checksum
        this.byte_Array_To_Write[15] = 
                (byte) ((byte)(this.byte_Array_To_Write[12] + 
                        this.byte_Array_To_Write[13] + 
                        this.byte_Array_To_Write[14]) & ((byte)127));
        
        if (DEBUG){
            System.out.println("Bytes: " + Arrays.toString(byte_Array_To_Write));
        }
        
    }