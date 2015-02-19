#include <Arduino.h>
#include <SPI.h>
#include <Ethernet.h>

#define PIN2INT 0
#define PIN3INT 1
#define PINLED 7

int etat = HIGH;
unsigned long mwh[25];
unsigned long lastChange[2];

byte mac[] = {
  0x90, 0xA2, 0xDA, 0x0E, 0xA1, 0x92
};
IPAddress ip(192, 168, 0, 102);
EthernetServer server(31415);

void setup() {
  Serial.begin(9600);
  pinMode(PINLED, OUTPUT);
  digitalWrite(PINLED, etat);
  mwh[PIN2INT] = mwh[PIN3INT] = 0;
  attachInterrupt(PIN2INT, tickPin2, FALLING);
  attachInterrupt(PIN3INT, tickPin3, FALLING);
  Ethernet.begin(mac, ip);
  server.begin();
}

void loop() {
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
      else if (line.indexOf("GET /cumulusmwh") != -1) {
        client.println(String(mwh[PIN2INT]));
        mwh[PIN2INT] = 0;
      }
      else if (line.indexOf("GET /chauffagemwh") != -1) {
        client.println(String(mwh[PIN3INT]));
        mwh[PIN3INT] = 0;
      }
      else if (line.indexOf("GET /cumulus_i") != -1) {
        static float numerateur = 60000;
        int conso = numerateur / (millis() - lastChange[PIN2INT]);
        client.println(String(conso));
      }
      else if (line.indexOf("GET /chauffage_i") != -1) {
        static float numerateur = 60000;
        int conso = numerateur / (millis() - lastChange[PIN3INT]);
        client.println(String(conso));
      }
      line = client.readStringUntil('\n');
    }
    lastLineEmpty = false;
    client.stop();
  }
}

void tickPin2(void) {
  tick(PIN2INT);
}

void tickPin3(void) {
  tick(PIN3INT);
}

void tick(int interrupNo) {
  //__|-|__ tick 90 ms :  status changed between 50 and 150 ms
  if (millis() - lastChange[interrupNo] > 200) { // && millis() - lastChange < 800) {
    etat = !etat;
    mwh[interrupNo] ++;
    lastChange[interrupNo] = millis();
    digitalWrite(PINLED, etat);
  }
}

boolean isEmptyLine(String line) {
  if (line.length() == 0) return true;
  return line.charAt(0) == '\r' || line.charAt(0) == '\n';
}


