'''

'''
import urllib2
import codecs
from selenium import webdriver
from time import sleep
class comment(object):
    def __init__(self,user,data):
        self.user = user
        self.data = data
driver = webdriver.Chrome()
while True:
    print"Enter the URL you wish to crawl..."
    print'Usage -"http://phocks.org"/stumble/creepy/"<-- With the double quotes'
    myurl = input("@>")
    driver.get(myurl)
    sleep(3)
    if(myurl.find("cnn.com")!=-1):
        title = driver.find_element_by_class_name('pg-headline').text
        author = driver.find_element_by_class_name('metadata__byline__author').text
        article_list = driver.find_elements_by_class_name('zn-body__paragraph')
        article =''
        for i in article_list:
            article = article +"\n"+i.text
        date = driver.find_element_by_class_name('update-time').text
        comments = [comment("N/A","N/A")]
    elif(myurl.find("foxnews.com")!=-1):
        title = driver.page_source[driver.page_source.find('<h1 itemprop="headline">')+24:driver.page_source.find('<div class="article-info">')-7]
        author = "No Author"
        article = driver.find_element_by_class_name('article-text').text
        date = driver.page_source[driver.page_source.find('pubDate:"')+9:driver.page_source.find('myTopChannelName')-6]
        while '<div class="fyre-stream-more">' in driver.page_source:
            driver.find_element_by_class_name('fyre-stream-more').click()
            sleep(2)
        comment_data = driver.find_elements_by_class_name('fyre-comment-body')
        comment_user = driver.find_elements_by_class_name('fyre-comment-username')
        comments = []
        for i in xrange(0,len(comment_data)):
            comments.append(comment(comment_user[i].text,comment_data[i].text))
    elif(myurl.find("washingtonpost.com")!=-1):
        title = driver.page_source[driver.page_source.find('<h1 data-pb-field="customFields.web_headline" itemprop="headline">')+66:driver.page_source.find('</h1>')]
        author = driver.find_element_by_class_name('pb-byline').text
        article = driver.find_element_by_id('article-body').text
        date = driver.find_element_by_class_name('pb-timestamp').text
        driver.find_element_by_class_name('echo-apps-conversations-streamingState').click()
        sleep(4)
        x=0
        while('<div class="echo-streamserver-controls-stream-more"' in driver.page_source) and x<15:
            driver.find_element_by_class_name('echo-streamserver-controls-stream-more').click()
            x+=1
            sleep(5)
        comment_data = driver.find_elements_by_class_name('echo-streamserver-controls-stream-item-text')
        comment_user = driver.find_elements_by_class_name('echo-streamserver-controls-stream-item-authorName')
        comments = []
        for i in xrange(0,len(comment_data)):
            comments.append(comment(comment_user[i].text,comment_data[i].text))
         
  #  print(title)
    #print(author)
   # print(date)
    #print(article)
    print(comments[0].user+" "+comments[0].data)



        
