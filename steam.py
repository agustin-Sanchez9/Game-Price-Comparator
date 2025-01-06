from bs4 import BeautifulSoup as bs4
import requests


def setUrl(gameName):
    gameNameAdapted = gameName.replace(" ","+")
    url = 'https://store.steampowered.com/search/?term='+ gameNameAdapted +'&supportedlang=latam%2Cenglish%2Cspanish&category1=998&ndl=1'
    return url
    

def search(game):

    url = setUrl(game)

    result = requests.get(url).text
    doc = bs4(result, "html.parser")
    gameList = doc.find("div", id="search_resultsRows")
    gameData = gameList.find("a")

    gameTitle = gameData.find("span", class_="title")
    gameOrPrice = gameData.find("div", class_="discount_original_price")
    gameDiscount = gameData.find("div", class_="discount_pct")
    gameFinalPrice = gameData.find("div", class_="discount_final_price")

    if gameTitle:
        # some games dont have prices, that is why the else statement here
        price = gameOrPrice.text if gameOrPrice else (gameFinalPrice.text if gameFinalPrice else '-')
        discount = gameDiscount.text if gameDiscount else '-'
        finalPrice = gameFinalPrice.text if gameFinalPrice else '-'

    print("///////////////STEAM RESULTS///////////////")
    print("TITLE: " + gameTitle.text)
    print("ORIGINAL PRICE: " + price)
    print("DISCOUNT: " + discount)
    print("FINAL PRICE: " + finalPrice)
    print("///////////////////////////////////////////")

    
