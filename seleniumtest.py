from selenium import webdriver
from time import sleep
url = "http://www.foxnews.com/us/2016/07/05/america-celebrates-its-independence.html"
driver = webdriver.Chrome()
driver.get(url)
sleep(5)
commentHTML = driver.find_elements_by_class_name('fyre-comment-body')
text = [comment.text for comment in commentHTML]
print text
