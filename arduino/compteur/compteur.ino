#include <Arduino.h>
#include <SPI.h>
#include <Ethernet.h>

#define PIN2INT 0
#define PINLED 7

int etat = HIGH;
unsigned long mwh = 0;
unsigned long lastChange;

byte mac[] = {
  0x90, 0xA2, 0xDA, 0x0E, 0xA1, 0x92
};
IPAddress ip(192, 168, 0, 102);
EthernetServer server(31415);

void setup() {
  Serial.begin(9600);
  pinMode(PINLED, OUTPUT);
  digitalWrite(PINLED, etat);

  attachInterrupt(PIN2INT, tick, CHANGE);
  Ethernet.begin(mac, ip);
  server.begin();
}

void loop() {
  Serial.println(mwh);

  EthernetClient client = server.available();
  String line;
  boolean lastLineEmpty = false;
  if (client) {
    lastLineEmpty = false;
    line = client.readStringUntil('\r');

    while (isEmptyLine(line) == false || lastLineEmpty == false) {
      if (isEmptyLine(line)) {
        lastLineEmpty = true;
      }
      else if (line.indexOf("GET /mwh") != -1) {
        client.println(String(mwh));
        mwh = 0;
      }
      else if (line.indexOf("GET /cumulus_i") != -1) {
        static float numerateur = 60000;
        int conso = numerateur / (millis() - lastChange);
        client.println(String(conso));
      }
      line = client.readStringUntil('\n');
    }
    lastLineEmpty = false;
    client.stop();
  }
}

void tick(void) {
  //__|-|__ tick 90 ms :  status changed between 50 and 150 ms
  if (millis() - lastChange > 50 && millis() - lastChange < 150) {
    etat = !etat;
    mwh ++;
    lastChange = millis();
    digitalWrite(PINLED, etat);
  }
}

boolean isEmptyLine(String line) {
  if (line.length() == 0) return true;
  return line.charAt(0) == '\r' || line.charAt(0) == '\n';
}

unsigned long getMwh() {
  static unsigned long tmp = mwh;
  mwh = 0;
  return tmp;
}

