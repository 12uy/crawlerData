import requests
from database import get_all_link

def download_audio(fileName,url):
    try:
        while 1:
            r = requests.get(url)
            if(r.status_code==404):
                print("error "+ fileName)
                continue
            saveTo = "/home/ruy/Downloads/TTS/" +str(fileName)+".mp3"
            with open(saveTo, 'wb+') as f:
                f.write(r.content)
            print("ok")
            break
    except:
        print("error")
    finally:
        f.close()


for item in get_all_link():
    idnews = item[0]
    link = item[1]
    download_audio(idnews,link)
