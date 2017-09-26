import requests
from inspirobot.quotes import quotes
from ananas import PineappleBot, hourly, interval

counter = 0

class InspiroBot(PineappleBot):
  @interval(1200)
  def post(self):
    global counter
    if (counter > len(quotes)):
      counter = 0

    generated = requests.get('http://inspirobot.me/api', {'generate': 'true'})
    if (generated.status_code == 200):
      imageData = requests.get(generated.text)
      media = self.mastodon.media_post(imageData.content, "image/jpeg")

      if (media['id'] != None):
        quote = quotes[counter]
        counter += 1
        self.mastodon.status_post(quote + " \n" + media['url'], media_ids=[media['id']])
    else:
      print('error')
