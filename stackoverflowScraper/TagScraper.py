import sys
import requests
import time
from bs4 import BeautifulSoup

# https://stackoverflow.com/tags
# https://stackoverflow.com/questions/tagged/three.js
class TagScraper:
    #
    def __inf__(self):
        """
        creates an TagScraper Object
        """
        pass

    # https://stackoverflow.com/questions/tagged/three.js?page=1&sort=newest&pagesize=50
    def scrapeTagForTags (self):
        placeToStoreResults = "../results/"

        tag = "three.js"
        url = "https://stackoverflow.com/questions/tagged/"
        sort = "newest"
        pagesize = 50 # 15, 30 or 50
        page = 1

        # Preparing Files
        tagFile = placeToStoreResults + tag + ".txt"  # Name of text file coerced with +.txt
        tagFile = open(tagFile, 'w') # ATTENTION: overwrites file


        totalUrl = "" + url + tag + "?page=" + str(page) + "&sort=" + sort + "&pagesize=" + str(pagesize)

        r = requests.post(totalUrl)
        totalQuestionOverview = BeautifulSoup(r.content, 'html.parser')

        findLinks = totalQuestionOverview.find_all("a", {'class':"question-hyperlink"}) # n Elements
        for link in findLinks:
            print(link)
            # finishedURL





if __name__ == "__main__":
    tagScraper = TagScraper()
    tagScraper.scrapeTagForTags()