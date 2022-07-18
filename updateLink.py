from database import get_data
from tts import textToSpeech
from DownloadFile import download_audio
from database import updateData


for item in get_data():
    idnews = item[0]
    content = item[1]
    try:
        links = textToSpeech(content)
        updateData(idnews, links)
        print(links)
        # download_audio(idnews,links)
    except:
        print(idnews)
        pass



