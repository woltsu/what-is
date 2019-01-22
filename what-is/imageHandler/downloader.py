from requests import get
from PIL import Image
import threading
import os
import sys
import json
import shutil

class Download(threading.Thread):
  def __init__(self, to, src, name, size, callback):
    threading.Thread.__init__(self,name = os.urandom(16))
    self.to = to
    self.src = src
    self.name = name
    self.size = size
    self.callback = callback

  def run(self):
    try:
      with open(f'{self.to}{self.name}', 'wb') as f:
        response = get(self.src, timeout=10)
        f.write(response.content)
        img = Image.open(f'{self.to}{self.name}')
        img = img.resize(self.size, Image.ANTIALIAS)
        img.save(f'{self.to}{self.name}')
    except:
      pass
    finally:
      self.callback()

class Downloader():
  API_URL='https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&searchType=image&start={start}'
  OUT_DIR='imgs/'
  SIZE=(600,600)
  LIMIT=50

  def __init__(self):
    self.downloaded = 0

  def fetchLinks(self, target):
    start = 1
    res = []
    try:
      while start <= (self.LIMIT - 10) + 1:
        response = get(
          self.API_URL.format(
            key=os.environ['API_KEY'],
            cx=os.environ['CX'],
            query=target,
            start=start
          )
        )
        responseJson = json.loads(response.text)
        items = responseJson['items']
        start += 10
        res += list(map(lambda item: item['link'], items))
    except:
      print('Failed fetching image sources. Probably an issue with the api key or cx.')
      sys.exit()
    return res

  def callback(self, total):
    def progress():
      self.downloaded += 1
      sys.stdout.write(f'\rDownloaded image {self.downloaded} of {total}')
    return progress

  def downloadImages(self, target):
    print('Fetching image sources...')
    self.downloaded = 0
    if os.path.exists(os.path.dirname(self.OUT_DIR)):
      shutil.rmtree(self.OUT_DIR)
    os.makedirs(self.OUT_DIR, 0o755)

    links = self.fetchLinks(target)
    threads = []
    for i,link in enumerate(links):
      download = Download(
        to=self.OUT_DIR,
        src=link,
        name=f'{i + 1}.jpg',
        size=self.SIZE,
        callback=self.callback(len(links))
      )
      download.start()
      threads.append(download)
    for t in threads:
      t.join()
    sys.stdout.write('\n')
