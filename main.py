import sys
import requests
from bs4 import BeautifulSoup

# Take username as input
# Do GET request to get Github user's homepage
user = sys.argv[1]
url = 'https://github.com/' + user
r = requests.get(url)
# Check if GET request suceeds, otherwise show error
assert r.status_code == 200
# The HTML of the user's homepage
data = r.text

# Use BeautifulSoup API to get pinned repositories from
# user page.
soup = BeautifulSoup(data,'html.parser')
# Get the containers for pinned repos
repos = soup.find_all('div',{'class': 'pinned-item-list-item-content'})

repos_data = []
# Display the titles of the repos
for repo in repos:
  title = repo.find('span', {'class': 'repo'}).text
  desc = repo.find('p', {'class': 'pinned-item-desc'}).text.strip()
  repos_data.append((title, desc))
print(repos_data)