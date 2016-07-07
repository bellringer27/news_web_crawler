import socket
import MySQLdb
print("[Server]: Attempting to start server.")
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 5005
connected = False
accepting = True
soc.bind(('',port))
soc.listen(5)
print("[Server]: Started server.")
print("[Server]: Accepting connections on port "+port)
while accepting == True:
    (conn, addr)=soc.accept()
    connected = True
    print ("[Server]: Got connection from "+addr)
    while connected == True:
        msg = conn.recv(1024)
        if msg:
            data_list = msg.split('++')
            site = data_list[0]
            title = data_list[1]
            author = data_list[2]
            date = data_list[3]
            article = data_list[4]
            db = MySQLdb.connect(host="localhost",
                                 user = "root",
                                 passwd="root",
                                 db="news_web_crawler")
            cur = db.cursor()
            cur.execute("INSERT INTO articles (article_site,article_title,article_author,article_date,article_data) VALUES(site,title,author,date,article)")
            id = cursor.lastrowid
            db.commit()
            for i in xrange(5,len(data_list)):
                comment_parts = data_list.split('-+-')
                cur.execute("INSERT INTO comments (comment_article_id, comment_id,comment_author,comment_data) VALUES (id,i-4,comment_parts[0],comment_parts[1])")
            db.commit()
            db.close()
