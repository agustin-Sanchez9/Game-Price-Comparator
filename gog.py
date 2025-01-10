from bs4 import BeautifulSoup as bs4
from playwright.sync_api import sync_playwright


def setUrl(gameName):
    gameNameAdapted = gameName.replace(" ","%20")
    url = 'https://www.gog.com/en/games?query='+ gameNameAdapted +'&order=desc:score&hideDLCs=true'
    return url

def search(game):
    url = setUrl(game)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        
        # method to accept cookies, otherwise it will not show regional prices
        try:
            page.locator("#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
        except Exception as e:
            print(f"No se encontro el boton de cookies: {e}")

        # only after reload the prices will be correct
        page.reload()
        result = page.content()
        page.close()  
        browser.close()
        
    doc = bs4(result, "html.parser")
    gameList = doc.find("div", class_="paginated-products-grid grid")

    if not gameList:
        not_found_result ="GAME NOT FOUND ON GOG."
        return not_found_result

    gameData = gameList.find("a")

    if not gameData:
        not_found_result ="GAME NOT FOUND ON GOG."
        return not_found_result
    
    gameTitle2 = gameData.find("product-title", class_="small")
    gameTitle = gameTitle2.find("span")
    gameOrPrice = gameData.find("span", class_="base-value ng-star-inserted")
    gameDiscount = gameData.find("price-discount", class_="ng-star-inserted")
    gameFinalPrice = gameData.find("span", class_="final-value ng-star-inserted")

    if gameTitle:
        # some games dont have prices, that is why the else statement here
        title = gameTitle.text
        price = gameOrPrice.text if gameOrPrice else (gameFinalPrice.text if gameFinalPrice else '-')
        discount = gameDiscount.text if gameDiscount else '-'
        finalPrice = gameFinalPrice.text if gameFinalPrice else '-'

    # text result to send to main
    result_text =(
        f"GOG RESULT:\n"
        f"TITLE: {title}\n"
        f"ORIGINAL PRICE: {price}\n"
        f"DISCOUNT: {discount}\n"
        f"FINAL PRICE: {finalPrice}\n"
    )
    return result_text

