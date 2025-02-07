import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_FA_Cup_finals"
r = requests.get(URL).text
soup = BeautifulSoup(r, "html.parser")
tables = soup.find_all('table')
#print("The number of tables is: ", len(tables))

for index, table in enumerate(tables):
    if "Results by team" in str(table):
        table_index = index
#print(table_index)
#print(tables[table_index].prettify())

finals_data = pd.DataFrame(columns = ["Club","Wins","Runner-ups", "Last final won"])

for row in tables[table_index].tbody.find_all('tr'):
    colnheader = row.find('th')
    coln = row.find_all('td')
    if coln:
        club = colnheader.text.strip()
        wins = coln[0].text.strip()
        runnup = coln[3].text.strip()
        last = coln[2].text.strip()
        
        tempdf = pd.DataFrame([{'Club':club,'Wins':wins,'Runner-ups':runnup,'Last final won':last}])
        finals_data = pd.concat([finals_data, tempdf], ignore_index = True)

finals_data.index = finals_data.index+1     # Fixing index to be one- instead of zero-based
print(finals_data)
