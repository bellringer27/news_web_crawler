import MySQLdb


db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="root",
                     db = "news_web_crawler")
cur = db.cursor()
cur.execute("INSERT INTO comments (comment_article_id,comment_id,comment_author,comment_data) VALUES('19200','19200','cantrell','lol')")
db.commit()
db.close()
