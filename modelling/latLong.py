import bs4 as bs
import urllib.request
import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 10000)
pd.set_option('display.width', 1000)

source = urllib.request.urlopen('https://developers.google.com/public-data/docs/canonical/countries_csv').read()
soup = bs.BeautifulSoup(source, 'lxml')
table = soup.find('table')
table_rows = table.find_all('tr')

rows = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    rows.append(row)

df = pd.DataFrame(rows, columns=['ISO2', 'latitude', 'longitude', 'country'])
df = df.iloc[1:, :]

# Export df to csv
df.to_csv('latLong.csv', index=False)