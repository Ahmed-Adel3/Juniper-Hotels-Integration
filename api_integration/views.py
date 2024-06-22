from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import xmltodict
from decouple import config
from .models import Hotel, Zone, City, HotelCategory
from .serializers import HotelDoLogSerializer


URL_BASE = 'https://xml-uat.bookingengine.es/webService/jp/operations/'
USER = config('USER')
PASSWORD = config('PASSWORD')

class HotelPortfolio(APIView):
    def post(self, request):
        # Helper function to generate SOAP payload with a given page number
        def generate_payload(page_number):
            return f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns="http://www.juniper.es/webservice/2007/">
              <soapenv:Header/>
              <soapenv:Body>
                <HotelPortfolio>
                  <HotelPortfolioRQ Version="1.1" Language="en" Page="{page_number}" RecordsPerPage="500">
                    <Login Email="{USER}" Password="{PASSWORD}"/>
                  </HotelPortfolioRQ>
                </HotelPortfolio>
              </soapenv:Body>
            </soapenv:Envelope>"""

        # Function to fetch total pages
        def fetch_total_pages():
            # Private
            pass

        # Define the headers
        

        # Fetch total pages
        total_pages = fetch_total_pages()

        # Process subsequent pages
        for page_number in range(1, total_pages + 1):
            # Private
            pass

        return Response({"status": "Hotels data saved successfully"}, status=status.HTTP_200_OK)


class HotelAvailability(APIView):
    def post(self, request):
        # Parse the incoming JSON data
        request_data = request.data

        # Transform JSON to SOAP
        soap_request = self.json_to_soap(request_data)

        # Define the headers
        headers = {
            'Content-Type': 'text/xml; charset=utf-8',
        }

        # private

    def json_to_soap(self, json_data):
        # private
        pass

class HotelBookingRules(APIView):
    def post(self, request):
        # Parse the incoming JSON data
        request_data = request.data

        # Transform JSON to SOAP
        soap_request = self.json_to_soap(request_data)

        # Define the headers
        headers = {
            'Content-Type': 'text/xml; charset=utf-8',
        }

        # private
        pass

    def json_to_soap(self, json_data):
        # private
        pass

class HotelBooking(APIView):
    def post(self, request):
        # Parse the incoming JSON data
        request_data = request.data

        # Transform JSON to SOAP
        soap_request = self.json_to_soap(request_data)

        # Transform JSON to SOAP
        soap_request = self.json_to_soap(request_data)

        # Define the headers
        headers = {
            'Content-Type': 'text/xml; charset=utf-8',
        }

        link = URL_BASE+'BookTransactions.asmx'
        # private
        # pass

    def json_to_soap(self, json_data):
        # Extracting data from JSON
        pass
    
    def build_pax_xml(self, pax):
        # private
        pass

    def build_rel_pax_dist_xml(self, dist):
        # private
        pass


class HotelReadBooking(APIView):
    def post(self, request):
        # Parse the incoming JSON data
        request_data = request.data

        # Transform JSON to SOAP
        soap_request = self.json_to_soap(request_data)

        # Define the headers
        headers = {
            'Content-Type': 'text/xml; charset=utf-8',
        }

        link = URL_BASE+'BookTransactions.asmx'

        # Send the SOAP request
        #private
        pass     
     
    def json_to_soap(self, json_data):
        # Extracting data from JSON
        version = json_data['ReadRQ']['Version']
        language = json_data['ReadRQ']['Language']
        reservation_locator = json_data['ReadRQ']['ReservationLocator']

        return f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns="http://www.juniper.es/webservice/2007/">
          <soapenv:Header/>
          <soapenv:Body>
              <ReadBooking>
                  <ReadRQ Version="{version}" Language="{language}">
                      <Login Email="{USER}" Password="{PASSWORD}"/>
                      <ReadRequest ReservationLocator="{reservation_locator}"/>
                  </ReadRQ>
              </ReadBooking>
          </soapenv:Body>
        </soapenv:Envelope>"""
    

class HotelCancelBooking(APIView):
    def post(self, request):
        # Parse the incoming JSON data
        request_data = request.data

        # Transform JSON to SOAP
        soap_request = self.json_to_soap(request_data)

        # Define the headers
        headers = {
            'Content-Type': 'text/xml; charset=utf-8',
        }

        link = URL_BASE+'BookTransactions.asmx'

        #private
        pass    
     
    def json_to_soap(self, json_data):
        # Extracting data from JSON
        version = json_data['CancelRQ']['Version']
        language = json_data['CancelRQ']['Language']
        reservation_locator = json_data['CancelRQ']['ReservationLocator']

        return f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns="http://www.juniper.es/webservice/2007/">
          <soapenv:Header/>
          <soapenv:Body>
              <CancelBooking>
                  <CancelRQ Version="{version}" Language="{language}">
                      <Login Email="{USER}" Password="{PASSWORD}"/>
                      <CancelRequest ReservationLocator="{reservation_locator}"/>
                  </CancelRQ>
              </CancelBooking>
          </soapenv:Body>
        </soapenv:Envelope>"""


class HotelCancelBooking(APIView):
    def post(self, request):
        # Parse the incoming JSON data
        request_data = request.data

        # Transform JSON to SOAP
        soap_request = self.json_to_soap(request_data)

        # Define the headers
        headers = {
            'Content-Type': 'text/xml; charset=utf-8',
        }

        link = URL_BASE+'BookTransactions.asmx'

         # Send the SOAP request
        response = requests.post(link, data=soap_request, headers=headers)

        #private
        pass    
     
    def json_to_soap(self, json_data):
        # Extracting data from JSON
        version = json_data['CancelRQ']['Version']
        language = json_data['CancelRQ']['Language']
        reservation_locator = json_data['CancelRQ']['ReservationLocator']

        return f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns="http://www.juniper.es/webservice/2007/">
          <soapenv:Header/>
          <soapenv:Body>
              <CancelBooking>
                  <CancelRQ Version="{version}" Language="{language}">
                      <Login Email="{USER}" Password="{PASSWORD}"/>
                      <CancelRequest ReservationLocator="{reservation_locator}"/>
                  </CancelRQ>
              </CancelBooking>
          </soapenv:Body>
        </soapenv:Envelope>"""


class HotelBookingList(APIView):
    def post(self, request):
        # Parse the incoming JSON data
        request_data = request.data

        # Transform JSON to SOAP
        soap_request = self.json_to_soap(request_data)

        # Define the headers
        headers = {
            'Content-Type': 'text/xml; charset=utf-8',
        }

        link = URL_BASE+'BookTransactions.asmx'

         # Send the SOAP request
        response = requests.post(link, data=soap_request, headers=headers)

        #private
        pass    
     
    def json_to_soap(self, json_data):
        #private
        pass    

        return f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns="http://www.juniper.es/webservice/2007/">
          <soapenv:Header/>
          <soapenv:Body>
              <BookingList>
                  <BookingListRQ Version="{version}" Language="{language}">
                      <Login Email="{USER}" Password="{PASSWORD}"/>
                      <BookingListRequest>
                          <ModificationBookingDate From="{start_date}" To="{end_date}"/>
                      </BookingListRequest>
                      <AdvancedOptions>
                          <AllStatus>{all_status}</AllStatus>
                      </AdvancedOptions>
                  </BookingListRQ>
              </BookingList>
          </soapenv:Body>
        </soapenv:Envelope>"""

