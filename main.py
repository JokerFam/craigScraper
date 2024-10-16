# main.py

import requests
import time
from bs4 import BeautifulSoup as bs

# part 1
url = f'https://denver.craigslist.org/search/remote-jobs#search=2~thumb~0~0'

page = requests.get(url)
# print(page.text)

# part 2
soup = bs(page.content, "html.parser")
results = soup.find_all('a')

count = 0
for job in results:
    job_link = job.find('a')
    job_title = job.find(class_='title')
    job_price = job.find(class_='price')
    print(f'{job_link}\n{job_title}\n{job_price}\n\n')
    count += 1

print(f'The number of job opporrunities is {count}')
