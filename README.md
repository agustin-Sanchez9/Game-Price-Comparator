# Game-Price-Comparator

Aplicación diseñada para scrapear precios de las juegos desde las tiendas de steam, gog y xbox.

Se utilizaron las librerías requests y playwright de pyton para realizar el scrapping, y se utilizo BeautifulSoup 4 para el parseo del HTML obtenido.

Luego se uso pyinstaller para hacer del código una aplicación de escritorio totalmente funcional, sin necesidad de instalar previamente ni python ni ninguna de las librerias usadas.

El único problema es que los browser usados por playwright son demasiado pesados (192MiB) como para estar incluidos en el repositorio, por lo que están almacenados por separado en una carpeta de Google Drive.

link: https://drive.google.com/drive/folders/11zL3J9Ww2YiTDbnUNtgD-_QN8ao3wo3C?usp=drive_link

Una vez descargada ".local-browsers" debe adjuntarse en la carpeta "dist" de la aplicación, reconocerá la carpeta dado que es la que tan solo contiene el archivo "main.exe".

El uso de la aplicación es intuitivo y sencillo, tan solo deberá escribir en la casilla de texto el nombre del juego que quiera comparar los precios, luego presionar el botón "Search" y al cabo de unos segundos aparecerán en pantalla el precio del juego en todas las tiendas.

Se recomienda que escriba el nombre del juego lo mas especifico posible para asegurarse que obtenga el resultado esperado.

En ciertas ocasiones aunque el juego no este presente en alguna de las tiendas recibirá igual un resultado,  por lo tanto se recomienda estar atento a los títulos que se obtienen dado que pueda llevar a pensar que en una tienda dicho juego es mas barato pero al prestar atención uno puede notar que el titulo no es el mismo que buscó.


