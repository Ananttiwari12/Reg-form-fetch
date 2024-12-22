import requests
from bs4 import BeautifulSoup
import os

def download_file():
    for ID in range(299674):
        url = f""
        local_filename = url.split('/')[-1]
        
        r = requests.get(url, stream=True, verify=False)
        if r.status_code != 200:
            continue
        
        # pdf is saved in folder /reg
        with open(f'reg/{ID}.pdf', 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    print('Downloaded all pdfs')
    
if __name__ == '__main__':
    if not os.path.exists('reg'):
        os.makedirs('reg')
    download_file()
