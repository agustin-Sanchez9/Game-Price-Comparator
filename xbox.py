from bs4 import BeautifulSoup as bs4
from playwright.sync_api import sync_playwright


def setUrl(gameName):
    gameNameAdapted = gameName.replace(" ","+")
    url = 'https://www.xbox.com/es-AR/search/results/games?q='+ gameNameAdapted +'&PlayWith=PC'
    return url


def search(game):
    url = setUrl(game)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            geolocation={"longitude": -34.6314592, "latitude": -58.3609427},
            permissions=["geolocation"])
        page = context.new_page()
        page.goto(url)

        result = page.content()
        page.close()  
        browser.close()

    doc = bs4(result, "html.parser")
    gameList = doc.find("div", class_="ModuleRow-module__row___N1V3E SearchProductGrid-module__productGrid___c2ZVh")

    if not gameList:
        print("NO SE ENCONTRO EL JUEGO EN XBOX.")
        return

    gameData = gameList.find("a")

    if not gameData:
        print("NO SE ENCONTRO EL JUEGO EN XBOX.")
        return

    gameTitle = gameData.find("span", class_="ProductCard-module__title___nHGIp typography-module__xdsBody2___RNdGY")
    gameOrPrice = gameData.find("span", class_="Price-module__originalPrice___XNCxs")
    gameDiscount = gameData.find("div", class_="ProductCard-module__discountTag___OjGFy typography-module__xdsBody2___RNdGY")
    gameFinalPrice = gameData.find("span", class_="Price-module__boldText___1i2Li Price-module__moreText___sNMVr ProductCard-module__price___cs1xr")
    gameFinalPrice2 = gameData.find("span", class_="Price-module__boldText___1i2Li Price-module__moreText___sNMVr ProductCard-module__price___cs1xr Price-module__listedDiscountPrice___A-+d5")

    gameFinalPrice3 = gameFinalPrice if gameFinalPrice else gameFinalPrice2

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
