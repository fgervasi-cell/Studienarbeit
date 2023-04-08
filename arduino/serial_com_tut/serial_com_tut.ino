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

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.println("Received " + data);
    analogWrite(pumpe1, (getValueAt(data, 0) * 0.5 + 50) * 2.55);
    analogWrite(pumpe2, (getValueAt(data, 1) * 0.5 + 50) * 2.55);
    analogWrite(pumpe3, (getValueAt(data, 2) * 0.5 + 50) * 2.55);
    analogWrite(pumpe4, (getValueAt(data, 3) * 0.5 + 50) * 2.55);
    delay(3000);
  } else {
    analogWrite(pumpe1, 0);
    analogWrite(pumpe2, 0);
    analogWrite(pumpe3, 0);
    analogWrite(pumpe4, 0);
    analogWrite(pumpe5, 0);
  }
}