from bs4 import BeautifulSoup as bs4
import requests
import time


def setUrl(gameName):
    gameNameAdapted = gameName.replace(" ","%20")
    url = 'https://www.gog.com/en/games?query='+ gameNameAdapted +'&order=desc:score&hideDLCs=true'
    return url

def search(game):
    url = setUrl(game)

    result = requests.get(url).text

    doc = bs4(result, "html.parser")
    gameList = doc.find("div", class_="paginated-products-grid grid")
    gameData = gameList.find("a")

    gameTitle2 = gameData.find("product-title", class_="small")
    gameTitle = gameTitle2.find("span")
    gameOrPrice = gameData.find("span", class_="base-value ng-star-inserted")
    gameDiscount = gameData.find("price-discount", class_="ng-star-inserted")
    gameFinalPrice = gameData.find("span", class_="final-value ng-star-inserted")

    if gameTitle:
        # some games dont have prices, that is why the else statement here
        price = gameOrPrice.text if gameOrPrice else (gameFinalPrice.text if gameFinalPrice else '-')
        discount = gameDiscount.text if gameDiscount else '-'
        finalPrice = gameFinalPrice.text if gameFinalPrice else '-'

    print("///////////////GOG RESULTS///////////////")
    print("URL: " + url)
    print("TITLE: " + gameTitle.text)
    print("ORIGINAL PRICE: " + price)
    print("DISCOUNT: " + discount)
    print("FINAL PRICE: " + finalPrice)
    print("///////////////////////////////////////////")

g = 'stardew valley'

search(g)
