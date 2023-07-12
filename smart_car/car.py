import time
import serial
import requests
from twilio.rest import Client
import json
from urllib.request import urlopen

account_sid = "AC8a7175c6d3cfafa93a55f3b94d8ed838"
auth_token = "c258a29fd5310c695afe35655eadd4d2"
twilio_number = "+12343015044"
recipient_number = "+916372083316"

serial_port = "COM8"  # Update with your serial port
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)
client = Client(account_sid, auth_token)


while True:
    # Reading from arduino
    line = ser.readline().decode().strip()
    print(line)

    # Alcohol
    if line == '2':
        
        url = "http://ipinfo.io/json"
        response = urlopen(url)
        data = json.load(response)
        x = f'driver is drunk at city: {data["city"]}, region: {data["region"]}, country: {data["country"]}, Lat & Long: {data["loc"]}'
        # Send the message via Twilio
        message = client.messages.create(
            body=x, from_=twilio_number, to=recipient_number
        )
        print("Message sent successfully!")
    # PIR Sensor
    if line == '1':
        
        url = "http://ipinfo.io/json"
        response = urlopen(url)
        data = json.load(response)
        x = f'Someone entered the car: {data["city"]}, region: {data["region"]}, country: {data["country"]}, Lat & Long: {data["loc"]}'
        # Send the message via Twilio
        message = client.messages.create(
            body=x, from_=twilio_number, to=recipient_number
        ) 
        print("Message sent successfully!")

# Close the serial port
ser.close()