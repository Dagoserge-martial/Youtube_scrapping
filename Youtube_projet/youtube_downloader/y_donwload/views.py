from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json

# Create your views here.
def home(request):

    url ='https://youtubemp4.to/download_ajax/'
    datas = {
        'url': 'https://www.youtube.com/watch?v=8NyParAaNos'
    }

    response = requests.post(url, data=datas)


    # Parser le resultat en HTML pour l'exploitation

    html_soup = BeautifulSoup(response.text, 'html.parser')


    # Verifier que le scrapping à marché

    # print(response.text)
    result = response.text
    result = json.loads(result)
    data_html = result['result']
    data = {
        'code': data_html
    }
    # tout va bien
    return render(request, 'index.html', data)