import requests
from bs4 import BeautifulSoup

#links
prosite_url = "https://prosite.expasy.org/cgi-bin/prosite/prosite_browse.cgi?order=hits%20desc&type=all"
desc_url = "https://prosite.expasy.org/accession_number"

#Requests part
prosite_response = requests.get(prosite_url)
if prosite_response:
    print("Prosite URL response successful")
else:
    raise Exception(f"Prosite URL Error; status code : {prosite_response.status_code}")

desc_response = requests.get(desc_url)
if desc_response:
    print("Description URL successful")
else:
    raise Exception(f"Description URL Error; status code: {desc_response.status_code}")

#Web Scrapping part
prosite_soup = BeautifulSoup(prosite_response.text, "html.parser")
desc_soup = BeautifulSoup(desc_response.text, "html.parser")

rows = prosite_soup.find_all('tr')

data = []
for row in rows:
    cols = row.find_all('td')
    ac = cols[0].text.strip()
    id = cols[1].text.strip()
    entry_type = cols[2].text.strip()

desc = desc_soup.find('div', {'class': 'description-class'})
desc_text = ""

if desc:
    desc_text = desc.text.strip()
else:
    desc_text = "none"

data.append({
    'AC': ac,
    'ID': id,
    'entry_type': entry_type,
    'description': desc_text
})

print(data)