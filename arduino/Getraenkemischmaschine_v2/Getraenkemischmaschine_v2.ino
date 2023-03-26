/*Programm für Softwareprojekt "Getränkemischmaschine"
   DHBW Karlsruhe TMT20B1 (Götz, Höckele, Lobert)

   Pinbelegung am Arduino:
  +5V = 5V
  TX  = pin 0 (RX)
  RX  = pin 1 (TX)
  GND = GND

  Pumpe1 = pin 11
  Pumpe2 = pin 10  
  Pumpe3 = pin 9
  Pumpe4 = pin 3
  Pumpe5 = pin 5

  Wasserstandssensor1 = A1
  Wasserstandssensor2 = A2
  Wasserstandssensor3 = A3
  Wasserstandssensor4 = A4
  Wasserstandssensor5 = A5

  Schalter = pin 13

*/
#include <Nextion.h>
//Variablen
int CurrentPage = 0;  //Aktuelle Seite des Displays
int S;                //Welcher pwm wert wird verändert
int pwm1 = 0;         //pwm Werte
int pwm2 = 0;
int pwm3 = 0;
int pwm4 = 0;
int pwm5 = 0;

int Schalter = 13;  //Füllen Druckknopf

int pumpe1 = 11;  //Pumpe 1
int pumpe2 = 10;  //Pumpe 2
int pumpe3 = 9;   //Pumpe 3
int pumpe4 = 3;   //Pumpe 4
int pumpe5 = 5;   //Pumpe 5

int Sensor1 = A1;  //Wasserstandssensor 1
int Sensor2 = A2;  //Wasserstandssensor 2
int Sensor3 = A3;  //Wasserstandssensor 3
int Sensor4 = A4;  //Wasserstandssensor 4
int Sensor5 = A5;  //Wasserstandssensor 5
//Nextion Elemente
NexButton j0 = NexButton(1, 10, "j0");    //progressbar
NexButton j1 = NexButton(1, 11, "j1");    //progressbar
NexButton j2 = NexButton(1, 12, "j2");    //progressbar
NexButton j3 = NexButton(1, 13, "j3");    //progressbar
NexButton j4 = NexButton(1, 14, "j4");    //progressbar
NexButton res = NexButton(1, 19, "res");  //resetbutton

NexSlider h0 = NexSlider(2, 2, "h0");  //Slider
NexButton b3 = NexButton(2, 7, "b3");  //Savebutton

NexDSButton bt0 = NexDSButton(3, 4, "bt0");   //DSButton zum Spülen
NexDSButton bt1 = NexDSButton(3, 5, "bt1");   //DSButton zum Spülen
NexDSButton bt2 = NexDSButton(3, 6, "bt2");   //DSButton zum Spülen
NexDSButton bt3 = NexDSButton(3, 14, "bt3");  //DSButton zum Spülen
NexDSButton bt4 = NexDSButton(3, 15, "bt4");  //DSButton zum Spülen
NexButton b2 = NexButton(3, 3, "b2");         //Back im Wartungsmenu

NexPage page0 = NexPage(0, 0, "Startseite");   //page
NexPage page1 = NexPage(1, 0, "Auswahl");      //page
NexPage page2 = NexPage(2, 0, "Einstellung");  //page
NexPage page3 = NexPage(3, 0, "Wartung");      //page

//char buffer[100] = {0};                      //für Text

NexTouch *nex_listen_list[] =  //Nextion Elemente einbinden
  {
    &j0,
    &j1,
    &j2,
    &j3,
    &j4,
    &res,
    &h0,
    &b3,
    &bt0,
    &bt1,
    &bt2,
    &bt3,
    &bt4,
    &b2,
    &page0,
    &page1,
    &page2,
    &page3,
    NULL
  };
