import steam
import gog
import xbox
import tkinter
import threading
import os

# this is to make the main.exe work
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = ".local-browsers"


def get_search():
    game = search_box.get()

    # checks for empty entry
    if not game.strip():
        steam_label.config(text = "No entry detected")
        gog_label.config(text = "No entry detected")
        xbox_label.config(text = "No entry detected")
        return
    
    # temporal messages while search not finished
    steam_label.config(text = "Searching on STEAM...")
    gog_label.config(text = "Searching on GOG...")
    xbox_label.config(text = "Searching on XBOX...")

    # separate the search using a thread so the window remains responsive 
    threading.Thread(target=perform_search, args=(game,), daemon=True).start()


def perform_search(game):

    steam_result = steam.search(game)
    gog_result = gog.search(game)
    xbox_result = xbox.search(game)

    # show results
    steam_label.config(text=steam_result)
    gog_label.config(text=gog_result)
    xbox_label.config(text=xbox_result)


def global_search(game):
    steam.search(game)
    xbox.search(game)
    gog.search(game)

window = tkinter.Tk()
window.geometry("900x300")
window.title("Game Price Comparator")

search_box = tkinter.Entry(window, width=50, font="bold")
search_box.grid(row=0, column=0, columnspan=3, pady=10)

button = tkinter.Button(window, text = "Search", command = get_search, font="bold", bg="lightyellow")
button.grid(row=1, column=0, columnspan=3, pady=5)

steam_label = tkinter.Label(window, text="STEAM", wraplength=250, justify="left", anchor="nw", bg="lightblue", relief="ridge", font="bold")
steam_label.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

gog_label = tkinter.Label(window, text="GOG", wraplength=250, justify="left", anchor="nw", bg="#dbcae3", relief="ridge", font="bold")
gog_label.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")

xbox_label = tkinter.Label(window, text="XBOX", wraplength=250, justify="left", anchor="nw", bg="lightgreen", relief="ridge", font="bold")
xbox_label.grid(row=2, column=2, padx=5, pady=10, sticky="nsew")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()