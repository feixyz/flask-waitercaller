import urllib.request
import urllib.parse
import json
import config

TOKEN = config.bitly_token
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}&format=json"

class BitlyHelper:

    def shorten_url(self, longurl):
        try:
            longurl = urllib.parse.quote(longurl, '.')
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            print(url)
            response = urllib.request.urlopen(url).read()
            jr = json.loads(response.decode())
            print(jr)
            return jr["data"]["url"]
        except Exception as e:
            print(e)
            return 'Failed to obtain a short url from bitly'