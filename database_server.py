import socket
import MySQLdb
print("[Server]: Attempting to start server.")
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 5005
connected = False
accepting = True
soc.bind(('0.0.0.0',port))
soc.listen(5)
print("[Server]: Started server.")
print("[Server]: Accepting connections on port ",port)
dsite = ""
while accepting == True:
    (conn, addr)=soc.accept()
    print '[Server]: Got connection from ',addr
    if True:
        waiting = True
        msg = ""
        while waiting == True:
            msgf = conn.recv(1073741824)
            msgf = msg.decode('utf-8')
            msg = msg+''+msgf
            if(msg.find("qwertyend")!=-1):
                waiting = False
        if msg:
            data_list = msg.split('][')
            dsite = data_list[0]
            title = data_list[1]
            author = data_list[2]
            date = data_list[3]
            article = data_list[4]
            db = MySQLdb.connect(host="localhost",
                                 user = "root",
                                 passwd="root",
                                 db="news_web_crawler")
            db.set_character_set('utf8')
            cur = db.cursor()
            q = "INSERT INTO articles (article_site,article_title,article_author,article_date,article_data) VALUES(%s,%s,%s,%s,%s)"
            db.commit()
            cur.execute(q,(dsite,title,author,date,article))
            id = cur.lastrowid
            for i in xrange(5,len(data_list)):
                comment_parts = data_list[i].split('}{')
                q="INSERT INTO comments (comment_article_id,comment_author,comment_data) VALUES (%s,%s,%s)"
                cur.execute(q,(id,comment_parts[0],comment_parts[1]))
            db.commit()
            db.close()
