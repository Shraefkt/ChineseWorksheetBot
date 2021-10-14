from bs4 import BeautifulSoup
import requests
from urllib import parse
def scrape(filename) :
    with open(filename,"r",encoding="utf-8") as f:
        words = f.readlines()
    sentences = {}
    for word in words:
        word = word.strip()
        query = parse.quote(word)
        query = query.replace("%0A","")
        page = requests.get(f"http://www.ichacha.net/zaoju/{query}.html")
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all("li", style="text-align:left")
        try:
            result = str(results[1])
            i = 1
            while "<a" in result:
                i+=1
                result = str(results[i])
        except:
            result = str(results[0])

        result = result.replace("<li style=\"text-align:left\">", "")
        result = result.replace("<font color=\"#cc0033\">","")
        result = result.replace("</font>", "")
        result = result.replace("</li>", "")

        sentences[word] = result
    return sentences


