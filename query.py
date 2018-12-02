import urllib.request
import re
import time

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

#url="https://www.sigmaaldrich.com/catalog/search?term=292249&interface=All&N=0&mode=match partialmax&lang=en&region=US&focus=product"
url_pre="https://www.sigmaaldrich.com/catalog/search?term="
url_post="&interface=All&N=0&mode=match partialmax&lang=en&region=US&focus=product"


filepath = 'input.txt'
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        #print("Processing Line {}: {}".format(cnt, line.strip()))
        url = url_pre+line.strip()+url_post
        #print (url)
        #exit()

        opener = AppURLopener()

        response = opener.open(url)
        html=response.read()
        htmlString =html.decode("utf-8")
        #print(html)

        #s = "Linear Formula: BF3 · C2H5NH2 Molecular Weight"
        result = re.search('Linear\sFormula:(.*)Molecular\sWeight', htmlString)
        formula = ""
        if (result and result.group(1)):
            formula = result.group(1)
        print (line.strip() + " : " + formula)
        time.sleep(2)

        line = fp.readline()
        cnt += 1
