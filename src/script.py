import requests
import gspread
import csv
from env_creds import WORKSHOP_PASSWORD, WORKSHOP_URL, CSV_PATH
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials


def get_data():
    # Check we have the Password / URL...
    if not WORKSHOP_PASSWORD or not WORKSHOP_URL:
        raise ValueError('No Workshop URL or Password set. Please set using .env file')
        return

    # Form the payload and send to server...
    payload = {'pass' : WORKSHOP_PASSWORD, 'enter' : 'Submit'}
    request = requests.post(WORKSHOP_URL, data=payload)

    if request.status_code > 300:
        raise ValueError('Error with external service.')

    # Instantiate a new parser...
    parser = BeautifulSoup(request.content, 'html.parser')

    # Open the CSV file to write...    
    csv_file = open(CSV_PATH, 'w+')
    csv_writer = csv.writer(csv_file)

    # loop all the rows in the table to get the values...
    for row in parser.find('table').find_all('tr'):
        csv_writer.writerow([x.text for x in row.find_all('td')])
    
    csv_file.close()
    print('CSV Generated')


if __name__ == "__main__":
    get_data()

