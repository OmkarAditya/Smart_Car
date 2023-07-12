#define alcohol A0
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(alcohol,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    char data=Serial.read();
    Serial.print(data);
  }
  int x=analogRead(alcohol);
//  Serial.println(x);
  if(x>350){
    Serial.println('2');
    digitalWrite(6,HIGH);
  }
  else{
    digitalWrite(6,LOW);
  }
  

}
