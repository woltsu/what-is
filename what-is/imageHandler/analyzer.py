from PIL import Image
import os
import sys

class Analyzer():
  LIMIT = 100

  def __init__(self, src, imageSize):
    self.src = src
    self.imageSize = imageSize

  def getAveragePixels(self):
    width, height = self.imageSize
    total = min(len(os.listdir(self.src)), self.LIMIT)
    result = [[(0, 0, 0) for x in range(width)] for y in range(height)]
    for i,item in enumerate(os.listdir(self.src)):
      if i + 1 > self.LIMIT:
        break
      sys.stdout.write(f'\rAnalyzing images... {round(((i + 1) / total) * 100)}%')
      try:
        img = Image.open(f'{self.src}{item}')
        pix = img.load()
        for x in range(width):
          for y in range(height):
            r1,g1,b1 = pix[x, y]
            r2,g2,b2 = result[x][y]
            result[x][y] = (r1+r2, g1+g2, b1+b2)
      except:
        continue
    pixels = []
    for x in range(width):
      for y in range(height):
        r,g,b = result[x][y]
        result[x][y] = (round(r/total), round(g/total), round(b/total))
    for y in range(width):
      for x in range(height):
        pixels.append(result[x][y])
    return pixels

  def analyzeImages(self):
    if not os.path.exists(os.path.dirname('output/')):
      os.makedirs('output/', 0o755)
    
    width, height = self.imageSize
    result = Image.new('RGB', (width,height))    
    result.putdata(self.getAveragePixels())
    result.save('output/result.jpg')
    show = input('\nDone! Would you like to see the result? (y/N) ')
    if (show == 'y'):
      result.show()
    print(f'The result is located at /output/result.jpg')
      