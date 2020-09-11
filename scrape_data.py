# WIKIPEDIA page with all the physics discoveries.
# https://en.wikipedia.org/wiki/Timeline_of_fundamental_physics_discoveries

import requests
import bs4
import csv
import re

# Website that I used to scrape the data. Because it was easier to clean.
URL = 'https://steemit.com/physics/@danielcayee/timeline-of-fundamental-physics-discoveries'

# Get request
res = requests.get(URL)
# Check for errors
res.raise_for_status()

# Create soup object
soup = bs4.BeautifulSoup(res.content, 'html.parser')

# Get the section of the page where all discoveries are listed
content = soup.find(class_='MarkdownViewer').next_element.next_element

# Create an array that cointains all the discoveries
full_desc = content.text.split('\n')

all_data = []

for i in full_desc:
    i = i.strip()
    # Get the data with regex
    pattern = '([0-9]{4,4})|([0-9]{3,3} BCE)'
    match = re.findall(pattern, i)
    if match != []:
        date = match[0][0] if match[0][0] != '' else match[0][1]
    i = re.sub(pattern, '', i).strip()

    if ':' in i:
        # Get the person and the discovery
        discovery, person = i.split(':')
    else:
        # Get the discovery if the person is not defined
        person = 'NaN'
        discovery = i
    all_data.append((date.strip(), person.strip(), discovery.strip()))


#Create csv file with the data
with open('physics_discoveries.csv', 'w') as csv_file:
    fieldnames = ['Date', 'Person', 'Discovery']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    for i in all_data: 
        csv_writer.writerow({'Date': i[0], 'Person': i[1], 'Discovery': i[2]})
