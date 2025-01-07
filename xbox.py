from bs4 import BeautifulSoup as bs4
import requests


def setUrl(gameName):
    gameNameAdapted = gameName.replace(" ","+")
    url = 'https://www.xbox.com/es-AR/search/results/games?q='+ gameNameAdapted +'&PlayWith=PC'
    return url


def search(game):
    url = setUrl(game)

    result = requests.get(url).text
    doc = bs4(result, "html.parser")
    gameList = doc.find("div", class_="ModuleRow-module__row___N1V3E SearchProductGrid-module__productGrid___c2ZVh")
    gameData = gameList.find("a")

    gameTitle = gameData.find("span", class_="ProductCard-module__title___nHGIp typography-module__xdsBody2___RNdGY")
    gameOrPrice = gameData.find("span", class_="Price-module__originalPrice___XNCxs")
    gameDiscount = gameData.find("div", class_="ProductCard-module__discountTag___OjGFy typography-module__xdsBody2___RNdGY")
    gameFinalPrice = gameData.find("span", class_="Price-module__boldText___1i2Li Price-module__moreText___sNMVr ProductCard-module__price___cs1xr")
    gameFinalPrice2 = gameData.find("span", class_="Price-module__boldText___1i2Li Price-module__moreText___sNMVr ProductCard-module__price___cs1xr Price-module__listedDiscountPrice___A-+d5")


    # the class for the 
    if gameFinalPrice:
        gameFinalPrice3 = gameFinalPrice
    elif gameFinalPrice2:
        gameFinalPrice3 = gameFinalPrice2


    if gameTitle:
        # some games dont have prices, that is why the else statement here
        price = gameOrPrice.text if gameOrPrice else (gameFinalPrice.text if gameFinalPrice else '-')
        discount = gameDiscount.text if gameDiscount else '-'
        finalPrice = gameFinalPrice3.text if gameFinalPrice3 else '-'

    print("///////////////XBOX RESULTS///////////////")
    print("TITLE: " + gameTitle.text)
    print("ORIGINAL PRICE: " + price)
    print("DISCOUNT: " + discount)
    print("FINAL PRICE: " + finalPrice)
    print("///////////////////////////////////////////")
