import requests
from bs4 import BeautifulSoup
import json

# # premier scrapping

# url ='https://youtubemp4.to/download_ajax/'  #URL à scraper

# # recuperer la page à scraper

# datas = {
#     'url': 'https://www.youtube.com/watch?v=8NyParAaNos'
# }

# response = requests.post(url, data=datas)


# # Parser le resultat en HTML pour l'exploitation

# html_soup = BeautifulSoup(response.text, 'html.parser')


# # Verifier que le scrapping à marché

# print(response.text)
# # tout va bien


# # Deuxième scrapping

url_you ='https://www.youtube.com/watch?v=BhB5uXdO73M'  #URL à scraper

# recuperer la page à scraper

url ="https://www.4kdownload.com/taskio/parse/?media_url={}".format(url_you)

response = requests.get(url)

result = json.loads(response.text)
print(result)
result = result['task']['task_id']


# Début deuxième lien
url ='https://www.4kdownload.com/taskio/tasks/?task_id={}'.format(result)  #URL à scraper



response = requests.get(url)

result = json.loads(response.text)
result= result[0]['task_result']['results']

print(result)