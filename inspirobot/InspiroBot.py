import io
import requests
import numpy as np
from PIL import Image
from inspirobot.quotes import quotes
from ananas import PineappleBot, schedule

counter = 0
reference = np.asarray(Image.open(open('./inspirobot/bad.jpg', 'rb'))).astype(np.float32)

def compareImages(A, B):
  error = np.absolute(A - B)
  rmse = np.mean((error**2).flatten())**0.5
  return (rmse <= 60) # are these images ~ similar?

class InspiroBot(PineappleBot):
  @schedule(hour=0, minute=0)
  @schedule(hour=2, minute=0)
  @schedule(hour=4, minute=0)
  @schedule(hour=6, minute=0)
  @schedule(hour=8, minute=0)
  @schedule(hour=10, minute=0)
  @schedule(hour=12, minute=0)
  @schedule(hour=14, minute=0)
  @schedule(hour=16, minute=0)
  @schedule(hour=18, minute=0)
  @schedule(hour=20, minute=0)
  @schedule(hour=22, minute=0)
  def post(self):
    global counter
    global reference

    if (counter >= len(quotes)):
      counter = 0

    generated = requests.get('http://inspirobot.me/api', {'generate': 'true'})
    if (generated.status_code == 200):
      imageData = requests.get(generated.text)
      img = np.asarray(Image.open(io.BytesIO(imageData.content))).astype(np.float32)

      if (compareImages(reference, img)):
        print('image is evil, skipping')
        return self.post()

      print('posting')
      media = self.mastodon.media_post(imageData.content, "image/jpeg")
      if (media['id'] is not None):
        quote = quotes[counter]
        counter += 1
        self.mastodon.status_post(quote, media_ids=[media['id']], sensitive=True)
    else:
      print('error')




