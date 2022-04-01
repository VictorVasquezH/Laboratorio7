#define led1 13
#define pot A0


void setup()
{
  Serial.begin(9600);
  pinMode(pot,INPUT);
  pinMode(led1,OUTPUT);
}

void loop()
{
  int val = analogRead(pot);
  int m = map(val,0,1023,0,100);
  Serial.print("Valor PWM: ");
  Serial.println(m);
 
    if(m>=50)
    {
     digitalWrite(led1,HIGH);

    }
    else
    {
     digitalWrite(led1,LOW);

    }
    //Envio de datos

    delay(50);

}
