'''

'''
import codecs
import socket
from selenium import webdriver
from time import sleep
class comment(object): #Declares comment class for later use
    def __init__(self,user,data):
        self.user = user
        self.data = data
server_address = ('48.218.255.24',5005)
driver = webdriver.Chrome()
while True:
    print"Enter the URL you wish to crawl..."
    print'Usage -"http://phocks.org"/stumble/creepy/"<-- With the double quotes'
    myurl = input("@>") #Recieve the url.
    driver.get(myurl)
    sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    if(myurl.find("cnn.com")!=-1): #Specified code for CNN sites
        site = 'CNN'
        title = driver.find_element_by_class_name('pg-headline').text
        author = driver.find_element_by_class_name('metadata__byline__author').text
        article_list = driver.find_elements_by_class_name('zn-body__paragraph')
        article =''
        for i in article_list:
            article = article +"\n"+i.text
        date = driver.find_element_by_class_name('update-time').text
        comments = [comment("N/A","N/A")]
    elif(myurl.find("foxnews.com")!=-1): #Specified code for Fox News sites
        site = 'FOX News'
        title = driver.page_source[driver.page_source.find('<h1 itemprop="headline">')+24:driver.page_source.find('<div class="article-info">')-7]
        author = "No Author"
        article = driver.find_element_by_class_name('article-text').text
        date = driver.page_source[driver.page_source.find('pubDate:"')+9:driver.page_source.find('myTopChannelName')-6]
        x=0
        while ('<div class="fyre-stream-more" style="display: none;">' not in driver.page_source) and x<15:
            try:
                driver.find_element_by_class_name('fyre-stream-more').click()
                x+=1
                sleep(6)
            except:
                sleep(2)

        comment_data = driver.find_elements_by_class_name('fyre-comment-body')
        comment_user = driver.find_elements_by_class_name('fyre-comment-username')
        comments = []
        for i in xrange(0,len(comment_data)):
            comments.append(comment(comment_user[i].text,comment_data[i].text))
    elif(myurl.find("washingtonpost.com")!=-1): #Specified code for Washington Post sites.
        sleep(6)
        site = 'Washington Post'
        title = driver.page_source[driver.page_source.find('<h1 data-pb-field="customFields.web_headline" itemprop="headline">')+66:driver.page_source.find('</h1>')]
        author = driver.find_element_by_class_name('pb-byline').text
        article = driver.find_element_by_id('article-body').text
        date = driver.find_element_by_class_name('pb-timestamp').text
        driver.find_element_by_class_name('echo-apps-conversations-streamingState-live').click()
        sleep(10)
        x=0
        while('<div class="echo-streamserver-controls-stream-more" style="display: none;"' not in driver.page_source) and x<15:
            try:
                driver.find_element_by_class_name('echo-streamserver-controls-stream-more').click()
                x+=1
                sleep(10)
            except:
                sleep(2)

        comment_data = driver.find_elements_by_class_name('echo-streamserver-controls-stream-item-text')
        comment_user = driver.find_elements_by_class_name('echo-streamserver-controls-stream-item-authorName')
        comments = []
        for i in xrange(0,len(comment_data)):
            comments.append(comment(comment_user[i].text,comment_data[i].text))
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(server_address)
    msg = site+']['+title+']['+author+']['+date+']['+article
    for i in xrange(0,len(comments)):
        msg = msg+']['+comments[i].user+'}{'+comments[i].data
    try:
        msg = msg+'qwertyend'
        sock.sendall(msg.encode('utf-8'))
    finally:
        sock.close()
    
