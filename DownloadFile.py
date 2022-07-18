import requests

def download_audio(fileName,url):
    try:
        r = requests.get(url)
        saveTo = "/home/ruy/Downloads/TTS/" +str(fileName)+".mp3"
        with open(saveTo, 'wb+') as f:
            f.write(r.content)
        print("ok")
    except:
        print("error")
    finally:
        f.close()

