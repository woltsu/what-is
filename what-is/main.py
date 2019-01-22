from dotenv import load_dotenv
from imageHandler import downloader, analyzer
import os

if __name__ == '__main__':
  load_dotenv()
  downloader = downloader.Downloader()
  analyzer = analyzer.Analyzer(downloader.OUT_DIR, downloader.SIZE)
  target = input('What is: ')
  downloader.downloadImages(target)
  analyzer.analyzeImages()
