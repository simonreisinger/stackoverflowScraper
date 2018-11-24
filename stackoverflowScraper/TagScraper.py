import sys
import requests
import re
from bs4 import BeautifulSoup
import time

# https://stackoverflow.com/tags
# https://stackoverflow.com/questions/tagged/three.js


class TagScraper:

    def __inf__(self):
        """
        creates an TagScraper Object
        """
        pass

    # https://stackoverflow.com/questions/tagged/three.js?page=1&sort=newest&pagesize=50
    @staticmethod
    def scrapetagfortags():
        placeToStoreResults = "../results/"
        
        # TODO auf arry zusammenfassen
        searchURLs = ["https://threejs.org/docs", "http://threejs.org/docs", "threejs.org/docs"] #TODO das letzte muesste reichen check this
        tag = "three.js"
        url = "https://stackoverflow.com/questions/tagged/"
        sort = "newest"
        pagesize = 50  # 15, 30 or 50

        # Preparing Files
        nametagfile = placeToStoreResults + tag + ".txt"  # Name of text file coerced with +.txt
        tagfile = open(nametagfile, 'w') # ATTENTION: overwrites file

        totalurlforpagenumber = "" + url + tag + "?page=1&sort=" + sort + "&pagesize=" + str(pagesize)
        rforpagenumber = requests.post(totalurlforpagenumber)
        bsForPageNumber = BeautifulSoup(rforpagenumber.content, 'html.parser')
        pagenNumbers = bsForPageNumber.find_all("span", {'class': "page-numbers"})
        maxPageNr = int(pagenNumbers[len(pagenNumbers)-2].contents[0])

        print("All pages: " + str(maxPageNr))
        for page in range(43, 75):
            print("Current pages: " + str(page))
            totalUrl = "" + url + tag + "?page=" + str(page) + "&sort=" + sort + "&pagesize=" + str(pagesize)
            r = requests.post(totalUrl)
            totalQuestionOverview = BeautifulSoup(r.content, 'html.parser')
            findLinks = totalQuestionOverview.find("div", {"id": "mainbar"}).find_all("a", {'class':"question-hyperlink"})  # 50 Elements

            print("current page: " + str(page))

            # print(findLinks)

            for link in findLinks:
                finishedUrl = "https://stackoverflow.com" + link.get("href")
                # print(finishedUrl)
                for searchURL in searchURLs:
                    rQuestion = requests.get(finishedUrl)
                    soupQuestion = BeautifulSoup(rQuestion.content, 'html.parser')
                    allUrlsOnPage = soupQuestion.find_all(href=re.compile(searchURL))
                    if len(allUrlsOnPage) > 0:
                        tagfile.writelines(finishedUrl + "\n")
                        print(finishedUrl)
                    for urlOnPage in allUrlsOnPage:
                        hrefx = urlOnPage.get("href")
                        tagfile.writelines(hrefx + "\n")
                        print(hrefx)
                    if len(allUrlsOnPage) > 0:
                        tagfile.writelines("\n")
                    time.sleep( 5 )
        tagfile.close()


if __name__ == "__main__":
    tagScraper = TagScraper()
    tagScraper.scrapetagfortags()
