import webbrowser

def abrir_youtube():
    # URL de la canción "Mónaco" de Desakata2 en YouTube
    url = "https://www.youtube.com/watch?v=OofkFIcvrGU&list=RDOofkFIcvrGU&start_radio=1"
    
    # Abrir la URL en el navegador predeterminado
    webbrowser.open(url)

if __name__ == "__main__":
    abrir_youtube()