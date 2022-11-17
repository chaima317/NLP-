import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
class Extract:

 def __init__(self) :
     super().__init__()
     self.text=self.wikipedia_page('Earth').lower()
     print(self.text)
     self.wordcloud=self.cerating_worldcloud()
 def wikipedia_page(self,title):
            '''
            This function returns the raw text of a wikipedia page
            given a wikipedia page title
            '''
            params = {
                'action': 'query',
                'format': 'json',  # request json formatted content
                'titles': title,  # title of the wikipedia page
                'prop': 'extracts',
                'explaintext': True
            }
            # send a request to the wikipedia api
            response = requests.get(
                'https://en.wikipedia.org/w/api.php',
                params=params
            ).json()

            # Parse the result
            page = next(iter(response['query']['pages'].values()))
            # return the page content
            if 'extract' in page.keys():
                return page['extract']
            else:
                return "Page not found"

        # We lowercase the text to avoid having to deal with uppercase and capitalized words



 def cerating_worldcloud(self):
     wordcloud = WordCloud(random_state=8,
                           normalize_plurals=False,
                           width=600, height=300,
                           max_words=300,
                           stopwords=[])
     # Apply the wordcloud to the text.
     return wordcloud



