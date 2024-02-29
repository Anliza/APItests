import requests
import json

url = "https://restful-booker.herokuapp.com/booking/{}"

id = 2

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Cookie": "token=abc123",
    "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
}

new_booking_data = {
    "firstname" : "James",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

payload = json.dumps(new_booking_data)

response = requests.put(url.format(id), data=payload, headers=headers)

if response.status_code == 200:
    print("Booking updated successfully.")
    updated_booking = response.json()  # If the server returns the updated booking data
    print("Updated booking details:", updated_booking)
else:
    print("Failed to update booking. Error:", response.text)