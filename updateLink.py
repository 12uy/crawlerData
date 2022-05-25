from database import get_data
from tts import textToSpeech
from database import updateData

for item in get_data():
    idnews = item[0]
    content = item[1]
    try:
        links = textToSpeech(content)
        updateData(idnews , links)
    except:
        print(idnews)
        break



