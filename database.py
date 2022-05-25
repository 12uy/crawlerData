import mysql.connector


def insert_data(title, content, shortdesc, categoryid):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="newsdb"
    )

    mycursor = conn.cursor()
    sql = """INSERT INTO new (createdby , title , content, shortdescription, category_id ) VALUES (%s, %s, %s, %s, %s)"""
    value = ("admin", title, content, shortdesc, categoryid)
    mycursor.execute(sql, value)
    conn.commit()
    print(mycursor.rowcount, "record inserted.")
    conn.close()

def get_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="newsdb"
    )

    mycursor = conn.cursor()
    mycursor.execute("SELECT id, content FROM news limit 0,3")
    myresult = mycursor.fetchall()
    return myresult
    conn.close()

def updateData(idnews , links):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="newsdb"
    )

    mycursor = conn.cursor()
    sql = """UPDATE news SET LinkTTS = %s WHERE id = %s"""
    value = (links, idnews)
    mycursor.execute(sql, value)
    conn.commit()
    print(mycursor.rowcount, "record(s) affected")
    print(links)
    conn.close()