//Events
void j0PopCallback(void *ptr)  //prog1 release
{
  S = 1;
}
void j1PopCallback(void *ptr)  //prog1 release
{
  S = 2;
}
void j2PopCallback(void *ptr)  //prog1 release
{
  S = 3;
}
void j3PopCallback(void *ptr)  //prog1 release
{
  S = 4;
}
void j4PopCallback(void *ptr)  //prog1 release
{
  S = 5;
}
void resPopCallback(void *ptr)  //reset release -> rücksetzen auf pwm=0
{
  pwm1 = 0;
  pwm2 = 0;
  pwm3 = 0;
  pwm4 = 0;
  pwm5 = 0;
}
void h0PopCallback(void *ptr)  //  slider release
{
}
void b3PopCallback(void *ptr)  //Save release
{
  uint32_t sl = 0;                //Variable
  h0.getValue(&sl);               //Sliderwert in Variable speichern
  for (int i = 0; i < 10; i++) {  //Sicherstellen das Wert richtig übernommen wurde
    if (sl == 0) {
      h0.getValue(&sl);
    }
  }
  if (sl != 0) {
    if (S == 1) {  //Feststellen welcher in welche PWM der Sliderwert übernommen werden soll
      //pwm1 = 125 + ((sl/100) * 130);
      pwm1 = (sl * 0.5 + 50) * 2.55;  //0-100 in 0-255 umwandeln 127,5
    } else if (S == 2) {
      //pwm2 = 125 + ((sl/100) * 130);
      pwm2 = (sl * 0.5 + 50) * 2.55;
    } else if (S == 3) {
      //pwm3 = 125 + ((sl/100) * 130);
      pwm3 = (sl * 0.5 + 50) * 2.55;
    } else if (S == 4) {
      //pwm4 = 125 + ((sl/100) * 130);
      pwm4 = (sl * 0.5 + 50) * 2.55;
    } else if (S == 5) {
      //pwm5 = 125 + ((sl/100) * 130);
      pwm5 = (sl * 0.5 + 50) * 2.55;
    }
  }
}

void bt0PopCallback(void *ptr)  // DSbutton release
{
  uint32_t bt_0 = 0;    // Variable
  bt0.getValue(&bt_0);  // Status des DSB in Variable speichern

  if (bt_0 == 1) {  //DS an -> Pumpe an
    pwm1 = 255;
  } else {  //DS aus -> Pumpe aus
    pwm1 = 0;
  }
}
void bt1PopCallback(void *ptr) {
  uint32_t bt_1 = 0;
  bt1.getValue(&bt_1);

  if (bt_1 == 1) {
    pwm2 = 255;
  } else {
    pwm2 = 0;
  }
}
void bt2PopCallback(void *ptr) {
  uint32_t bt_2 = 0;
  bt2.getValue(&bt_2);

  if (bt_2 == 1) {
    pwm3 = 255;
  } else {
    pwm3 = 0;
  }
}
void bt3PopCallback(void *ptr) {
  uint32_t bt_3 = 0;
  bt3.getValue(&bt_3);

  if (bt_3 == 1) {
    pwm4 = 255;
  } else {
    pwm4 = 0;
  }
}
void bt4PopCallback(void *ptr) {
  uint32_t bt_4 = 0;
  bt4.getValue(&bt_4);

  if (bt_4 == 1) {
    pwm5 = 255;
  } else {
    pwm5 = 0;
  }
}
void b2PopCallback(void *ptr)  //back release
{
  pwm1 = 0;  //sicherstellen das beim verlassen des Wartungsmenus wieder alle Pumpen aus sind
  pwm2 = 0;
  pwm3 = 0;
  pwm4 = 0;
  pwm5 = 0;
}
void page0PushCallback(void *ptr)  // page init
{
  CurrentPage = 0;  //             //aktuelle Seite merken
}
void page1PushCallback(void *ptr) {
  CurrentPage = 1;
}
void page2PushCallback(void *ptr) {
  CurrentPage = 2;
}
void page3PushCallback(void *ptr) {
  CurrentPage = 3;
}

