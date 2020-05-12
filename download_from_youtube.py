import webbrowser
url = input("Cole a url do video do youtube: ")
download = url[:12] + 'ss' + url[:12]
webbrowser.open(download)