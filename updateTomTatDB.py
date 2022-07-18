from database import get_all_data
from database import updateTomTat
from tomtat import tomtat

for item in get_all_data():
    idnews = item[0]
    content = item[1]
    try:
        result = tomtat(content)
        updateTomTat(idnews , result)
    except:
        print(idnews)
        pass