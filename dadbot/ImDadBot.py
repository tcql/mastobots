from ananas import PineappleBot, reply, html_strip_tags
import re

class ImDadBot(PineappleBot):
  @reply
  def im_dad(self, mention, user):
    match = re.match(r"(.*)?i'?m\s(.*)", html_strip_tags(mention["content"]), re.I)
    if (match != None):
      post = "@{0} hi {1}, i'm dad!".format(user["acct"], match.group(2))
      lentest = len(post)
      if (mention['spoiler_text'] != None):
        lentest += len(mention['spoiler_text'])
      if (lentest > 500):
        post = "sorry @{0}, that name was too long for me to understand... but i'm dad!".format(user["acct"])

      self.mastodon.status_post(post,
        in_reply_to_id = mention["id"],
        visibility = mention["visibility"],
        spoiler_text = mention["spoiler_text"])
