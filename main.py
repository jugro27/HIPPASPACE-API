import requests
import pandas as pd
from config import api_token,path
from phone_numbers import phone_numbers


# Define a function to get fax numbers from the API given a list of phone numbers
def get_fax_numbers(api_token, phone_numbers):
   fax_numbers = {}
   base_url = "https://www.hipaaspace.com/api/npi/search_with_predicates"


   for phone in phone_numbers:
       params = {
           # Query parameter: the phone number to search
           'q': phone,
           # Query filter parameter: specifies that the query should exactly match the phone number
           'qf': f"Phone:true:{phone}",
           # Return type parameter: specifies that the response should be JSON
           'rt': 'json',
           # Token to use/authenticate
           'token': api_token
       }
       try:
           response = requests.get(base_url, params=params)
           if response.status_code == 200:
               data = response.json()
               # Loop through all records to find a fax number
               fax_found = False
               for record in data['NPI']:
                   if 'PracticeLocationAddressFaxNumber' in record:
                       fax_numbers[phone] = record['PracticeLocationAddressFaxNumber']
                       fax_found = True
                       break
               if not fax_found:
                   fax_numbers[phone] = 'Fax number not found'
           else:
               fax_numbers[phone] = 'Failed to retrieve data'
               error_message = f"Failed to retrieve data: {response.status_code} - {response.reason}"
               print(error_message)
       except requests.exceptions.RequestException as e:
           print(f"Error with phone number {phone}: {e}")


   return fax_numbers


# Replace with your actual API token
api_token = api_token
# Add in phone numbers (list)
phone_numbers = phone_numbers


# Call function and assign to variable
fax_numbers = get_fax_numbers(api_token, phone_numbers)


# Creates a DataFrame from the fax_numbers dictionary with columns 'Phone Number' and 'Fax Number'
df = pd.DataFrame(list(fax_numbers.items()), columns=['Phone Number', 'Fax Number'])
# Replace with your path ('/your/path/fax_numbers.csv')
csv_filename = path
# Writes to CSV
df.to_csv(csv_filename, index=False)
