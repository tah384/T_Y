import requests
from bs4 import BeautifulSoup

def extract_video_url(zee5_link):
    response = requests.get(zee5_link)
    soup = BeautifulSoup(response.content, 'html.parser')
    video_url = soup.find('meta', attrs={'property': 'og:video'})['content']
    return video_url
