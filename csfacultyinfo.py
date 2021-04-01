import requests
import json
from bs4 import BeautifulSoup

URL = 'https://cs.utdallas.edu/people/faculty/'

def main():
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, features='html5lib').tbody
    profs_html = soup.find_all('tr')
    profs_dict = { tr.td.find_all('a')[-1].text : {
        'utd_site': tr.td.find_all('a')[-1].get('href'),
        'position': ' '.join(tr.td.text.split('\n')[2:]).strip(),
        'email': tr.find_all('td')[1].a.text,
        'phone': tr.find_all('td')[1].text.strip().split('\n')[1],
        'website': tr.find_all('td')[1].find_all('a')[1].get('href') if len(tr.find_all('td')[1].find_all('a')) > 1 else None,
            }
            for tr in profs_html
        }
    with open('out.json', 'w') as f:
        f.write(json.dumps(profs_dict))

if __name__ == '__main__':
    main()
