// Function to control a linear actuator using two relays. 
// Inputs: 
//        mode: 1-->extend 0-->off -1-->retract
//        hotRelay: pin controlling the relay connected actuator hot
//        gndRelay: pincontrolling the relay connected to actuator ground
// Wiring:
//        Both Relays will be wired with a ground on the left, and +12V
//        on the right. The middle pin on each relay will be the hot and
//        ground wires from the actuator, respectively.
// Written By: 
//        Robert Irwin 

/*
const int hotRelay = 12; // pin controlling the relay with the 
                         // hot side of the actuator

const int gndRelay = 8; // pin controlling the relay with the 
                        // hot side of the actuator


void setup() {
  // set both pins as outputs

  pinMode(hotRelay, OUTPUT);
  pinMode(gndRelay, OUTPUT);

}
*/

void actuator_control(int mode, int hotRelay, int gndRelay) {
  
  int hot = HIGH;
  int gnd = LOW;

  // off state (both relays switched to ground)
  if (mode == 0){
    digitalWrite(hotRelay, gnd);
    digitalWrite(gndRelay, gnd);
  }
  // extend state
  else if (mode == 1){ 
    digitalWrite(hotRelay, gnd);
    digitalWrite(gndRelay, hot);
  }

  // retract state
  else if (mode == -1){
    digitalWrite(gndRelay, gnd);
    digitalWrite(hotRelay, hot);
  }
  
}
