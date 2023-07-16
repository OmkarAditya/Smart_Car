import time
import serial
import requests
from twilio.rest import Client
import json
from urllib.request import urlopen

account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"
twilio_number = "TWILIO NUMBER"
recipient_number = "YOUR NUMBER"

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
