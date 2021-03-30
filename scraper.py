import requests
import pandas as pd
from bs4 import BeautifulSoup


def scrape():
    try:
        datasets = [
            'hospital-beds',
            'non-covid-icu-beds',
            'ventilators'
        ]

        for d in datasets:
            url = f'https://delhifightscorona.in/data/{d}/'

            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

            beds_table = soup.find(id='beds').find('tbody')
            rows = beds_table.find_all('tr')

            hospitals = []

            for row in rows:
                data = row.find_all('td')

                hospital = dict()

                hospital['name'] = data[0].find('h5').get_text()
                hospital['address'] = data[0].find('address').get_text()
                hospital['contact'] = str(data[0].find('a').get_text())

                hospital['label'] = data[1].find(class_='label').get_text()

                hospital['total'] = int(data[2].get_text())
                hospital['vacant'] = int(data[3].get_text())

                hospitals.append(hospital)

            df = pd.DataFrame(hospitals)
            df.to_csv(f'data/{d}.csv', index=False)
            print(f'Saved data/{d}.csv')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    scrape()
