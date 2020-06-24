import requests
from bs4 import BeautifulSoup
import csv

source = requests.get("https://coreyms.com/").text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video link'])


for article in soup.find_all('article'):

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)



    try:
        video_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = video_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        ytlink = f'https://youtube.com/watch?v={vid_id}'

    except Exception as e:
        ytlink = None
    print(ytlink)
    print()

    csv_writer.writerow(([headline, summary, ytlink]))

csv_file.close()
