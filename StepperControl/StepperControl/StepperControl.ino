/*
microstep driver ST-M5045
Pul+ goes to +5V
Pul- goes to Arduino Pin 9
Dir+ goes to +5V
Dir- goes to to Arduino Pin 8
Enable+ to nothing
Enable- to nothing
*/

int sensorPin = A3;
int sensorValue = 0;
void stepperdriver(int,int, int, int);

void setup() {                
  pinMode(8, OUTPUT);     //direction pin
  pinMode(9, OUTPUT); //step pin
}

void loop() {
  //A 250 millisecond delay is the fastest the stepper can be driven
  stepperdriver(250,0, 9, 8);
 }

 //Input: delaytime, stepperdirection, steppercontrolpin, stepperdirectionpin
 //Outputs: None
 //Summary: Fastest delay for half-step is ~250 milliseconds, the one for full-steps is 1 milliseconds
 //with half-steps we get more vibration and less torque. The stepper direction is clockwise when 0,
 //counterwise when stepperdirection is 1. 
 void stepperdriver(int delaytime,int stepperdirection, int steppercontrolpin, int stepperdirectionpin){
  pinMode(stepperdirectionpin, OUTPUT);
  pinMode(steppercontrolpin, OUTPUT);
  if(stepperdirection == 1){
    digitalWrite(stepperdirection, LOW);
  } else {
    digitalWrite(stepperdirection, HIGH);
  }
  digitalWrite(steppercontrolpin, HIGH);
  delayMicroseconds(delaytime);          
  digitalWrite(steppercontrolpin, LOW); 
  delayMicroseconds(delaytime);
 }

