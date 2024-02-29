import requests
import json

url = "https://restful-booker.herokuapp.com/booking/{}"

id = 1

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Cookie": "token=abc123",
    "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
}

new_booking_data = {
    "firstname" : "James",
    "lastname" : _, # testing the output when input is empty
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "", # testing the output when input is empty
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

payload = json.dumps(new_booking_data)

response = requests.put(url.format(id), data=payload, headers=headers)

if response.status_code == 200:
    print("Booking updated successfully.")
    updated_booking = response.json()  
    print("Updated booking details:", updated_booking)
else:
    print("Failed to update booking. Error:", response.text)


    # output for empty strings (input for date)
    # Booking updated successfully.
    # Updated booking details: {'firstname': 'James', 'lastname': '', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '0NaN-aN-aN', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}

    # output for non-string input for lastname
    # Traceback (most recent call last):
    # File "/home/kamzu/Arbete/APItests/missingData.py", line 17, in <module>
    # "lastname" : _, # testing the output when input is empty
    # NameError: name '_' is not defined