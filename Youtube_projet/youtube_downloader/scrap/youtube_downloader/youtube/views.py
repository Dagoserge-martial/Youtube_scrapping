from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json

# Create your views here.

def home(request):
    url ='https://youtubemp4.to/download_ajax/'  #URL à scraper

    # recuperer la page à scraper
    datas={
        'url': "https://www.youtube.com/watch?v=8CYllfGkmLw",
    }
    response = requests.post(url,data=datas)


    # Parser le resultat en HTML pour l'exploitation

    html_soup = BeautifulSoup(response.text, 'html.parser')


    # Verifier que le scrapping à marché

    result=response.text
    result=json.loads(result)
    data_html=result['result']
    data={
        'code':data_html
    }
    
    return render(request,'index.html',data)

def audio(request):
    url ="https://www.4kdownload.com/taskio/parse/?media_url={}".format('https://www.youtube.com/watch?v=SqxZCVg_u_w')  #URL à scraper
    url_final="https://www.4kdownload.com/taskio/tasks/?task_id={}"
    response = requests.get(url)
    # print(response.status_code,'==============-----------')
    response=json.loads(response.text)
    task=response['task']['task_id']
    url_final=url_final.format(task)

    reponses=requests.get(url_final)
    # print('responses statut code ',reponses.status_code,'-=============================---')
    reponses=json.loads(reponses.text)
    result=reponses[0]['task_result']['results'][3]

    # print('finaal result =---------=',result,'===================')
    return render(request,'audio.html',{'result':result})
