from bs4 import BeautifulSoup as bs4
import requests
import time



def setUrl(gameName):
    gameNameAdapted = gameName.replace(" ","+")
    url = 'https://www.xbox.com/es-AR/search/results/games?q='+ gameNameAdapted +'&PlayWith=PC'
    return url


def search():
    pass
