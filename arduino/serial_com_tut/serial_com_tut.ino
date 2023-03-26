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
    for (int i = 0; i < 4; i++) {
      Serial.println(getValueAt(data, i));
    }
  }
}