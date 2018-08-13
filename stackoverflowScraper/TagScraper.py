import sys
import requests
import re
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

        searchURL = "https://threejs.org/docs"
        tag = "three.js"
        url = "https://stackoverflow.com/questions/tagged/"
        sort = "newest"
        pagesize = 50  # 15, 30 or 50

        # Preparing Files
        nameTagFile = placeToStoreResults + tag + ".txt"  # Name of text file coerced with +.txt
        tagFile = open(nameTagFile, 'w') # ATTENTION: overwrites file

        totalUrlForPageNumber = "" + url + tag + "?page=1&sort=" + sort + "&pagesize=" + str(pagesize)
        rForPageNumber = requests.post(totalUrlForPageNumber)
        bsForPageNumber = BeautifulSoup(rForPageNumber.content, 'html.parser')
        pagenNumbers = bsForPageNumber.find_all("span", {'class':"page-numbers"})
        maxPageNr = int(pagenNumbers[len(pagenNumbers)-2].contents[0])

        print("All pages: " + str(maxPageNr))
        for page in range(1, maxPageNr):
            totalUrl = "" + url + tag + "?page=" + str(page) + "&sort=" + sort + "&pagesize=" + str(pagesize)
            r = requests.post(totalUrl)
            totalQuestionOverview = BeautifulSoup(r.content, 'html.parser')
            findLinks = totalQuestionOverview.find_all("a", {'class':"question-hyperlink"})  # 50 Elements
            #i = 0
            print("current page: " + str(page))
            for link in findLinks:
                finishedUrl = "https://stackoverflow.com" + link.get("href")

                rQuestion = requests.get(finishedUrl)
                soupQuestion = BeautifulSoup(rQuestion.content, 'html.parser')
                allUrlsOnPage = soupQuestion.find_all(href=re.compile(searchURL))
                if(len(allUrlsOnPage) > 0):
                    tagFile.writelines(finishedUrl + "\n")
                for urlOnPage in allUrlsOnPage:
                    hrefx = urlOnPage.get("href")
                    tagFile.writelines(hrefx + "\n")
                    print(hrefx)
                if(len(allUrlsOnPage) > 0):
                    tagFile.writelines("\n")

                #if(i == 1):
                #    break
                #i = i+1

        tagFile.close()

if __name__ == "__main__":
    tagScraper = TagScraper()
    tagScraper.scrapeTagForTags()