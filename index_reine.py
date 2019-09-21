# importation

import requests
from bs4 import BeautifulSoup
import json

# Utilisation
# url_moi='https://www.4kdownload.com/taskio/tasks/?task_id=b1519ecb-5353-4e6a-bb27-0f53d5491a27'
# url = 'https://www.4kdownload.com/taskio/parse/?media_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DDyX-QZZBgpw' #URL à scraper

# recuperer la page à scraper

url_videoyou= 'https://www.youtube.com/watch?v=DyX-QZZBgpw'

url= 'https://www.4kdownload.com/taskio/parse/?media_url={}'.format(url_videoyou)

response= requests.get(url)

resultat= response.text

contenu = json.loads(resultat)

task = contenu['task']['task_id']

url_2 = 'https://www.4kdownload.com/taskio/tasks/?task_id={}'.format(task)
response_2 = requests.get(url_2)

resultat_2 = response_2.text
contenu_2 = json.loads(resultat_2)
task_result = contenu_2[0]['task_result']['results']

print(task_result)

for task in task_result:
      if task['format']=="MP4" and task["resolution"]=="360p":
          best = task
          break
print(best)
