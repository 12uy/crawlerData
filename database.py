import mysql.connector

def connectDb():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="newsdb"
    )
    return conn


def insert_data(title, content, shortdesc, categoryid, htmlPage):
    conn = connectDb()

    mycursor = conn.cursor()
    sql = """INSERT INTO news (createdby , title , content, shortdescription, category_id, htmlPage ) VALUES (%s, %s, %s, %s, %s, %s)"""
    value = ("admin", title, content, shortdesc, categoryid, htmlPage)
    mycursor.execute(sql,value)
    conn.commit()
    print(mycursor.rowcount, "record inserted.")
    conn.close()

def get_data():
    conn = connectDb()

    mycursor = conn.cursor()
    mycursor.execute("SELECT id, content FROM news limit 80,40") # limit x, y lay y dong tu thu tu thu x
    myresult = mycursor.fetchall()
    return myresult
    conn.close()

def get_all_data():
    conn = connectDb()

    mycursor = conn.cursor()
    mycursor.execute("SELECT id, content FROM news")
    myresult = mycursor.fetchall()
    return myresult
    conn.close()

def updateData(idnews , links):
    conn = connectDb()

    mycursor = conn.cursor()
    sql = """UPDATE news SET LinkTTS = %s WHERE id = %s"""
    value = (links, idnews)
    mycursor.execute(sql, value)
    conn.commit()
    print(mycursor.rowcount, "record(s) affected")
    print(links)
    conn.close()

def updateTomTat(idnews, tomtat):
    conn = connectDb()

    mycursor = conn.cursor()
    sql = """UPDATE news SET tomtat = %s WHERE id = %s"""
    value = (tomtat, idnews)
    mycursor.execute(sql, value)
    conn.commit()
    print(mycursor.rowcount, "record(s) affected")
    print(tomtat)
    conn.close()