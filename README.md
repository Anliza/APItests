# APItests
## Overview
This Python script is designed to update booking information using the RESTful API provided by "restful-booker". It utilizes the requests library to interact with the API endpoint. It updates a booking using the RESTful API provided by the URL https://restful-booker.herokuapp.com/booking/:id. 

## Features
- Updates booking information such as first name, last name, total price, check-in/out dates, and additional needs.
- Handles HTTP requests with appropriate headers and payload.
- Provides feedback on the success or failure of the update operation.

## Script Explained
1. It imports the necessary modules: requests for making HTTP requests and json for handling JSON data.
2. Defines the URL of the RESTful API endpoint where the booking will be updated. It uses {} as a placeholder for the booking ID.
3. Sets the ID of the booking to be updated. ID set to 1
4. Constructs the headers required for the HTTP request. These headers include content type, accept type, a cookie token, and basic authorization credentials.
5. Defines the data for the new booking, including the first name, last name, total price, whether a deposit is paid, booking dates (check-in and check-out), and any additional needs.
6. Converts the new_booking_data dictionary into a JSON string using json.dumps() to create the payload for the HTTP request.
7. Sends a PUT request to the API endpoint with the ID of the booking to update, along with the payload and headers.
8. Checks if the response status code is 200 (OK). If it is, it prints a success message and the updated booking details returned by the server. Otherwise, it prints an error message along with the response text.
9. The executing command is python <filename>.py

## Configuration (when needed)
- URL: Update the url variable to point to the desired RESTful API endpoint.
- ID: Set the id variable to the ID of the booking you want to update.
- Headers: Modify the headers dictionary to include any necessary authentication tokens or authorization credentials.
- Booking Data: Adjust the new_booking_data dictionary to specify the details of the booking update.

## Dependencies
Python 3.x
requests library

## Different scenarios to test
### A perfect booking (updateBooking.py)
This is the original script and the update is a success.
The output:
    Booking updated successfully.
    Updated booking details: {'firstname': 'James', 'lastname': 'Brown', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}

### Duplicate Booking (updateBooking.py executed twice)
Test updating a booking with the same data it already has to see if the API correctly handles duplicate requests.
The Output
    Failed to update booking. Error: Method Not Allowed

### Invalid Booking ID (invalidID.py)
Test what happens when one provides an invalid booking ID (e.g., a non-existent ID).
The output:
    Failed to update booking. Error: Method Not Allowed

### Invalid Data Format (invalidFormat.py)
Provide invalid data formats (e.g., string for total price instead of integer, incorrect date format) and observe how the script handles them.
The output:
    -> output for empty strings (input for date)
    Booking updated successfully.
    Updated booking details: {'firstname': 'James', 'lastname': '', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '0NaN-aN-aN', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}

    -> output for non-string input for lastname
    Traceback (most recent call last):
    File "/home/kamzu/Arbete/APItests/missingData.py", line 17, in <module>
    "lastname" : _, # testing the output when input is empty
    NameError: name '_' is not defined

### Missing Required Fields (missingFields.py)
Test the script with missing required fields (e.g., first name, last name) to see if it properly handles validation errors from the API.
The output:
    Failed to update booking. Error: Bad Request

### Unauthorized Access (unauthorized.py)
Modify the authorization credentials or remove them entirely to test how the API responds to unauthorized access attempts.
The output:
    Failed to update booking. Error: Forbidden

### Boundary Testing (boundarytest.py)
Test boundary cases such as maximum values for total price, minimum/maximum values for date fields, and other edge cases to ensure robustness.
The output:
    -> output while adjusting the price (see price)
    Booking updated successfully.
    Updated booking details: {'firstname': 'James', 'lastname': 'Brown', 'totalprice': 11100000000, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}

    -> output for date (see checkout date)
    Booking updated successfully.
    Updated booking details: {'firstname': 'James', 'lastname': 'Brown', 'totalprice': 11100000000, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '0NaN-aN-aN'}, 'additionalneeds': 'Breakfast'}


## Conclusion
All scenarios tested exhibit good reporting of error and the API configuration. 
