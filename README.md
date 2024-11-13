# HIPPASPACE-API

**HIPAASpace API For Fax Numbers Documentation** <br>
This repo is designed for a circumstance of a small business having a CSV of pharmacy leads with phone numbers, but in need of corresponding fax numbers. This repo will show how to use the HIPAASPACE API to search for unique phone numbers, return the fax number on record, and how to join this data to your CSV.

**Overview:** <br>
The REST/SOAP HIPAASpace API offers a fleet of web services that grant access to healthcare-related data. It includes services for medical data lookup (like NPI, HCPCS, and NDC), crosswalking (ICD-9 to ICD-10 conversions), and validation services for various healthcare codes. 

There are many data points available to you through this API as well as fax numbers that could prove to be very beneficial, some of these being: official organization name, mailing address, phone numbers, enumeration dates, authorized official name and title, taxonomy code, etc.

**How-To:** <br>
Obtain your API token:
Visit the [API Get Started page](https://www.hipaaspace.com/medical_web_services/medical_coding_web_services.aspx) to obtain and activate a free trial token. This trial is 30 days or 500 total calls. They do not track usage based on IP, so you can use as many emails as you’d like for as many trials as you need.
The token can be upgraded via subscription. The lowest tier subscription available is 30,000 calls per month for $179.00 per month.
I suggest using their [API Playground/Documentation](https://www.hipaaspace.com/medical_web_services/test.drive.restful.web.services?Type=NPI#CodeExamples) for testing as you won’t tap into your own call limit and will allow you to get used to the API.

**Implement Code:** <br>
This Python script (main.py) is written to create a function where the appropriate parameters to the API are declared to use Phone numbers from a Google Sheets file to use as a lookup to HIPAASpace to get the corresponding Fax numbers from HIPAASpace. (Phone is a reliable 1:1 data point, as in where a business name or address can be unreliable since spelling, grammar, and punctuation can vary across domains.)
Since there are several records for the same business, the code loops through all results until it finds a fax number or exhausts all options.
Since I do not have access to advanced stacks/integrations, I kept it simple with an output to a local .csv with the phone numbers and corresponding fax numbers.
To run this Python script yourself, all to be changed is your API token, your list of phone numbers, and the .csv export location/path.
The phone numbers need to be in quotes delimited by commas, so an easy way to do this is the Sheets function ="'" & A1 & "'" & “,”
If the phone numbers on the Sheet are in (xxx) xxx-xxxx format, but in the Python list they need to be in a xxx-xxx-xxxx format. An easy way to do this is a find/replace in Google Sheets. Replace ‘(‘ with blank and ‘) ‘ with ‘-’. 

**Bring into sheets:** <br>
There are various ways to bring this data gathered back into the Google Sheet, but here is a straightforward way.
Add a sheet to the Google Sheet doc with the new data csv.
Modify the phone number on your new sheet to revert to the old format of (xxx) xxx-xxxx. This can be done with regex in sheets as a formula: =REGEXREPLACE(A1, "(\d{3})-(\d{3})-(\d{4})", "($1) $2-$3")
Use a VLOOKUP on the fax column to join/match on the phone numbers: =VLOOKUP(A1, Sheet2!A:B, 2, FALSE). This brings in the fax numbers.

**Notes:** <br>
Not every single fax number will be available from this API, but a majority will.
This API can also be utilized to bring in new info and new prospects/leads.
Depending on your stack, the export transformation could be smoothed out/handled code side if this process will be used extensively.

**Links:** <br>
API Get Started Page: https://www.hipaaspace.com/medical_web_services/medical_coding_web_services.aspx <br>
API Playground/Documentation: https://www.hipaaspace.com/medical_web_services/test.drive.restful.web.services?Type=NPI#CodeExamples 
