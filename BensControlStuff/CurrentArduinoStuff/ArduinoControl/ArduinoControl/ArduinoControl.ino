/*
 UDPSendReceiveString:
 This sketch receives UDP message strings, prints them to the serial port
 and sends an "acknowledge" string back to the sender
 A Processing sketch is included at the end of file that can be used to send
 and received messages for testing with a computer.
 created 21 Aug 2010
 by Michael Margolis
 This code is in the public domain.
 */


#include <SPI.h>         // needed for Arduino versions later than 0018
#include <Ethernet.h>
#include <EthernetUdp.h>         // UDP library from: bjoern@cs.stanford.edu 12/30/2008

void actuatordriver (int, int, int);
void stepperdriver(int,int, int, int);
void conveyerdriver(boolean, int);
void augerdriver(boolean, int);

//Lazy global variables
int ACTUATOR_HOT;
int ACTUATOR_GROUND;
int ACTUATOR_DIRECTION_CONTROL = 0;

int STEPPER_CONTROL_PIN = 9;
int STEPPER_DIRECTION_PIN = 8;
int STEPPER_DIRECTION_CONTROL = 0;

int CONVEYER_PIN;
boolean CONVEYER_ON = false;

int AUGER_PIN;
boolean AUGER_ON = false;

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(192, 168, 0, 103);

unsigned int localPort = 1111;      // local port to listen on

// buffers for receiving and sending data
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];  //buffer to hold incoming packet,
char  ReplyBuffer[] = "acknowledged";       // a string to send back

// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;

void setup() {
    //Pin setup
    pinMode(ACTUATOR_HOT, OUTPUT);
    pinMode(ACTUATOR_GROUND, OUTPUT);
    
    pinMode(STEPPER_DIRECTION_PIN, OUTPUT);
    pinMode(STEPPER_CONTROL_PIN, OUTPUT);
    
    pinMode(CONVEYER_PIN, OUTPUT);
    
    pinMode(AUGER_PIN, OUTPUT);

    
    // start the Ethernet and UDP:
    Ethernet.begin(mac, ip);
    Udp.begin(localPort);
  
    Serial.begin(9600);
}

void loop() {
  // if there's data available, read a packet
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    Serial.print("Received packet of size ");
    Serial.println(packetSize);
    Serial.print("From ");
    IPAddress remote = Udp.remoteIP();
    for (int i = 0; i < 4; i++) {
      Serial.print(remote[i], DEC);
      if (i < 3) {
        Serial.print(".");
      }
    }
    Serial.print(", port ");
    Serial.println(Udp.remotePort());

    // read the packet into packetBufffer
    Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    Serial.println("Contents:");
    Serial.println(packetBuffer);
  
    ACTUATOR_DIRECTION_CONTROL = packetBuffer[0];
    STEPPER_DIRECTION_CONTROL = packetBuffer[1];
    if (packetBuffer[2] != 1)
      CONVEYER_ON = false;
    else
      CONVEYER_ON = true;

    if (packetBuffer[3] != 1)
      AUGER_ON = false;
    else
      AUGER_ON = true;
      
    actuatordriver(ACTUATOR_DIRECTION_CONTROL, ACTUATOR_HOT, ACTUATOR_GROUND);
    stepperdriver(250,STEPPER_DIRECTION_CONTROL, STEPPER_CONTROL_PIN, STEPPER_DIRECTION_PIN);
    conveyerdriver(CONVEYER_ON, CONVEYER_PIN);
    augerdriver(AUGER_ON, AUGER_PIN);
    

    // send a reply to the IP address and port that sent us the packet we received
    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
    Udp.write(ReplyBuffer);
    
    Udp.endPacket();
    
  }
  delay(10);
}

void actuatordriver (int mode, int hotRelay, int gndRelay) {
  
  // off state (both relays switched to ground)
  if (mode == 0){
    digitalWrite(hotRelay, LOW);
    digitalWrite(gndRelay, LOW);
  }
  
  // extend state
  else if (mode == 1){ 
    digitalWrite(hotRelay, LOW);
    digitalWrite(gndRelay, HIGH);
  }

  // retract state
  else if (mode == 2){
    digitalWrite(hotRelay, HIGH);
    digitalWrite(gndRelay, LOW);
  }
}

void augerdriver(boolean on, int pin){
  if (on){
    digitalWrite(pin, HIGH);
  }
  else{
    digitalWrite(pin, LOW);
  }
}

void conveyerdriver(boolean on, int pin){
  if (on){
    digitalWrite(pin, HIGH);
  }
  else{
    digitalWrite(pin, LOW);
  }
}

void stepperdriver(int delaytime,int stepperdirection, int steppercontrolpin, int stepperdirectionpin){
    if(stepperdirection == 1){
      digitalWrite(stepperdirectionpin, LOW);
    } else {
      digitalWrite(stepperdirectionpin, HIGH);
    }
    digitalWrite(steppercontrolpin, HIGH);
    delayMicroseconds(delaytime);          
    digitalWrite(steppercontrolpin, LOW); 
    delayMicroseconds(delaytime);
 }


