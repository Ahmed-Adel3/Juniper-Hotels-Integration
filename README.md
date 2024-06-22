
# Juniper Api Soap Integration

## 1. Definition
This project involves integrating a SOAP-based API from Juniper into a backend system, with the primary objective of facilitating hotel-related operations through various endpoints. It includes a static mapping process for the hotel portfolio and a dynamic flow for booking operations. Designing a database to store hotel codes alongside their respective cities is crucial for efficient retrieval and management of hotel data.

## 2. Project Goal
The objective of this project is to demonstrate how the JP API from Juniper was developed and integrated. The API technology is based on SOAP, and a DRF python backend was developed to transform the requests into JSON format. Due to the complexity of the integration, large sections of the code have been removed. In the evidence folder, JSON requests and responses can be found, as well as images that document the development process. Unfortunately, it is not possible to provide the complete code for free. Additionally, a logging module was developed to store every request and response. This module checks for errors and logs detailed information whenever an error is detected.

## 3. Architecture
This project utilizes a monolithic architecture, where the application is built as a single, self-contained unit. In this example, only the API integration application is shown. However, the actual application comprises many modules, each operating independently.

Key Components:
###  Modular Application Structure:
- Each module has well-defined boundaries and responsibilities, ensuring separation of concerns and easier maintenance.

### Separate Components as Services:
- Each service/module contains its own set of models, serializers, views and business logic, promoting a clear separation of functionality.

### Code Reusability:
- Modules can share common libraries and utilities within the monolith, reducing redundancy and fostering consistency across the application.

### Decoupled Logic:
- The business logic is decoupled from the server, allowing for better modularization and flexibility in updating or replacing components as needed.

#### Example: Using Vue.js in the Frontend
**Frontend (Vue.js) Setup:**

- Use Vue.js to build the user interface.
- Implement components for various parts of the application (e.g., user management, reservations, packages).

**Backend (DRF) Setup:**
- Use Django Rest Framework to build the API endpoints.
- Ensure the backend only handles data storage, retrieval, and basic validation.

**Decoupling Business Logic:**
- Implement core business logic in Vue.js components and services.
- Use Vuex for state management to handle application state and business logic centrally.

## 4. Technologies Used
The integration uses the following technologies:
- Python Django Rest Framework (DRF): For building the backend API.
- requests library: For making HTTP requests.
- xmltodict: For converting XML responses from the SOAP API into JSON format.
- python decouple: Utilized for managing project settings and environment variables.

## 5. Technical Details
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

## 7. Endpoints
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

## 6. References
Link from JP API
https://api-edocs.ejuniper.com/en/api/jp/hotel-api
