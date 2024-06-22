
# Juniper Api Soap Integration

## 1. Definition
This project involves integrating a SOAP-based API from Juniper into a backend system, with the primary objective of facilitating hotel-related operations through various endpoints. It includes a static mapping process for the hotel portfolio and a dynamic flow for booking operations. Designing a database to store hotel codes alongside their respective cities is crucial for efficient retrieval and management of hotel data.

## 2. Project Goal
The objective of this project is to demonstrate how the JP API from Juniper was developed and integrated. The API technology is based on SOAP, and a DRF python backend was developed to transform the requests into JSON format. Due to the complexity of the integration, large sections of the code have been removed. In the evidence folder, JSON requests and responses can be found, as well as images that document the development process. Unfortunately, it is not possible to provide the complete code for free. Additionally, a logging module was developed to store every request and response. This module checks for errors and logs detailed information whenever an error is detected.

## 3. Technologies Used
The integration uses the following technologies:
- Python Django Rest Framework (DRF): For building the backend API.
- requests library: For making HTTP requests.
- xmltodict: For converting XML responses from the SOAP API into JSON format.

## 4. Technical Details
### SOAP to REST Conversion:
- Utilize the requests library to send SOAP requests to the Juniper API.
- Convert SOAP XML responses to JSON using xmltodict.
- Structure responses to match the expected format for the Django Rest Framework.

### Database Design:
- Design tables to store hotel codes, cities, and related data.
- Optimize for quick lookup and efficient data management.

### Static Mapping Process:
- Map hotel portfolio data to the database.
- Ensure data consistency and integrity through validation checks.

### Dynamic Booking Flow:
- Implement booking rules and availability checks.
- Handle booking requests, cancellations, and booking status updates.

### Logging module:
- Developed a logging module to capture and store every request and response.
- Implemented error detection mechanisms to log detailed information when errors occur.

## 5. Endpoints
### Retrieval and save all available hotel codes:
v1/hotel-portfolio/

### Checks hotel availability:
v1/hotel-availability/
[RQ](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelAvail/RQ.txt)
[RS](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelAvail/RS.txt)
![Screenshot](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelAvail/image.jpg)

### Validate the combination in order to complete the booking flow process:
v1/hotel-bookingrules/
[RQ](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelBookingRules/RQ.txt)
[RS](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelBookingRules/RS.txt)
![Screenshot](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelBookingRules/images.jpg)

### Booking confirmation request:
v1/hotel-booking/
[RQ](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelBooking/RQ.txt)
[RS](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelBooking/RS.txt)
![Screenshot](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelBooking/image.jpg)

### Cancels bookings:
v1/hotel-cancelbooking/
[RQ](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelCancel/RQ.txt)
[RS](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelCancel/RS.txt)
![Screenshot](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelCancel/image.jpg)

### Reads booking details:
v1/hotel-readbooking/
[RQ](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelReadBooking/RQ.txt)
[RS](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelReadBooking/RS.txt)
![Screenshot](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelReadBooking/image.jpg)

### Lists all bookings:
v1/hotel-bookinglist/
v1/hotel-readbooking/
[RQ](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelBookingList/RQ.txt)
[RS](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelBookingList/RS.txt)
![Screenshot](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HotelBookingList/image.jpg)

### Logging module:
- [Error](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HandleLogs/ErrorHandle.jpg)
- [HotelAvailability](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HandleLogs/HotelAvailability.jpg)
- [HotelBookingRules](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HandleLogs/HotelBookingRules.jpg)
- [HotelBooking](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HandleLogs/HotelBooking.jpg)
- [HotelReadBooking](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HandleLogs/HotelReadBooking.jpg)
- [HotelCancel](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HandleLogs/HotelCancel.jpg)
- [HotelBookingList](https://github.com/julifmontoya/drf-juniper-public/blob/master/evidence/HandleLogs/HotelBookingList.jpg)

## 4. References
Link from JP API
https://api-edocs.ejuniper.com/en/api/jp/hotel-api