int getValueAt(String s, int vpos) {
  int pos = 0;
  int valueCount = 0;
  for (int i = 0; i < s.length(); i++) {
    if (s.charAt(i) == ',' || i == s.length() - 1) {
      String value = "";
      int bound = (i == s.length() - 1 ? i + 1 : i);
      for (int j = pos; j < bound; j++) {
        value.concat(s.charAt(j));
      }
      if (valueCount == vpos) {
        return value.toInt();
      }
      pos = i + 1;
      valueCount++;
    }
  }
  return -1;
}

int isSetup = 1;

void setup() {
  S = 0;                     //kein pwm Wert auswählen
  pinMode(Schalter, INPUT);  //Eingänge und Ausgänge definieren
  pinMode(Sensor1, INPUT);
  pinMode(Sensor2, INPUT);
  pinMode(Sensor3, INPUT);
  pinMode(Sensor4, INPUT);
  pinMode(Sensor5, INPUT);
  pinMode(pumpe1, OUTPUT);
  pinMode(pumpe2, OUTPUT);
  pinMode(pumpe3, OUTPUT);
  pinMode(pumpe4, OUTPUT);
  pinMode(pumpe5, OUTPUT);

  Serial.begin(115200);         //Kommunikation starten(Baud:115200)
  delay(500);                   //Vorgang kann etwas dauern
  Serial.print("baud=115200");  //Nextion auf gleiche Baudrate stellen
  Serial.write(0xff);           //3 Endtags damit Nextion weiß alles wurde gesendet
  Serial.write(0xff);
  Serial.write(0xff);
  //Events einbinden
  j0.attachPop(j0PopCallback);
  j1.attachPop(j1PopCallback);
  j2.attachPop(j2PopCallback);
  j3.attachPop(j3PopCallback);
  j4.attachPop(j4PopCallback);
  res.attachPop(resPopCallback);

  h0.attachPop(h0PopCallback);
  b3.attachPop(b3PopCallback);

  bt0.attachPop(bt0PopCallback);
  bt1.attachPop(bt1PopCallback);
  bt2.attachPop(bt2PopCallback);
  bt3.attachPop(bt3PopCallback);
  bt4.attachPop(bt4PopCallback);
  b2.attachPop(b2PopCallback);

  page0.attachPush(page0PushCallback);
  page1.attachPush(page1PushCallback);
  page2.attachPush(page2PushCallback);

  int isSetup = 0;
}

void loop() {
  nexLoop(nex_listen_list);           //Nextion events überprüfen
  if (digitalRead(Schalter) == HIGH)  //Füllen Knopf an -> PWM Werte an Pumpen geben
  {
    if (analogRead(Sensor1) <= 800) {  //Read max: 1024
      analogWrite(pumpe1, pwm1);
    }
    if (analogRead(Sensor2) <= 800) {
      analogWrite(pumpe2, pwm2);
    }
    if (analogRead(Sensor3) <= 800) {
      analogWrite(pumpe3, pwm3);
    }
    if (analogRead(Sensor4) <= 800) {
      analogWrite(pumpe4, pwm4);
    }
    if (analogRead(Sensor5) <= 800) {
      analogWrite(pumpe5, pwm5);
    }
  } else if (Serial.available() > 0 && isSetup == 0) {
    String data = Serial.readStringUntil('\n');  // e.g. "50,50,0,0"
    analogWrite(pumpe1, (getValueAt(data, 0) * 0.5 + 50) * 2.55);
    analogWrite(pumpe2, (getValueAt(data, 1) * 0.5 + 50) * 2.55);
    analogWrite(pumpe3, (getValueAt(data, 2) * 0.5 + 50) * 2.55);
    analogWrite(pumpe4, (getValueAt(data, 3) * 0.5 + 50) * 2.55);
    delay(3000);  // let the "button" be "pressed" for three seconds
    analogWrite(pumpe1, 0);
    analogWrite(pumpe2, 0);
    analogWrite(pumpe3, 0);
    analogWrite(pumpe4, 0);
  } else  //Füllen Knopf aus -> Pumpen aus
  {
    analogWrite(pumpe1, 0);
    analogWrite(pumpe2, 0);
    analogWrite(pumpe3, 0);
    analogWrite(pumpe4, 0);
    analogWrite(pumpe5, 0);
  }
}
