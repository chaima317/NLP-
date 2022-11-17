import requests

class extract:
    def __init__(self):



    def wikipedia_page(title):
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






