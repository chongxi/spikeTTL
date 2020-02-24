/*
  Serial Event --> TTL&LED pulse 
  (using Pin 13: Teensy 3.5/4.0 has the LED on pin 13)

  -----------------------------------------------------------------
  When the serial data arrives, it converts into LED and TTL pulse.

  b'10'   --> 10us pulse
  b'100'  --> 100us pulse
  b'1000' --> 1000us pulse

  etc. 
  The precision of 10/100/1000us pulse were tested (pass). 
  The longest accurate pulse is 16383us, that is 16.3ms.
  -----------------------------------------------------------------
  
  created 24 Fet 2020
  by Chongxi Lai

*/

const int ledPin =  13;         // the number of the LED pin
String inputString = "";        // a String to hold incoming data
bool stringComplete = false;    // whether the string is complete

// the follow variables is a long because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
long interval = 1;           // length of the TTL pulse (milliseconds)

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  // set the digital pin as output:
  pinMode(ledPin, OUTPUT);      
}

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    TTL_Pulse(inputString.toInt());
    Serial.println(inputString);
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}


void TTL_Pulse(int T) {
  // LED with TTL (pin13) HIGH last for T microseconds
  digitalWrite(ledPin, HIGH);
  delayMicroseconds(T);
  digitalWrite(ledPin, LOW);
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
