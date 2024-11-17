import requests
from bs4 import BeautifulSoup

# Prosite link
prosite_url = "https://prosite.expasy.org/cgi-bin/prosite/prosite_browse.cgi?order=hits%20desc&type=all"

# Checks if the link works
prosite_response = requests.get(prosite_url)
if prosite_response:
    print("Prosite URL response successful")
else:
    raise Exception(f"Prosite URL Error; status code: {prosite_response.status_code}")

# Using bs4 we can parse through the html
prosite_soup = BeautifulSoup(prosite_response.text, "html.parser")

# finds the first pre (which matches the grid) and extracts its content
tag_pre = prosite_soup.find("pre")

# turns the grid into a text with several rows
grid = tag_pre.text.strip().split('\n')

# we essentially get the index of a column thanks to the name of said column displayed on the html
header = grid[0].split()
AC_col = header.index("AC")
ID_col = header.index("ID")
entry_type_col = header.index("entry_type")
desc_col = header.index("doc_AC")

# init a list which will contain all the info we want
data_list = []
for row in grid[2:]: # skips header (first line) and hyphens (second line)
    cols = row.split()
    AC = cols[AC_col]
    ID = cols[ID_col]
    entry_type = cols[entry_type_col]
    desc = cols[desc_col]
    print(desc)

    # Desc URL ; uses the value extracted from the AC_doc column
    desc_url = f"https://prosite.expasy.org/{desc}"

    # Checks if link works
    desc_response = requests.get(desc_url)
    if desc_response:
        # Parses the html doc
        desc_soup = BeautifulSoup(desc_response.text, 'html.parser')

        # finds & extract content from the first p tag, which happens to be the description here 
        tag_p = desc_soup.find('p')

        # turns the content into a text
        desc_text = tag_p.text.strip()
    else:
        print(f"Description URL Error; status code: {desc_response.status_code}. PDOC value used for link: {desc}")
        desc_text = "No description found"

    # adds all the values we need to the list
    data_list.append({
        'AC': AC,
        'ID': ID,
        'entry_type': entry_type,
        'description': desc_text
    })