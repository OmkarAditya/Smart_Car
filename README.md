# Smart_Car
A smart car mechannism which detects either driver is drunk or if an intruder as entered the car and if so sends an sms with live location regarding the same


COMPONENTS USED: ARDUINO UNO, ARDUINO MEGA,BREADBOARD, ALCOHOL SENSOR , ULTRASONIC SENSOR,PIR SENSOR AND FINGERPRINT SENSOR
SOFTWARE USED: ARDUINO IDE, PYTHON, TWLIO

WORKING OF INTRUDER DETECTION MODEL

1. The ultrasonic sensor connected with arduino mega detects if any obstacle is in front of it(within 10 cm) and if so alarm rings
2. The fingerprint sensor authorizes the entry of the authorized driver in the car
3. The pir sensor detects if any persion has entered the person.
   NOTE: IF THE AUTHORIZED PERSON IS INSIDE THE CAR(THE FINGERPRINT SENSOR HAS AUTHORIZED THE ENTRY), THE PIR DOESNT DETECT ANYTHING
   Hence if an intruder has entered the car then an alert sms will be sent to us shown below
4. All these sensors(pir,fingerprint)send their data from arduino mega to arduino uno, where we are running the python file to SEND SMS

https://github.com/OmkarAditya/Smart_Car/assets/108687318/becaeab9-1d56-4623-983c-334451dee1fd



SMS

![intruder](https://github.com/OmkarAditya/Smart_Car/assets/108687318/2a78d081-8724-41ba-9cf5-12d6642d40a6)

WORKING OF ALCOHOL DETECTION MODEL
1. alcohol sensor is connected directly to arduino uno to detect presence of alcohol
2. Irrespective of if the person is authorized or not, if alcohol is detected, an sms is sent whose python file takes data from arduino uno serial monitor
https://github.com/OmkarAditya/Smart_Car/assets/108687318/72f314df-599d-4071-9d4e-a1edac4b31a8

SMS

![alcohol](https://github.com/OmkarAditya/Smart_Car/assets/108687318/965a2ffb-6c05-43bd-b11f-59bf6d50d38f)
